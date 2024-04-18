from ._anvil_designer import Signup_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Signup_form(Signup_formTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def email_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in the email text box"""
        pass

    def password_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in the password text box"""
        pass

    def button_1_click(self, **event_args):
        """This method is called when the signup button is clicked"""
        email = self.email.text
        password = self.password.text
        confirm_password = self.c_password.text

        # Check if passwords match
        if password != confirm_password:
            # Display an error message
            alert("Passwords do not match. Please try again.")
        else:
          
                app_tables.table_2.add_row(email=email, ecpassword=password)
                # Display success message
                alert("Signup successful!")
          
               
 