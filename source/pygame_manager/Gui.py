from source.pygame_manager.Screen import Screen
from source.pygame_manager.Element import Element
from source.pygame_manager.Animation import Animation
from source.pygame_manager.Cursor import Cursor
from source.pygame_manager.EventHandler import EventHandler

class Gui(Screen, Element, Animation, Cursor, EventHandler):
    def __init__(self):
        Screen.__init__(self)
        EventHandler.__init__(self)
        Element.__init__(self)
        Animation.__init__(self)
        Cursor.__init__(self)
