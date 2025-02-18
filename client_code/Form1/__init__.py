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
    pass

def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    
    try:
        CGPA = float(self.text_box_2.text)  # Convert to float first
    except ValueError:
        # Handle invalid input if it's not a valid number
        Notification("Please enter a valid CGPA").show()
        return  # Exit the function early if the input is invalid
    
    try:
        number = int(self.text_box_3.text)  # Assuming number should be an integer
    except ValueError:
        # Handle invalid input for number
        Notification("Please enter a valid number").show()
        return  # Exit the function early if the input is invalid

    need_friend = self.check_box_1.checked
    
    # Now, call the server function with the correct values
    anvil.server.call('submit', name=name, CGPA=CGPA, number=number, need_friend=need_friend)
    
    # Show confirmation notification
    Notification("Your response has been Recorded with Mohit").show()
