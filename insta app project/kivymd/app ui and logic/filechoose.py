# from kivymd.app import MDApp
# from kivy.lang import Builder
# from plyer import filechooser
# import android

# from android.storage import app_storage_path
# settings_path = app_storage_path()

# from android.storage import primary_external_storage_path
# primary_ext_storage = primary_external_storage_path()

# from android.storage import secondary_external_storage_path
# secondary_ext_storage = secondary_external_storage_path()

# choose_helper = '''
# MDFloatLayout:
#     Image:
#         id:img

#     MDLabel:
#         id:selected_path
#         text:""
#         halign:"center"
#         pos_hint:{'center_x': 0.5, 'center_y': 0.4}

#     MDRectangleFlatButton:
#         text:"Upload"
#         halign:"center"
#         pos_hint:{'center_x': 0.5, 'center_y': 0.5}
#         on_release:
#             app.file_chooser()

# '''




# class ChooseImgApp(MDApp):
#     def build(self):
#         screen = Builder.load_string(choose_helper)
#         return screen

#     def file_chooser(self):
#         filechooser.open_file(on_selection=self.selected)

#     def selected(self, selection):
#         # print(selection)
#         if selection:
#             self.root.ids.selected_path.text=selection[0]
#             # self.root.ids.img.source = selection[0]



# ChooseImgApp().run()
