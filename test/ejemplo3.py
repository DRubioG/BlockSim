import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class DragAndDropExample(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Drag and Drop Example")
        self.set_size_request(300, 200)
        self.connect("destroy", Gtk.main_quit)

        # Crear una etiqueta y hacerla arrastrable
        label = Gtk.Label()
        label.set_text("Arrastra y suelta aquí")
        label.drag_source_set(Gtk.TargetEntry.new("text/plain", 0, 0), Gdk.DragAction.COPY)
        label.connect("drag-data-get", self.on_drag_data_get)

        # Crear una etiqueta receptora para soltar
        drop_label = Gtk.Label()
        drop_label.set_text("Suelta aquí")
        drop_label.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY)
        drop_label.connect("drag-data-received", self.on_drag_data_received)

        # Agregar las etiquetas a la ventana
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(drop_label, True, True, 0)
        self.add(vbox)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_text = "Texto de ejemplo"
        data.set_text(selected_text, -1)

    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        text = data.get_text()
        print("Texto recibido:", text)

if __name__ == '__main__':
    win = DragAndDropExample()
    win.show_all()
    Gtk.main()