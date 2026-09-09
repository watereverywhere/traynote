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
icon.set_from_icon_name("accessories-text-editor")
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
win.connect("focus-out-event", on_focus_out)
view.connect("key-press-event", on_key)

# Окно НЕ показываем при запуске
is_visible = False

Gtk.main()
