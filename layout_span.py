import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class mygrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #set colums
        self.cols=1

        #adding another grid on Top
        self.topgrid=GridLayout()
        self.topgrid.cols=2

        
        #Adding Widget
        self.topgrid.add_widget(Label(text="Name: "))
        self.name=TextInput(multiline=False)
        self.topgrid.add_widget(self.name)

        self.topgrid.add_widget(Label(text="Age: "))
        self.age=TextInput(multiline=False)
        self.topgrid.add_widget(self.age)
        
        self.add_widget(self.topgrid)


        self.submit=Button(text="Submit")
        #Binding The Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name=self.name.text
        age=self.age.text
        print(f'')
        self.add_widget(Label(text=f'Hello, {name}, you are {age} years old'))
        self.name.text=""
        self.age.text=""




class myapp(App):
    def build(self):
        return mygrid()
    
if __name__=='__main__':
    myapp().run()