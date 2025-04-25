### main.py
from textual.app import App
from textual.widgets import Header, Footer, Static, Label

class TimeManagerApp(App):
    def compose(self):
        yield Header()
        yield Static("Welcome to Terminal Time Manager!", id="main-message")
        yield Footer()
        yield Label("This is a simple time management application.", id="info-label")

if __name__ == "__main__":
    TimeManagerApp().run()

