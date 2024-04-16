from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class CustomStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        x=0.05
        for i in range(1,11):
            b=Button(text=str(i), size_hint=(x,x))
            self.add_widget(b)
            x=x+0.05

class CustomAnchorLayout(AnchorLayout):
    pass

class CustomGridLayout(GridLayout):
    pass

class CustomBoxLayout(BoxLayout):
  pass
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
