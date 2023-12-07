from ._anvil_designer import sportsformTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

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

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    NAME = self.text_box_1.text
    AGE = int(self.text_box_2.text)
    NUMBER = int(self.text_box_3.text)
    ADDRESS = self.text_area_1.text
    PERSONAL_TRAINER = self.check_box_1.checked
    SPORT_YOU_LIKE = self.text_box_4.text
    anvil.server.call('submit',NAME=NAME,AGE=AGE,NUMBER=NUMBER,ADDRESS=ADDRESS,PERSONAL_TRAINER=PERSONAL_TRAINER,SPORT_YOU_LIKE=SPORT_YOU_LIKE)
    Notification('THANKS FOR JOINING THE ACADEMY').show()
    
