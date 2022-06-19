from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper = ''' 
MDTextField:
    hint_text:"Enter Username"
    helper_text:"Download DP of this username"
    # helper_text_mode:"persistent"
    helper_text_mode:"on_focus"
    icon_right:"instagram"
    icon_right_color:"red"
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:"280dp"
'''



class Download(MDApp):
    def build(self):
        screen = Screen()
        # username = MDTextField(text="Enter Insta Username",pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint_x=None,width="280dp")
        username = Builder.load_string(username_helper)
        # pa = Builder.load_string(pa_helper)
        screen.add_widget(username)
        # screen.add_widget(pa)
        return screen


Download().run()
