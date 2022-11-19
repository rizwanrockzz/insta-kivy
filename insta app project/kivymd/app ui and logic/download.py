import instaloader
from logging import disable
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix import button
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper
from helpers import password_helper
from kivymd.uix.label import MDLabel, MDIcon



class Download(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text="DOWNLOAD DP",halign="center", pos_hint={
            'center_x': 0.5, 'center_y': 0.9}, theme_text_color="Custom", text_color=(235/255.0, 51/255.0, 73/255.0, 1), font_style="H4")
        self.username = Builder.load_string(username_helper)
        # self.password = Builder.load_string(password_helper)
        btn = MDRectangleFlatButton(text='Download', pos_hint={
                                    'center_x': 0.5, 'center_y': 0.3}, on_release=self.showData)
        screen.add_widget(label)
        screen.add_widget(self.username)
        # screen.add_widget(self.password)
        screen.add_widget(btn)
        # screen.add_widget(pa)
        return screen

    def showData(self, obj):
        if self.username.text is "":
            dialog_output = "Please enter a username"
        else:
            dialog_output = f'Hii ,{self.username.text}!!'
        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_btn = MDFlatButton(text='More')
        self.dialog = MDDialog(title="Greetings from Rizwan",
                               text=dialog_output, size_hint_x="0.9", buttons=[more_btn, close_btn])
        self.dialog.open()
        print(self.username.text)
        # print(self.password.text)
        
        dp = instaloader.Instaloader()
        # username = input("Enter username : ")
        dp.download_profile(self.username.text,profile_pic_only=True)



    def close_dialog(self, obj):
        self.dialog.dismiss()


Download().run()
