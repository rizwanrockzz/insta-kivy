from turtle import width
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix import button
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon


class Download(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text="INSTA APP", halign="center", pos_hint={
            'center_x': 0.5, 'center_y': 0.9}, theme_text_color="Custom", text_color=(235/255.0, 51/255.0, 73/255.0, 1), font_style="H4")
        btn1 = MDRectangleFlatButton(text='Download DP', pos_hint={
            'center_x': 0.5, 'center_y': 0.5}, on_release=self.showDataDownload)
        btn2 = MDRectangleFlatButton(text=' Uplaod DP ', pos_hint={
            'center_x': 0.5, 'center_y': 0.4}, on_release=self.showDataUpload)

        screen.add_widget(label)
        screen.add_widget(btn1)
        screen.add_widget(btn2)
        return screen

    def showDataDownload(self, obj):
        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title="Selected Option",
                               text="Downloading DP...", size_hint_x="0.9", buttons=[close_btn])
        self.dialog.open()

    def showDataUpload(self, obj):
        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title="Selected Option",
                               text="Uploading DP...", size_hint_x="0.9", buttons=[close_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


Download().run()
