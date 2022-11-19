from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

screen_helper = '''
ScreenManager:
    DownloadScreen:
    UploadScreen:

<DownloadScreen>:
    name:"download"
    MDRectangleFlatButton:
        text:"Upload Screen"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:root.manager.current = 'upload'

<UploadScreen>:
    name:"upload"
    MDLabel:
        text:"Upload Screen"
        halign:"center"
    MDRectangleFlatButton:
        text:"Back"
        pos_hint:{'center_x':0.5,'center_y':0.15}
        on_press:root.manager.current = 'download'

'''


class DownloadScreen(Screen):
    pass


class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(DownloadScreen(name='download'))
sm.add_widget(UploadScreen(name='upload'))

class ScreenApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


ScreenApp().run()
