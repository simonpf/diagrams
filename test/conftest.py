"""
Global fixtures to allow testing tkinter apps.
"""
import pytest

class Tk:
    """
    Mock of the tkinter.Tk class.
    """
    def __init__(*args, **kwargs):
        pass

    def mainloop(*args, **kwargs):
        pass

class Canvas:
    """
    Mock of the tkinter.Canvas class.
    """

    def __init__(*args, **kwargs):
        pass

    def create_rectangle(*args, **kwargs):
        pass

    def create_text(*args, **kwargs):
        pass

    def create_line(*args, **kwargs):
        pass

    def create_polygon(*args, **kwargs):
        pass

    def pack(*args, **kwargs):
        pass


@pytest.fixture(autouse=True)
def patch_mainloop(monkeypatch):
    do_nothing = lambda x: None
    monkeypatch.setattr("tkinter.Tk", Tk)
    monkeypatch.setattr("tkinter.Canvas", Canvas)
