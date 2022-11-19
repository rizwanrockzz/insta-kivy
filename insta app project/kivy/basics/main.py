from itertools import count
import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


# class WidgetsExample(GridLayout):
#     count = 0
#     myTxt = StringProperty("Hii rizwan!!")
#     def buttonClicked(self):
#         # global count
#         # print(count)
#         # print("Hii button is clicked")
#         # self.myTxt = "Hi changing text"
#         self.count += 1
#         self.myTxt = str(self.count)


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text="Button A")
    #     b2 = Button(text="Button B")
    #     b3 = Button(text="Button C")
    #     b4 = Button(text="Button D")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    #     self.add_widget(b4)


class MainWidget(Widget):
    pass


class Insta(App):
    pass
    # def build(self):
    #     return BoxLayoutExample()


Insta().run()
