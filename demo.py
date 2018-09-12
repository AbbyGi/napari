import sys

import vispy
from PyQt5.QtWidgets import QApplication, QAction
import numpy as np

from gui.elements.image_widget import ImageWidget
from vispy import app, gloo, visuals, scene

from gui.elements.image_window import ImageWindow
from gui.napari_application import NapariApplication
from gui.utils.example_data_utils import load_bluemarble_image

app.use_app('pyqt5')


def open_2Drgb(win):
    # opening a 2D RGB image:
    image = load_bluemarble_image(large=False)
    meta = dict(name='BlueMarble', itype='rgb')
    win.add_image(image, meta)


def open_2Dsc(win):
    # opening a 2D single channel image:
    h = 5120
    w = 5120
    Y, X = np.ogrid[-2.5:2.5:h * 1j, -2.5:2.5:w * 1j]
    image = np.empty((h, w), dtype=np.float32)
    image[:] = np.random.rand(h, w)
    image[-30:] = np.linspace(0, 1, w)
    meta = dict(name='2D1C', itype='mono')
    viewer = win.add_image(image, meta)
    viewer.cmap = 'viridis'


def open_3Dsc(win):
    # opening a 3D single channel image:
    h = 512
    w = 512
    d = 512
    Z, Y, X = np.ogrid[-2.5:2.5:h * 1j, -2.5:2.5:w * 1j, -2.5:2.5:d * 1j]
    image = np.empty((h, w, d), dtype=np.float32)
    image[:] = np.exp(- X ** 2 - Y ** 2 - Z ** 2)  # * (1. + .5*(np.random.rand(h, w)-.5))
    # image[-30:] = np.linspace(0, 1, w)
    meta = dict(name='3D1C', itype='mono')
    viewer = win.add_image(image, meta)
    viewer.cmap = 'blues'


def open_4dsc(win):
    # opening a 4D single channel image:
    h = 32
    w = 32
    d = 64
    b = 64
    C, Z, Y, X = np.ogrid[-2.5:2.5:h * 1j, -2.5:2.5:w * 1j, -2.5:2.5:d * 1j, -2.5:2.5:b * 1j]
    image = np.empty((h, w, d, b), dtype=np.float32)
    image[:] = np.exp(- X ** 2 - Y ** 2 - Z ** 2 - C ** 2)  # * (1. + .5*(np.random.rand(h, w)-.5))
    # image[-30:] = np.linspace(0, 1, w)
    meta = dict(name='4D1C', itype='mono')
    viewer = win.add_image(image, meta)
    viewer.cmap = 'blues'


if __name__ == '__main__':
    # starting
    application = NapariApplication(sys.argv)

    win = ImageWindow()

    open_2Drgb(win)
    open_2Dsc(win)
    open_3Dsc(win)
    open_4dsc(win)

    win.resize(win.layout().sizeHint())
    win.show()
    win.raise_()

    sys.exit(application.exec_())
