"""
Grid overlay for voice-controlled positioning.
Reference: Claude Sonnet 4.6
"""

import json
import os
import threading
import time
from AppKit import (
    NSApplication,
    NSPanel,
    NSColor,
    NSView,
    NSWindowStyleMaskBorderless,
    NSBackingStoreBuffered,
    NSScreen,
    NSBezierPath,
    NSEvent,
    NSKeyDownMask,
    NSFont,
    NSString,
    NSForegroundColorAttributeName,
    NSFontAttributeName,
    NSDictionary,
)
from Quartz import CGRectMake, kCGScreenSaverWindowLevel

from config import COLS, ROWS, CANVAS_TOP_LEFT_X, CANVAS_TOP_LEFT_Y, CANVAS_W, CANVAS_H

# COLS = 15
# ROWS = 10
FIGMA_NODES_PATH = "figma_nodes.json"

# CANVAS_TOP_LEFT_X = 0
# CANVAS_TOP_LEFT_Y = 76
# CANVAS_W = 1470
# CANVAS_H = 956 - 76


def load_figma_nodes():
    try:
        with open(FIGMA_NODES_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"could not load figma_nodes.json: {e}")
        return None


def setup_quit_handler(app):
    NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(
        NSKeyDownMask,
        lambda event: (
            app.terminate_(None) if event.charactersIgnoringModifiers() == "q" else None
        ),
    )


class GridView(NSView):
    def drawRect_(self, rect):
        w = self.frame().size.width
        h = self.frame().size.height

        cell_w = w / COLS
        cell_h = h / ROWS

        # grid lines
        NSColor.colorWithRed_green_blue_alpha_(0.5, 0.5, 0.5, 0.8).setStroke()
        path = NSBezierPath.bezierPath()
        path.setLineWidth_(1.0)

        for col in range(1, COLS):
            path.moveToPoint_((col * cell_w, 0))
            path.lineToPoint_((col * cell_w, h))

        for row in range(1, ROWS):
            path.moveToPoint_((0, row * cell_h))
            path.lineToPoint_((w, row * cell_h))

        path.stroke()

        # grid cell numbers
        grid_attrs = NSDictionary.dictionaryWithObjects_forKeys_(
            [
                NSColor.colorWithRed_green_blue_alpha_(0.5, 0.5, 0.5, 0.8),
                NSFont.boldSystemFontOfSize_(14),
            ],
            [NSForegroundColorAttributeName, NSFontAttributeName],
        )

        for row in range(ROWS):
            for col in range(COLS):
                number = row * COLS + col + 1
                label = NSString.stringWithString_(str(number))
                x = col * cell_w + 10
                y = h - (row + 1) * cell_h + cell_h - 25
                label.drawAtPoint_withAttributes_((x, y), grid_attrs)

        # figma node labels
        data = load_figma_nodes()
        if not data:
            return

        nodes = data.get("nodes", [])
        vp = data.get("viewport", {})
        if not vp:
            return

        zoom = vp.get("zoom", 1)
        vp_x = vp.get("x", 0)
        vp_y = vp.get("y", 0)

        node_attrs = NSDictionary.dictionaryWithObjects_forKeys_(
            [NSColor.whiteColor(), NSFont.boldSystemFontOfSize_(10)],
            [NSForegroundColorAttributeName, NSFontAttributeName],
        )

        canvas_cocoa_origin_y = h - CANVAS_TOP_LEFT_Y - CANVAS_H

        for node in nodes:
            try:
                screen_x = (node["x"] - vp_x) * zoom
                screen_y = CANVAS_H - (
                    (node["y"] - vp_y) * zoom
                )  # cocoa Y flip within canvas height

                # screen_x = CANVAS_TOP_LEFT_X + (node["x"] - vp_x) * zoom
                # screen_y = (
                #     canvas_cocoa_origin_y + CANVAS_H - ((node["y"] - vp_y) * zoom)
                # )

                label_text = f"{node['name']}  ({node['id']})"
                label_w = len(label_text) * 6

                NSColor.colorWithRed_green_blue_alpha_(0.5, 0.5, 0.5, 0.8).setFill()
                NSBezierPath.fillRect_(CGRectMake(screen_x, screen_y, label_w, 17))

                label = NSString.stringWithString_(label_text)
                label.drawAtPoint_withAttributes_(
                    (screen_x + 4, screen_y + 3), node_attrs
                )
            except Exception as e:
                print(f"error drawing node {node.get('name', '?')}: {e}")


def watch_file(path, view):
    last_modified = None
    while True:
        try:
            current_modified = os.path.getmtime(path)
            if last_modified is None:
                last_modified = current_modified
            if current_modified != last_modified:
                last_modified = current_modified
                print("file changed - redrawing")
                view.performSelectorOnMainThread_withObject_waitUntilDone_(
                    "setNeedsDisplay:", True, False
                )
        except Exception as e:
            print(f"watcher error: {e}")
        time.sleep(0.2)


if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(0)

    screen = NSScreen.screens()[0].frame()
    w = screen.size.width
    h = screen.size.height

    print(f"screen: {w} x {h}")

    window = NSPanel.alloc().initWithContentRect_styleMask_backing_defer_(
        CGRectMake(
            CANVAS_TOP_LEFT_X,
            h - CANVAS_TOP_LEFT_Y - CANVAS_H,  # cocoa coordiante system adaptation
            CANVAS_W,
            CANVAS_H,
        ),
        NSWindowStyleMaskBorderless,
        NSBackingStoreBuffered,
        False,
    )
    window.setLevel_(kCGScreenSaverWindowLevel)
    window.setBackgroundColor_(NSColor.colorWithRed_green_blue_alpha_(0, 0, 0, 0))
    window.setOpaque_(False)
    window.setIgnoresMouseEvents_(True)
    window.setHidesOnDeactivate_(False)

    view = GridView.alloc().initWithFrame_(CGRectMake(0, 0, w, h))
    window.setContentView_(view)
    window.orderFrontRegardless()

    watcher = threading.Thread(
        target=watch_file, args=(FIGMA_NODES_PATH, view), daemon=True
    )
    watcher.start()

    setup_quit_handler(app)
    print("overlay running - press q to quit")
    app.run()
