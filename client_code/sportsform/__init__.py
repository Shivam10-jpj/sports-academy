from ._anvil_designer import sportsformTemplate
from anvil import *

class sportsform(sportsformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass
