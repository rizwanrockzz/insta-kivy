from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix import button
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from uploadhelpers import username_helper
from uploadhelpers import password_helper
from uploadhelpers import postname_helper
from uploadhelpers import hashtag_helper
from kivymd.uix.label import MDLabel, MDIcon


class Upload(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text="UPLOAD DP",halign="center", pos_hint={
            'center_x': 0.5, 'center_y': 0.9}, theme_text_color="Custom", text_color=(235/255.0, 51/255.0, 73/255.0, 1), font_style="H4")
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        self.postname = Builder.load_string(postname_helper)
        self.hashtag = Builder.load_string(hashtag_helper)
        btn = MDRectangleFlatButton(text='Upload', pos_hint={
                                    'center_x': 0.5, 'center_y': 0.2}, on_release=self.showData)
        screen.add_widget(label)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(self.postname)
        screen.add_widget(self.hashtag)
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
        print(self.password.text)

    def close_dialog(self, obj):
        self.dialog.dismiss()


Upload().run()
