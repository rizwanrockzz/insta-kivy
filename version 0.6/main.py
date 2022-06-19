from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mainhelper import screen_helper


class MainScreen(Screen):
    pass


class DownloadScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(DownloadScreen(name='download'))
sm.add_widget(UploadScreen(name='upload'))


class ScreenApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


ScreenApp().run()
