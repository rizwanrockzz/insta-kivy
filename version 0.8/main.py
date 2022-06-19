import instaloader
#:import hex kivy.utils.get_color_from_hex

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


class InstaApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def downloadingdp(self):
        uname = self.root.get_screen('download').ids.username.text  # username

        if uname != str(''):
            try:
                print(uname)
                dp = instaloader.Instaloader()
                dp.download_profile(uname, profile_pic_only=True)
            except:
                print("Insta App not responding")
                print("There is an error occured you might have given a wrong username")

        else:
            print('Please,Enter a username to proceed')

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
