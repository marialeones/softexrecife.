from typing import List

class TextEditor():
    def __init__(self):
        super().__init__()
        self.lines = []

    def insertLine(self, lineNumber: int, text: str):
        if lineNumber <= len(self.lines):
            self.lines.insert(lineNumber, text)
        else:
            self.lines.append(text)
        self.notifyObservers()

    def removeLine(self, lineNumber: int):
        if lineNumber < len(self.lines):
            self.lines.pop(lineNumber)
            self.notifyObservers()

class User:
    def __init__(self):
        self.textEditor = TextEditor()
        self.textEditor.attach(self)

    def update(self):
        print("\n".join(self.textEditor.lines))

    def run(self):
        self.textEditor.notify('open')
        while True:
            text = input("Digite uma linha de texto ou EOF para sair: ")
            if text == "EOF":
                break
            self.textEditor.insertLine(len(self.textEditor.lines), text)
        self.textEditor.notify('save')

