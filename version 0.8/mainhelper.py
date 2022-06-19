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

    MDRoundFlatIconButton:
        text:'Download DP'
        icon:"face-profile"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        on_press:root.manager.current = "download"

    MDRoundFlatIconButton:
        text:'Upload Image'
        icon:"image"
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
        id:username 
        hint_text:"Enter Username"
        required: True 
        helper_text:"Download DP of this username"
        helper_text_mode:"on_focus"
        icon_right:"instagram"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:"300dp"
    MDRectangleFlatIconButton:
        text:"Download"
        icon:"download"
        on_release: app.downloadingdp()
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
        id:usernamelogin
        hint_text:"Enter Username"
        required: True 
        helper_text:"Enter your instagram username"
        helper_text_mode:"on_focus"
        icon_right:"instagram"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint_x:None
        width:"300dp"
    MDTextField:
        id:password
        password:True
        hint_text:"Enter Password"
        required: True 
        helper_text:"Enter your instagram password"
        helper_text_mode:"on_focus"
        icon_right:"form-textbox-password"
        icon_right_color:"red"
        pos_hint:{'center_x': 0.5, 'center_y': 0.63}
        size_hint_x:None
        width:"300dp"
    MDTextField:
        id:postname
        hint_text:"Enter Postname"
        helper_text:"Enter the name of the post you are going to upload"
        helper_text_mode:"on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.51}
        size_hint_x:None
        width:"300dp"
    MDTextField:
        id:hashtag
        hint_text:"Enter Hashtag"
        helper_text:"Enter one or more #tag"
        helper_text_mode:"on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.39}
        size_hint_x:None
        width:"300dp"
    MDRoundFlatIconButton:
        text:'Select Image'
        icon:"image"
        required: True 
        pos_hint:{'center_x': 0.5, 'center_y': 0.25}
    MDRectangleFlatIconButton:
        text:'Upload'
        icon:"cloud-upload-outline"
        pos_hint:{'center_x': 0.5, 'center_y': 0.1}
        on_release:app.uploadingdp()
    MDIconButton:
        icon:"keyboard-backspace"
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current = 'main'

'''
