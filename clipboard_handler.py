import pyperclip

class ClipboardHandler:
    def copy(self, content):
        pyperclip.copy(content)

    def paste(self):
        return pyperclip.paste()
