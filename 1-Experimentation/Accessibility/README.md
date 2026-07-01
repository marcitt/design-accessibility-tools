
## Questions to Answer

> How to connect the LLM to the actual interface?

Potentially look at overlays with tkinter vs pyqt vs NS vs alternative...?

Screenshot results:
- mss          avg: 69.5ms
- PIL          avg: 345.2ms
- pyautogui    avg: 333.7ms

can be seen mss is quite a bit faster

---
`AX-overlay` is a lot nicer than `pyqt-overlay` in terms of seamless integration and user experience.
It has significantly less interference e.g. it allows clicks through and does not create additional clutter like popups associated with pyqt

Anoter potential method may be something like tkinter