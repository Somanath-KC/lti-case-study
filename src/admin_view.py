from .auth_view import auth
from prompt_toolkit.shortcuts import message_dialog

def main(session):
    """
        Entry Point for admin view.
    """

    # Authenticate admin user
    while True:
        if auth(session, is_admin=True):
            break
        else:    
            message_dialog(
                title='Authentication Failed',
                text='Invalid Username/Password. Press ENTER to try again.').run()


    message_dialog(
    title='Example dialog window',
    text='Do you want to continue?\nPress ENTER to quit.').run()