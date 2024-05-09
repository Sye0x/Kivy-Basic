import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class mygrid(GridLayout):
    
    def press(self,instance):
        name=self.name.text
        age=self.age.text
        print(f'')
        self.add_widget(Label(text=f'Hello, {name}, you are {age} years old',
                              font_size=12,
                           size_hint_y=None,
                           height=50,
                           ))
        self.name.text=""
        self.age.text=""

class myapp(App):
    def build(self):
        return mygrid()
    
if __name__=='__main__':
    myapp().run()