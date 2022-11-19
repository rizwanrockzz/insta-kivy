from itertools import tee
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class InstaGrid(GridLayout):
    def __init__(self, **kwargs):
        super(InstaGrid, self).__init__()

        self.cols = 2

        self.add_widget(Label(text="Insta Username : "))
        self.insta_username = TextInput(multiline=False)
        self.add_widget(self.insta_username)

        self.add_widget(Label(text="Enter insta password : "))
        self.insta_pass = TextInput()
        self.add_widget(self.insta_pass)

        self.press = Button(text="Download DP")
        self.press.bind(on_press=self.DP_click)
        self.add_widget(self.press)

    def DP_click(self,instance):
        print("Your entered DP is downloaded Succesfully")
        print("Username entered is : {}".format(self.insta_username.text))
        print("Password entered is : {}".format(self.insta_pass.text))


class InstaApp(App):
    def build(self):
        return InstaGrid()


if __name__ == "__main__":
    InstaApp().run()
