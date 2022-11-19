import instaloader
import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mainhelpercopy import screen_helper
# bot code
from instabot import Bot
import os
import shutil
# for file choose
from plyer import filechooser

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
        self.doesnotexists = False
        screen = Builder.load_string(screen_helper)
        return screen

    def downloadingdp(self):
        uname = self.root.get_screen('download').ids.username.text  # username
        response = requests.get("https://instagram.com/" + uname + "/")
        # try and except may be there
        # JSON Query to mahi7781/feed/: HTTP error code 560. [retrying; skip with ^C]
        if response.status_code == 404:
            print("The username doesnot exists")
            self.root.get_screen(
                'download').ids.validornot.text = f"The username \"{uname}\" doesnot exists,try again with another username"
        else:
            self.root.get_screen(
                'download').ids.validornot.text = f"The username \"{uname}\" exists,redirecting to other screen"
            print(uname)
            dp = instaloader.Instaloader()
            dp.download_profile(uname, profile_pic_only=True)
            self.root.get_screen(
                'downloadlanding').ids.labeltextchange.text = f"{uname} DP is downloaded"
            self.root.current = "downloadlanding"

    def goingback(self):
        self.root.get_screen('download').ids.validornot.text = ""
        # self.root.get_screen('download').ids.username.text = ""

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        print(selection)
        if selection:
            self.imagepath = selection[0]
            
    def clean_up(self):
        dir = "config"
        # images\2.jpg
        remove_me = self.imagepath+".REMOVE_ME"
        print("Image path from file choose : ",self.imagepath)
        # checking whether config folder exists or not
        if os.path.exists(dir):
            try:
                # removing it because in 2021 it makes problems with new uploads
                shutil.rmtree(dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        if os.path.exists(remove_me):
            # "images\2.jpg"
            src = os.path.realpath(self.imagepath)
            os.rename(remove_me, src)

    def uploadingdp(self):
        uname = self.root.get_screen('upload').ids.usernamelogin.text
        passwordinsta = self.root.get_screen('upload').ids.password.text
        postname = self.root.get_screen('upload').ids.postname.text
        hashtag = self.root.get_screen('upload').ids.hashtag.text

        bot = Bot()

        bot.login(username=uname, password=passwordinsta)
        bot.upload_photo(self.imagepath, caption=postname)

        print(uname)
        print(passwordinsta)
        print(postname)
        print(hashtag)


InstaApp().run()
