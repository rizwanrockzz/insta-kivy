from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser

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
            app.file_chooser()

'''

    


class ChooseImgApp(MDApp):
    def build(self):
        screen = Builder.load_string(choose_helper)
        return screen

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        # print(selection)
        if selection:
            self.root.ids.selected_path.text=selection[0]
            image = selection[0].split(".")
            print(image)
            imag_name=image[0]+"."+image[1]
            if image[1]=="jpg" or image[1]=="jpeg":
                print("Can be uploaded without conversion")
                print(imag_name)
            else:
                print("Should be converted before uploading")
                print(imag_name)


            # self.root.ids.img.source = selection[0]


ChooseImgApp().run()
