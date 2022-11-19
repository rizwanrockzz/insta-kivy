from kivymd.app import MDApp
from kivy.lang import Builder
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

choose_helper = '''
MDFloatLayout:
    Image:
        id:img

    MDLabel:
        id:selected_path
        text:""
        halign:"center"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}

    MDRectangleFlatButton:
        text:"Upload"
        halign:"center"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        on_release:
            app.chooser()
'''




class ChooseImgApp(MDApp):
    def build(self):
        screen = Builder.load_string(choose_helper)
        return screen

    def chooser(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        self.root.ids.selected_path.text=filename
        print(filename)


ChooseImgApp().run()
