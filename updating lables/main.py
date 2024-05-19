import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file("whatever.kv")

class mygrid(Widget):
    name=ObjectProperty(None)
    age=ObjectProperty(None)
    def press(self):
        name=self.name.text
        age=self.age.text
        print(f'Hello, {name}, you are {age} years old')
        
        self.name.text=""
        self.age.text=""

class Super(App):
    def build(self):
        return mygrid()
    
if __name__=='__main__':
    Super().run()