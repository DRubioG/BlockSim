import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DragAndDropExample:
    def __init__(self):
        # Crear la ventana principal
        # self.window = Gtk.Window(Gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Drag and Drop Example")
        self.window.set_size_request(300, 200)
        self.window.connect("destroy", lambda w: Gtk.main_quit())

        # Crear una etiqueta y hacerla arrastrable
        label = Gtk.Label("Arrastra y suelta aquí")
        label.set_size_request(200, 100)
        label.drag_source_set(Gtk.gdk.BUTTON1_MASK, [], Gtk.gdk.ACTION_COPY)
        label.connect("drag-data-get", self.on_drag_data_get)

        # Crear una etiqueta receptora para soltar
        drop_label = Gtk.Label("Suelta aquí")
        drop_label.set_size_request(200, 100)
        drop_label.drag_dest_set(Gtk.DEST_DEFAULT_ALL, [], Gtk.gdk.ACTION_COPY)
        drop_label.connect("drag-data-received", self.on_drag_data_received)

        # Agregar las etiquetas a la ventana
        vbox = Gtk.VBox()
        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(drop_label, True, True, 0)
        self.window.add(vbox)

        self.window.show_all()

    def on_drag_data_get(self, widget, context, data, info, time):
        selected_text = "Texto de ejemplo"
        data.set_text(selected_text, len(selected_text))

    def on_drag_data_received(self, widget, context, x, y, data, info, time):
        text = data.get_text()
        print("Texto recibido:", text)

if __name__ == '__main__':
    DragAndDropExample()
    Gtk.main()