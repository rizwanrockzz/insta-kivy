from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

list_helper = '''
Screen:
    ScrollView:
        MDList:
            id:container
           


'''

class ListApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range(20):
            t = "Item "+str(i+1)
            items = OneLineListItem(text=t)
            self.root.ids.container.add_widget(items)


ListApp().run()
