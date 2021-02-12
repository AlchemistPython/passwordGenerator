from kivy.app import App
from kivy.uix.widget import Widget

class Grid(Widget):
    pass
        
class PassGenerator(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    PassGenerator().run()
