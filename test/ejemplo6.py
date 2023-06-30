import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk

win = Gtk.Window()

def on_event(widget, event):
    # Check if the event is a mouse movement
    if event.type == Gdk.EventType.MOTION_NOTIFY:
        print(event.x, event.y) # Print the mouse's position in the window

t = Gtk.TextView()
t.connect("event", on_event)
win.add(t)

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()