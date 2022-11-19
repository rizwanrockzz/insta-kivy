from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (350, 600)


kv = """
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "assets//logo.jpg"
        pos_hint: {"y": .25}
    MDLabel:
        text: "Log In"
        pos_hint: {"center_x": .5, "center_y": .5}
        halign: "center"
        font_name: "BPoppins"
        font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 60/255, 43/255, 117/255, 1
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x": .5, "center_y": .38}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            hint_text: "Email"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            font_name: "Poppins"
            font_size: "18sp"
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x": .5, "center_y": .28}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            hint_text: "Password"
            password: True
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            font_name: "Poppins"
            font_size: "18sp"
    MDTextButton:
        text: "Forget your password?"
        font_name: "Poppins"
        theme_text_color: "Custom"
        text_color: 246/255, 135/255, 177/255, 1
        pos_hint: {"center_x": .5, "center_y": .21}
    Button:
        text: "LOGIN"
        font_name: "BPoppins"
        font_size: "20sp"
        size_hint: .5, .08
        pos_hint: {"center_x": .5, "center_y": .12}
        background_color: 0, 0, 0, 0
        canvas.before:
            Color: 
                rgb: 246/255, 135/255, 177/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [23]
"""


class LoginPage(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="Your Font Path\\Poppins-Regular.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Your Font Path \\Poppins-SemiBold.ttf")
    LoginPage().run()