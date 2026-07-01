from AppKit import (
    NSApplication,
    NSWindow,
    NSWindowStyleMaskBorderless,
    NSBackingStoreBuffered,
)

from AppKit import NSScreen

from AppKit import NSView

from AppKit import NSDictionary


from AppKit import (
    NSColor,
    NSForegroundColorAttributeName,
    NSFont,
    NSFontAttributeName,
    NSString,
    NSBezierPath,
)

from Quartz import CGRectMake, kCGScreenSaverWindowLevel

# in cocoas coordinate system (0,0) is bottom left hand corner

# what is the difference between Quartz and AppKit?
# Quartz is more low-level whereas AppKit is more high level
# Quartz is the underlying graphics engine


# ---------------------------------- SCREENS & FRAMES --------------------------------- #

screens = NSScreen.screens()
# frame = NSScreen.mainScreen().frame()

# screen represents the physical display itself - you need frame to extract position and size
# other properties can include:
# backingScaleFactor() - retina scale
# colorSpace() - color profile
# visibleFrame() - usable area exlcuding dock and menu

screen = screens[0]
frame = screen.frame()
w = frame.size.width
h = frame.size.height

# ---------------------------------- APP --------------------------------- #

app = NSApplication.sharedApplication()

# ---------------------------------- WINDOWS --------------------------------- #

# window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
#     CGRectMake(100, 100, 800, 600),
#     NSWindowStyleMaskBorderless,
#     NSBackingStoreBuffered,
#     False,  # why is false added? create the window immediately rather than waiting for it to be shown
# )

# NSWindow.alloc() allocates memory for the object
# styling is a transferal between objective-c to pyobjc

# different methods:
# window with just a rectangle: window = NSWindow.alloc().initWithContentRect_(rect)
# specific screen: window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_screen_(
#     rect, style, backing, defer, screen  # adds an extra param for screen
# )

# alternatives to NSWindowStyleMaskBorderless
# NSWindowStyleMaskTitled - title bar with window name
# NSWindowStyleMaskClosable - adds close button (red dot)
# NSWindowStyleMaskMiniaturizable - minimisable e.g. yellow dot
# NSWindowStyleMaskResizable
# NSWindowStyleMaskFullScreen
# they can be combined using | (bitwise OR)

# NSBackingStoreBuffered
# buffered = double buffering - draws the frame offscreen first then swaps it onto the screen
# NSBackingStoreRetained - draws directly to screen (this can cause flickering)

# ---------------------------------- CUSTOM CLASS --------------------------------- #

# why do we use NSDictionary?
# When PyObjC bridges Python to Objective-C,
# the method expects an Objective-C object as the attributes argument, specifically an NSDictionary
# if you pass a plain python dictionary e.g. {"color": NSColor.whiteColor()} this won't work
# You need to use Cocoa's own dictionary type:
# NSDictionary.dictionaryWithObjects_forKeys_(
#     [NSColor.whiteColor(), NSFont.boldSystemFontOfSize_(20)],  # values
#     [NSForegroundColorAttributeName, NSFontAttributeName],      # keys
# )


# class MyView(NSView):
#     def drawRect_(self, rect):
#         w = self.frame().size.width
#         h = self.frame().size.height

#         attrs = NSDictionary.dictionaryWithObjects_forKeys_(
#             [NSColor.whiteColor(), NSFont.boldSystemFontOfSize_(20)],
#             [NSForegroundColorAttributeName, NSFontAttributeName],
#         )

#         label = NSString.stringWithString_("hello")
#         label.drawAtPoint_withAttributes_((100, 100), attrs)

ROWS = 3
COLS = 3


class MyView(NSView):
    def drawRect_(self, rect):
        w = self.frame().size.width
        h = self.frame().size.height

        attrs = NSDictionary.dictionaryWithObjects_forKeys_(
            [NSColor.whiteColor(), NSFont.boldSystemFontOfSize_(20)],
            [NSForegroundColorAttributeName, NSFontAttributeName],
        )

        label = NSString.stringWithString_("hello")
        label.drawAtPoint_withAttributes_((100, 100), attrs)

        # # work out the centre points of each grid square...
        # label = NSString.stringWithString_("7")
        # label.drawAtPoint_withAttributes_((int(w / 6), int(h / 6)), attrs)

        # label = NSString.stringWithString_("4")
        # label.drawAtPoint_withAttributes_((int(w / 6), int(3 * h / 6)), attrs)

        # label = NSString.stringWithString_("1")
        # label.drawAtPoint_withAttributes_((int(w / 6), int(5 * h / 6)), attrs)

        # label = NSString.stringWithString_("2")
        # label.drawAtPoint_withAttributes_((int(3 * w / 6), int(5 * h / 6)), attrs)

        # label = NSString.stringWithString_("3")
        # label.drawAtPoint_withAttributes_((int(5 * w / 6), int(5 * h / 6)), attrs)

        i = 1

        for row in range(ROWS):
            for col in range(COLS):
                label = NSString.stringWithString_(str(i))
                label.drawAtPoint_withAttributes_(
                    ((col + 0.5) * w / COLS, h - (row + 0.5) * h / ROWS), attrs
                )

                i = i + 1

        # path.moveToPoint_((int(w / 3), 0))
        # path.lineToPoint_((int(w / 3), h))

        # path.moveToPoint_((int(2 * w / 3), 0))
        # path.lineToPoint_((int(2 * w / 3), h))

        # path.moveToPoint_((0, int(h / 3)))
        # path.lineToPoint_((w, int(h / 3)))

        # path.moveToPoint_((0, int(2 * h / 3)))
        # path.lineToPoint_((w, int(2 * h / 3)))

        NSColor.whiteColor().setStroke()
        path = NSBezierPath.bezierPath()

        for col in range(1, COLS):
            x = col * w / COLS
            path.moveToPoint_((x, 0))
            path.lineToPoint_((x, h))

        for row in range(1, ROWS):
            y = row * h / ROWS
            path.moveToPoint_((0, y))
            path.lineToPoint_((w, y))

        path.stroke()


window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
    CGRectMake(frame.origin.x, frame.origin.y, w, h),  # x, y, width, height
    NSWindowStyleMaskBorderless,
    NSBackingStoreBuffered,
    False,
)

# ---------------------------------- APP ACTIVATION POLICY --------------------------------- #

app.setActivationPolicy_(0)

# 0 = NSApplicationActivationPolicyRegular
# 1 = NSApplicationActivationPolicyAccessory
# 2 = NSApplicationActivationPolicyProhibited

window.orderFrontRegardless()

window.setLevel_(kCGScreenSaverWindowLevel)  # always on top
window.setBackgroundColor_(NSColor.colorWithRed_green_blue_alpha_(0, 0, 0, 0.4))
window.setOpaque_(False)  # tells macOS the window has transparency
window.setIgnoresMouseEvents_(True)  # clicks pass through

# view = MyView.alloc().initWithFrame_(CGRectMake(0, 0, 800, 600))
view = MyView.alloc().initWithFrame_(CGRectMake(0, 0, w, h))
window.setContentView_(view)

app.run()
# this starts an event loop
# it must be the last line because the code is blocking
# nothing after it will execute until the app quits
