from instabot import Bot
import os
import shutil


def clean_up():
    dir = "config"
    remove_me = "images\1.jpg.REMOVE_ME"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it because in 2021 it makes problems with new uploads
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("images\1.jpg")
        os.rename(remove_me, src)


def upload_post():
    bot = Bot()

    bot.login(username="_rizz_13", password="@MDrizwan13")
    bot.upload_photo("images/1.jpg", caption="nice pic")


if __name__ == '__main__':
    clean_up()
    upload_post()
