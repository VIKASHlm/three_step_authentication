from ._anvil_designer import Login_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login_form(Login_formTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def l_email_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in the email text box"""
        pass

    def l_password_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in the password text box"""
        pass

    def button_1_click(self, **event_args):
        """This method is called when the login button is clicked"""
        email = self.l_email.text
        password = self.l_password.text

        # Retrieve user from the database based on email
        user = app_tables.table_2.get(email=email)

        if user is not None:
            # User found, check password
            if user['ecpassword'] == password:
                # Password matches, login successful
                alert("Login successful!")
                open_form(Main_formTemplate)
            else:
                # Password doesn't match
                alert("Incorrect password. Please try again.")
        else:
            # User not found
            alert("User not found. Please check your email.")
