from PIL import Image
import os
  
# importing the image 
im = Image.open("b.png")
print("The size of the image before conversion : ", end = "")
print(os.path.getsize("b.png"))
  
# converting to jpg
rgb_im = im.convert("RGB")
  
# exporting the image
rgb_im.save("b.jpg")
print("The size of the image after conversion : ", end = "")
print(os.path.getsize("b.jpg"))