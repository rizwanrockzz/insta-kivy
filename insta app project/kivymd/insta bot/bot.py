from instabot import Bot
from PIL import Image

im = Image.open("c.png")
rgb_im = im.convert("RGB")
rgb_im.save("c.jpg")

bot = Bot()
bot.login(username="_rizz_13", password="@MDrizwan13")
bot.upload_photo("c.jpg", caption="Nice pic!")



