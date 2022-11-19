username_helper = ''' 
MDTextField:
    hint_text:"Enter Username"
    helper_text:"Download DP of this username"
    # helper_text_mode:"persistent"
    helper_text_mode:"on_focus"
    icon_right:"instagram"
    icon_right_color:"red"
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width:"300dp"
'''

password_helper = ''' 
MDTextField:
    hint_text:"Enter Password"
    # helper_text:"Download DP of this username"
    helper_text_mode:"on_focus"
    icon_right:"password"
    icon_right_color:"red"
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:"300dp"
'''