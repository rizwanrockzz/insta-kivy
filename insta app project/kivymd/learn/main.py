# import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon


class InstaApp(MDApp):
    def build(self):
        label = MDLabel(text="Hello Rizwan!!", halign="center",theme_text_color="Custom",text_color=(235/255.0,51/255.0,73/255.0,1),font_style="Button")
        icon = MDIcon(icon="instagram", halign="center")
        return label
# ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon']

InstaApp().run()
