"""
Global fixtures to allow testing tkinter apps.
"""
import pytest

@pytest.fixture(autouse=True)
def patch_mainloop(monkeypatch):
    do_nothing = lambda x: None
    monkeypatch.setattr("tkinter.Tk.mainloop", do_nothing)
