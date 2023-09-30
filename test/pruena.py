from calendar import c
import sys
import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
SIZE = 30

class AppWindow(Gtk.ApplicationWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_size_request(450, 550)
		drawingarea = Gtk.DrawingArea()
		# win = ButtonWindow()
		# self.connect("destroy", Gtk.main_quit)
		# drawingarea.add(win)
		self.add(drawingarea)
		drawingarea.connect('draw', self.draw)
		drawingarea.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
		drawingarea.connect('button-press-event', self.on_mouse_pressed)
		

	def on_mouse_pressed(self, da, event, *data):
		print("Hola ", da, event.x, event.y, data)
		self.triangle(event.x, event.y)

	def triangle(self, x=SIZE, y=0):
		# if not ctx:
		# 	ctx = self.ctx
		# ctx.save()
		# ctx.new_path()
		self.ctx.set_source_rgb(0, 0, 0)
		self.ctx.translate(x + SIZE, y + SIZE)
		self.ctx.set_line_width(10)
		# self.ctx.move_to(x, y)
		self.ctx.line_to(x+20, y+200)
		# ctx.line_to(x+8* SIZE, y+0)
		# ctx.rel_line_to(8*SIZE,0)
		# ctx.fill()
		# ctx.close_path()
		# ctx.restore()
		



	# def square(self, ctx):
	# 	ctx.move_to(0, 0)
	# 	ctx.rel_line_to(2 * SIZE, 0)
	# 	ctx.rel_line_to(0, 2 * SIZE)
	# 	ctx.rel_line_to(-2 * SIZE, 0)
	# 	ctx.close_path()
	# def bowtie(self, ctx):
	# 	ctx.move_to(0, 0)
	# 	ctx.rel_line_to(2 * SIZE, 2 * SIZE)
	# 	ctx.rel_line_to(-2 * SIZE, 0)
	# 	ctx.rel_line_to(2 * SIZE, -2 * SIZE)
	# 	ctx.close_path()
		
	# def inf(self, ctx):
	# 	ctx.move_to(0, SIZE)
	# 	ctx.rel_curve_to(0, SIZE, SIZE, SIZE, 2 * SIZE, 0)
	# 	ctx.rel_curve_to(SIZE, -SIZE, 2 * SIZE, -SIZE, 2 * SIZE, 0)
	# 	ctx.rel_curve_to(0, SIZE, -SIZE, SIZE, -2 * SIZE, 0)
	# 	ctx.rel_curve_to(-SIZE, -SIZE, -2 * SIZE, -SIZE, -2 * SIZE, 0)
	# 	ctx.close_path()
		
	def draw_shapes(self, ctx, x, y, fill):
		ctx.save()
		# ctx.new_path()
		# ctx.translate(x + SIZE, y + SIZE)
		# self.bowtie(ctx)
		# # if fill:
		# ctx.fill()
		# else:
		# 	ctx.stroke()
		# ctx.new_path()
		# ctx.translate(3 * SIZE, 0)
		# self.square(ctx)
		# if fill:
		# 	ctx.fill()
		# else:
		# 	ctx.stroke()
		# ctx.new_path()
		# ctx.translate(3 * SIZE, 0)
		# self.triangle(ctx=ctx)
		# if fill:
		# ctx.stroke()
		# else:
		# 	ctx.stroke()
		# ctx.new_path()
		# ctx.translate(3 * SIZE, 0)
		# self.inf(ctx)
		# if fill:
		# 	ctx.fill()
		# else:
		# 	ctx.stroke()
		ctx.restore()
		
	def fill_shapes(self, ctx, x, y):
		self.draw_shapes(ctx, x, y, True)
		
	def stroke_shapes(self, ctx, x, y):
		self.draw_shapes(ctx, x, y, False)
		
	def draw(self, da, ctx):
		ctx.set_source_rgb(0, 0, 0)
		ctx.set_line_width(SIZE / 4)
		ctx.set_tolerance(0.1)
		ctx.set_line_join(cairo.LINE_JOIN_ROUND)
		ctx.set_dash([SIZE / 4.0, SIZE / 4.0], 0)
		self.stroke_shapes(ctx, 0, 0)
		self.ctx = ctx
		# ctx.set_dash([], 0)
		# self.stroke_shapes(ctx, 0, 3 * SIZE)
		# ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
		# self.stroke_shapes(ctx, 0, 6 * SIZE)
		# ctx.set_line_join(cairo.LINE_JOIN_MITER)
		# self.stroke_shapes(ctx, 0, 9 * SIZE)
		# self.fill_shapes(ctx, 0, 12 * SIZE)
		# ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
		# self.fill_shapes(ctx, 0, 15 * SIZE)
		# ctx.set_source_rgb(1, 0, 0)
		# self.stroke_shapes(ctx, 0, 15 * SIZE)
		# arr1 = Gtk.Arrow(Gtk.ARROW_UP, Gtk.SHADOW_NONE)
		# self.add(arr1)
		
# class ButtonWindow(Gtk.Window):
# 	def __init__(self):
# 		super().__init__(title="Button Demo")
# 		self.set_border_width(10)

# 		hbox = Gtk.Box(spacing=6)
# 		self.add(hbox)
		
		

# 		button = Gtk.Button.new_with_label("Click Me")
# 		button.connect("clicked", self.on_click_me_clicked)
# 		hbox.pack_start(button, True, True, 0)

# 		button = Gtk.Button.new_with_mnemonic("_Open")
# 		button.connect("clicked", self.on_open_clicked)
# 		hbox.pack_start(button, True, True, 0)

# 		button = Gtk.Button.new_with_mnemonic("_Close")
# 		button.connect("clicked", self.on_close_clicked)
# 		hbox.pack_start(button, True, True, 0)

# 	def on_click_me_clicked(self, button):
# 		print('"Click me" button was clicked')

# 	def on_open_clicked(self, button):
# 		print('"Open" button was clicked')

# 	def on_close_clicked(self, button):
# 		print("Closing application")
# 		Gtk.main_quit()

class Application(Gtk.Application):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, application_id="org.example.myapp",**kwargs)
		self.window = None
		
	def do_activate(self):
		if not self.window:
			self.window = AppWindow(application=self, title="Drawing Areas")
			
			# win.show_all()
			self.window.show_all()
			self.window.present()


if __name__ == "__main__":
	app = Application()
	app.run(sys.argv)