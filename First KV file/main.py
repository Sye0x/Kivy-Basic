import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class mygrid(GridLayout):
    name=ObjectProperty(None)
    age=ObjectProperty(None)
    def press(self):
        name=self.name.text
        age=self.age.text
        print(f'Hello, {name}, you are {age} years old')
        
        self.name.text=""
        self.age.text=""

class myapp(App):
    def build(self):
        return mygrid()
    
if __name__=='__main__':
    myapp().run()