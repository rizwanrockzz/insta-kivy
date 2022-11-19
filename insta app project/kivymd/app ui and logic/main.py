import instaloader
import lzma
# import urllib3,charset_normalizer,chardet,idna
import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mainhelper import screen_helper


class MainScreen(Screen):
    pass


class DownloadScreen(Screen):
    pass


class DownloadLandingScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class UploadLandingScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(DownloadScreen(name='download'))
sm.add_widget(DownloadLandingScreen(name='downloadlanding'))
sm.add_widget(UploadScreen(name='upload'))


class InstaApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def downloadingdp(self):
        uname = self.root.get_screen('download').ids.username.text  # username
        response = requests.get("https://instagram.com/" + uname + "/")
        if response.status_code == 404:
            print(f"The username {uname} doesnot exists")
            self.root.get_screen('download').ids.validornot.text = f"The username \"{uname}\" doesnot exists,try again with another username"
        else:
            self.root.get_screen('download').ids.validornot.text = f"The username \"{uname}\" exists, redirecting to other screen"
            print(uname)
            dp = instaloader.Instaloader()
            dp.download_profile(uname, profile_pic_only=True)
            self.root.get_screen(
                'downloadlanding').ids.labeltextchange.text = f"{uname} DP is downloaded"
            self.root.current = "downloadlanding"

    def uploadingdp(self):
        uname = self.root.get_screen('upload').ids.usernamelogin.text
        password = self.root.get_screen('upload').ids.password.text
        postname = self.root.get_screen('upload').ids.postname.text
        hashtag = self.root.get_screen('upload').ids.hashtag.text

        print(uname)
        print(password)
        print(postname)
        print(hashtag)


InstaApp().run()
