
This is my initial testing and experiment with the macOS AX API and other accessibility tools.

`environment.yaml` - environment required to run these experiments.


- `pyautogui-os-control.ipynb` - Basic commands required for direct mouse and keyboard emulation. `pyqutogui` wraps lower level functionality making this very easy - it is also cross-platform.
- `AX.ipynb` - Quick AX tests in Jupyter Notebook - was looking to see if there's any useful info I can get e.g. from the accessibility tree for configuring the canvas 
- `AX-tutorial` - Bits of code and notes from learning how to use the macOS AX API
- `pyqt-minimal.ipynb` - Basic test with `pyqt` for creating an overlay / app - boilerplate for any future work
- `pyqt-overlay.ipynb` - Created a basic overlay with `pyqt` - soon transitioned to AX overlays for more control
- `AX-overlay`- Replaces implementing an overlay with `pyqt` which allows me to have more control over fine-grained details.

## Questions to Answer

Potentially look at overlays with `tkinter` vs `pyqt` vs NS vs alternative...?
(I ended up using AX - which uses NS)

Screenshot results:
- mss          avg: 69.5ms
- PIL          avg: 345.2ms
- pyautogui    avg: 333.7ms

can be seen mss is quite a bit faster

---
`AX-overlay` is a lot nicer than `pyqt-overlay` in terms of seamless integration and user experience.
It has significantly less interference e.g. it allows clicks through and does not create additional clutter like popups associated with `pyqt`

Another potential method may be something like `tkinter` - but it will likely carry the same issues as `pyqt`