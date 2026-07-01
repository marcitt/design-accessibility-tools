"""
Enables the creation of an overlay with AppKit and Quartz rather than an external python module
This is better for native integration
Reference: Claude Sonnet 4.6
"""

from AppKit import (
    NSApplication,
    NSPanel,
    NSColor,
    NSWindowStyleMaskBorderless,
    NSBackingStoreBuffered,
    NSTimer,
    NSScreen,
)
from Quartz import CGRectMake, kCGScreenSaverWindowLevel


def start_overlay(x, y, width, height):
    rect = CGRectMake(x, y, width, height)
    window = NSPanel.alloc().initWithContentRect_styleMask_backing_defer_(
        rect,
        NSWindowStyleMaskBorderless,
        NSBackingStoreBuffered,
        False,
    )
    window.setLevel_(kCGScreenSaverWindowLevel)  # sets window to float above everything
    window.setBackgroundColor_(NSColor.redColor())
    window.setOpaque_(True)
    window.setIgnoresMouseEvents_(True)
    window.setHidesOnDeactivate_(
        False
    )  # keeps window visible even when another app is focused
    # window.orderFront_(None)
    window.orderFrontRegardless()
    return window


if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(1)  # makes it a proper foreground app
    app.activateIgnoringOtherApps_(True)
    screen = NSScreen.mainScreen().frame()
    cx = screen.size.width / 2
    cy = screen.size.height / 2
    overlay = start_overlay(cx - 150, cy - 100, 300, 200)
    NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
        6.0, app, "terminate:", None, False
    )
    app.run()
