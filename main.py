import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class mygrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class myapp(App):
    def build(self):
        return Label(text="Hello World",font_size=100)
    
if __name__=='__main__':
    myapp().run()