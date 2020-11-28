from prompt_toolkit.shortcuts import message_dialog


def main(session):
    message_dialog(
    title='Example dialog window',
    text='Do you want to continue?\nPress ENTER to quit.').run()