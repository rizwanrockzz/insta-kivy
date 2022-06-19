screen_helper = '''
ScreenManager:
    MainScreen:
    DownloadScreen:
    UploadScreen:

<MainScreen>:
    name:"main"
    MDLabel:
        text:"INSTA APP"
        halign:"center"
        theme_text_color:"Custom"
        text_color:(235/255.0, 51/255.0, 73/255.0, 1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
        font_style:"H4"

    MDRectangleFlatButton:
        text:'Download DP'
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        on_press:root.manager.current = "download"

    MDRectangleFlatButton:
        text:'Upload DP'
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        on_press:root.manager.current = "upload"


<DownloadScreen>:
    name:"download"
    MDLabel:
        text:"DOWNLOAD DP"
        halign:"center"
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
        theme_text_color:"Custom"
        text_color:(235/255.0, 51/255.0, 73/255.0, 1)
        font_style:"H4"
    MDTextField:
        hint_text:"Enter Username"
        helper_text:"Download DP of this username"
        # helper_text_mode:"persistent"
        helper_text_mode:"on_focus"
        icon_right:"instagram"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:"300dp"
    MDRectangleFlatButton:
        text:"Download"
        pos_hint:{'center_x':0.5,'center_y':0.3}


    MDIconButton:
        icon:"keyboard-backspace"
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current = 'main'


<UploadScreen>:
    name:"upload"
    MDLabel:
        text:"UPLOAD DP"
        halign:"center"
        pos_hint:{'center_x': 0.5, 'center_y': 0.9}
        theme_text_color:"Custom"
        text_color:(235/255.0, 51/255.0, 73/255.0, 1)
        font_style:"H4"
    MDTextField:
        hint_text:"Enter Username"
        helper_text:"Download DP of this username"
        # helper_text_mode:"persistent"
        helper_text_mode:"on_focus"
        icon_right:"instagram"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:"300dp"
    MDTextField:
        hint_text:"Enter Password"
        # helper_text:"Download DP of this username"
        helper_text_mode:"on_focus"
        icon_right:"password"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.58}
        size_hint_x:None
        width:"300dp"
    MDTextField:
        hint_text:"Enter Postname"
        # helper_text:"Download DP of this username"
        helper_text_mode:"on_focus"
        icon_right:"password"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.46}
        size_hint_x:None
        width:"300dp"
    MDTextField:
        hint_text:"Enter Hashtag"
        # helper_text:"Download DP of this username"
        helper_text_mode:"on_focus"
        icon_right:"password"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.34}
        size_hint_x:None
        width:"300dp"
    MDRectangleFlatButton:
        text:'Upload'
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
    MDIconButton:
        icon:"keyboard-backspace"
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current = 'main'

'''
