#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk, Gdk, GLib, GtkSource

win = Gtk.Window()
win.set_default_size(420, 600)
win.set_decorated(False)

view = GtkSource.View()
view.set_cursor_visible(True)
view.set_editable(True)
view.set_can_focus(True)
view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)

buf = view.get_buffer()
buf.set_text(" ")

scroll = Gtk.ScrolledWindow()
scroll.add(view)
win.add(scroll)

icon = Gtk.StatusIcon()
from gi.repository import GdkPixbuf
size = 22
pixels = bytearray()
for y in range(size):
    for x in range(size):
        if x == 0 or y == 0 or x == size-1 or y == size-1:
            pixels.extend([80, 60, 40, 255])
        elif y == 3:
            pixels.extend([180, 50, 50, 255])
        elif y in (7, 11, 15, 19) and 3 < x < size-3:
            pixels.extend([150, 150, 180, 255])
        else:
            pixels.extend([245, 245, 220, 255])
pixbuf = GdkPixbuf.Pixbuf.new_from_data(
    bytes(pixels), GdkPixbuf.Colorspace.RGB, True, 8, size, size, size*4)
icon.set_from_pixbuf(pixbuf)
icon.set_visible(True)

is_visible = False

def position_window():
    display = Gdk.Display.get_default()
    seat = display.get_default_seat()
    pointer = seat.get_pointer()
    if pointer:
        screen, x, y = pointer.get_position()
        win.move(x - 400, 0)

def toggle(*args):
    global is_visible
    if is_visible:
        win.hide()
        is_visible = False
    else:
        position_window()
        win.show_all()
        win.present()
        view.grab_focus()
        is_visible = True

def on_focus_out(*args):
    global is_visible
    if is_visible:
        GLib.timeout_add(100, hide_check)
    return False

def hide_check():
    global is_visible
    if not win.is_active() and is_visible:
        win.hide()
        is_visible = False
    return False

def on_key(widget, event):
    ctrl = bool(event.state & Gdk.ModifierType.CONTROL_MASK)
    hw = event.hardware_keycode
    
    if event.keyval == Gdk.KEY_Escape:
        win.hide()
        global is_visible
        is_visible = False
        return True
    
    if ctrl and hw == 52:
        if buf.can_undo():
            buf.undo()
        return True
    
    if ctrl and hw == 29:
        if buf.can_redo():
            buf.redo()
        return True
    
    return False

icon.connect("activate", toggle)

def on_popup_menu(icon, button, activate_time):
    menu = Gtk.Menu()
    quit_item = Gtk.MenuItem(label="Выход")
    quit_item.connect("activate", quit_app)
    menu.append(quit_item)
    menu.show_all()
    menu.popup(None, None, None, None, button, activate_time)

def quit_app(*args):
    Gtk.main_quit()

icon.connect("popup-menu", on_popup_menu)
win.connect("focus-out-event", on_focus_out)
view.connect("key-press-event", on_key)

# Окно НЕ показываем при запуске
is_visible = False

Gtk.main()
