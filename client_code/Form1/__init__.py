from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    CGPA = int(self.text_box_2.text)
    number = int(self.text_box_3.text)
    need_friend = self.check_box_1.checked
    anvil.server.call('submit', name=name, CGPA=CGPA, number=number, need_friend=need_friend)
    Notification("Your response has been Recorded with Mohit").show()
