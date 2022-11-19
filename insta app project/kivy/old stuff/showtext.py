import kivy
from kivy.app import App
from kivy.uix.label import Label 

class InstaApp(App):

    def build(self):
        return Label(text="Hii building insta app with  Kivy..")

if __name__ == "__main__":
    InstaApp().run()

    