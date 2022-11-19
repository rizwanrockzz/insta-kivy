from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton,MDFloatingActionButton
from kivymd.uix.screen import Screen


class InstaApp(MDApp):
    def build(self,**kwargs):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        screen = Screen()
        btn_rect = MDRectangleFlatButton(text='Sign In', theme_text_color="Custom", text_color=(
            0, 0, 1, 1), line_color=(0, 0, 1, 1), pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_rect = MDRectangleFlatButton(text='Hello Rizwan', pos_hint={
                                         "center_x": 0.5, "center_y": 0.5})
        icon_btn = MDIconButton(icon="instagram", pos_hint={"center_x": 0.5, "center_y": 0.5})
        icon_btn_action = MDFloatingActionButton(icon="instagram", pos_hint={"center_x": 0.5, "center_y": 0.5})
        screen.add_widget(btn_rect)
        # screen.add_widget(icon_btn)
        # screen.add_widget(icon_btn_action)

        return screen


InstaApp().run()
