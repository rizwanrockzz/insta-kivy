from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem,OneLineAvatarListItem, MDList
from kivymd.uix.list import ImageLeftWidget,OneLineIconListItem,IconLeftWidget
from kivy.uix.scrollview import ScrollView


class ListApp(MDApp):

    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        scroll_view.add_widget(list_view)
        for i in range(100):
            icon = IconLeftWidget(icon="instagram")
            img = ImageLeftWidget(source="insta.jpeg")
            t = "Item "+str(i+1)
            item = OneLineAvatarListItem(text=t)
            item.add_widget(img)
            list_view.add_widget(item)
        screen.add_widget(scroll_view)
        return screen


ListApp().run()
