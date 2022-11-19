import os 
    
# Directory name 
directory = "config"
    
# Parent Directory 
parent = "C:\Users\hp\Desktop\RIZWAN\Python\insta bot"

    
# Path 
path = os.path.join(parent, directory) 
    
# Remove the Directory 
# "Geeks" 
os.rmdir(path)