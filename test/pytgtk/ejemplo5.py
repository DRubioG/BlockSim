import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os, sys

class GUI:
    def __init__(self):

        window = Gtk.Window()
        entry = Gtk.Entry()
        entry.connect("activate", self.entry_activated )
        entry.set_alignment(1.0)
        window.add(entry)
        window.show_all()
        window.connect("destroy", self.on_window_destroy )

    def on_window_destroy(self, window):
        Gtk.main_quit()

    def entry_activated (self, entry):
        text = entry.get_text()
        text = text * 2
        entry.set_text(text)
        length = len(text)
        entry.set_position(length)

def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())