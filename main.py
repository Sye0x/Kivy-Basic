from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CustomBoxLayout(BoxLayout):
  """  def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="1")
        b2 = Button(text="2")
        
        self.add_widget(b1)
        self.add_widget(b2)"""

class MainWidget(Widget):
    pass

class TheLab(App):
    pass

TheLab().run()
