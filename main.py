import json
import webbrowser
from kivy.utils import platform
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, ScreenManager


KV = """
#import akivymd library

#: import akivymd kivymd_extensions.akivymd

ScreenManager:
    ProfileScreen:
    Screen_1:
    Screen_2:
    Screen_3:
    Screen_4:
    Blank:
    Maths:
    About_Us:
    videolectures:
    screen0:
    BottomNavigation:
    screen1:
    screen2:
    screen3:
    screen4:
    screen5:
    LoginScreen:
    profilepage:


<ProfileScreen>:
    name:"profile"
    name_input: name_input
    email_input: email_input
    year_input: year_input


    MDScreen:
        md_bg_color:[0.403921568627451, 0.2, 0.9882352941176471, 0.9]
        MDCard:

            orientation: 'vertical'
            size_hint: None, None
            size: "260dp", "350dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 1
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                height: dp(200)

                MDFloatLayout:

                    MDIconButton:
                        icon_size:"100sp"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        user_font_size: "128sp"
                        pos_hint: {"center_x": 0.5, "center_y": .7}
                        canvas:
                            Color:
                                rgba: 0,0,0,0
                            Ellipse:
                                pos: self.pos
                                size: self.size
                        icon: "account-circle"

                    MDLabel:
                        text: "SIGN-UP"      
                        font_style: 'Subtitle1' 
                        pos_hint: {"center_x": 0.89, "center_y": .3}

                MDTextField:
                    id: name_input
                    hint_text: "Name"
                    size_hint_y: None
                    height: dp(48)

                MDTextField:
                    id: email_input
                    hint_text: "Email"
                    size_hint_y: None
                    height: dp(48)

                MDTextField:
                    id: year_input
                    hint_text:"Persuing Year"
                    size_hint_y: None
                    height: dp(48)


                MDRaisedButton:
                    text: "Continue"
                    pos_hint: {"center_x": 0.5, "center_y": .7}
                    on_release: root.save_profile_details()


<profilepage>:
    name:"page"
    md_bg_color:[0.403921568627451, 0.2, 0.9882352941176471, 0.9]
    MDScreen:

        MDIconButton:
            icon_size:"100sp"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            user_font_size: "128sp"
            pos_hint: {"center_x": 0.5, "center_y": .9}
            canvas:
                Color:
                    rgba: 0,0,0,0
                Ellipse:
                    pos: self.pos
                    size: self.size
            icon: "account-circle"

        MDLabel:
            text:"PROFILE DETAILS"
            font:"Subtitle2"
            pos_hint: {"center_x": 0.8, "center_y": .8}

        MDCard:  
            md_bg_color:[0.403921568627451, 0.2, 0.9882352941176471, 0.9]  
            orientation: 'vertical'
            size_hint: None, None
            size: "260dp", "300dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.48}
            elevation: 1
            MDFloatLayout:
                MDLabel:
                    id:name_label
                    font:"H4"
                    pos_hint: {"center_x": 0.5, "center_y": .8}
                    font_size:"20sp"

                MDLabel:
                    id:email_label
                    font:"subtitle1"
                    pos_hint: {"center_x": 0.5, "center_y": .6}
                    font_size:"20sp"

                MDLabel:
                    id:year_label
                    font:"subtitle2"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    font_size:"20sp"

                MDFillRoundFlatIconButton:
                    text:"Edit Details"
                    icon:"pen"
                    pos_hint: {"center_x": .5, "center_y": .2}

        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="one"
            
        BottomNavigation:

<Screen_1>:

    name:"one"
    name_label: name_label
    FloatLayout:
        MDLabel:
            id: name_label  
            font_style: 'H4'
            pos_hint: {"center_x": 0.5, "center_y": .8}
            height: dp(48)

        MDLabel:
            text:"Welcome to Backlog Wallah!"
            pos_hint: {"center_x": 0.6, "center_y": .7}
            font_style:"Subtitle1"
            font_size:"20sp"

        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.5}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFloatingActionButton:
            icon: "arrow-right"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": 0.8, "center_y": 0.3}
            on_press:root.manager.current="five"

        BottomNavigation:


        MDBoxLayout:
            orientation:"vertical"
            spacing:"20dp"

            MDTopAppBar:  
                title :"HOME" 
                left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                md_bg_color:"#00B9F1"
                elevation:0
            Widget:




        MDNavigationDrawer:
            width: root.width - dp(80)
            id:nav_drawer
            MDNavigationDrawerMenu:


                MDNavigationDrawerHeader:
                    title:"Backlog Wallah!"   
                    spacing:10
                    padding:12,0,0,56

                MDNavigationDrawerItem:
                    icon:"account"
                    text:"Profile"
                    icon_color:(0,0,0,.9)

                    focus_color:"#00B9F1"
                    on_press:root.manager.current="page"

                MDNavigationDrawerItem:
                    icon:'theme-light-dark'
                    text:"Light - Dark "
                    icon_color:(0,0,0,.9)
                    focus_color:"#00B9F1"

                MDNavigationDrawerItem:
                    icon:'logout'
                    text:"Logout"
                    icon_color:(0,0,0,.9)

                    focus_color:"#00B9F1"
                    on_release: app.logout()


                MDNavigationDrawerDivider:
                    color:(0, 0, 0, 1)

                MDNavigationDrawerItem:
                    text:"Support"
                    icon:'headset'
                    icon_color:(0,0,0,.9)


                    focus_color:"#00B9F1"

                MDNavigationDrawerItem:
                    text:"Suggestions"
                    icon:'lightbulb-outline'
                    icon_color:(0,0,0,.9)

                    focus_color:"#00B9F1"

                MDNavigationDrawerItem:
                    icon:'information'
                    icon_color:(0,0,0,.9)

                    focus_color:"#00B9F1"

                    text:"About Us "

                    on_press:root.manager.current="about"




<BottomNavigation>:
    BoxLayout:
        orientation: "vertical"

        AKBottomNavigation:
            id: bottom_navigation
            size_hint_y: None
            height: dp(20)
            items: root.bottom_navigation_items


<Screen_2>:
    name:"two"
    FloatLayout:

        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text:"Choose Year"
            icon: "star"
            icon_size:"18sp" 

            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDFillRoundFlatIconButton:
            text: "I-YEAR"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.2, "center_y": 0.5}
            on_press:root.manager.current="three"


        MDFillRoundFlatIconButton:
            text: "II-YEAR"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.5}
            on_press:root.manager.current="none"

        MDFillRoundFlatIconButton:
            text: "III-YEAR"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.2, "center_y": 0.28}
            on_press:root.manager.current="none"

        MDFillRoundFlatIconButton:
            text: "IV-year"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.28}
            on_press:root.manager.current="none"

        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="five"

        BottomNavigation:



<Screen_3>:
    name:"three"
    FloatLayout:    

        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text:"Choose Semester"
            icon: "star"
            icon_size:"18sp"  
            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDFillRoundFlatIconButton:
            text: "I-semester"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.2, "center_y": 0.5}
            on_press:root.manager.current="four"

        MDFillRoundFlatIconButton:
            text: "II-semester"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.5}
            on_press:root.manager.current="none"


        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="two"
        BottomNavigation:


<Screen_4>:
    name:"four"
    FloatLayout:  
        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text:"Choose Subject"
            icon: "star"
            icon_size:"18sp"  
            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDFillRoundFlatIconButton:
            text: "ENGLISH"
            icon:"book"    
            icon_size:"20sp"
            pos_hint: {"center_x": 0.2, "center_y": 0.5}


        MDFillRoundFlatIconButton:
            text: "PYTHON"
            icon:"language-python"
            icon_size:"20sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.5}


        MDFillRoundFlatIconButton:
            text: "CAEG"
            icon:"draw"
            icon_size:"25sp" 
            pos_hint: {"center_x": 0.2, "center_y": 0.34}

        MDFillRoundFlatIconButton:
            text: "MATHS"
            icon: "math-integral-box"
            icon_size:"25sp" 
            pos_hint: {"center_x": 0.8, "center_y": 0.34}
            on_press:root.manager.current="p"


        MDFillRoundFlatIconButton:
            text: "FIMS"
            icon:"finance"
            icon_size:"25sp" 
            pos_hint: {"center_x": 0.2, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text: "FRENCH"
            icon:"images/bonjour.png"
            icon_size:"20sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.2}


        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="three"
        BottomNavigation:

<Blank>:
    name:"none"
    FloatLayout:  
        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"
            text_hue:"100"
            font_style:"Subtitle1"
            font_size:"10sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDLabel:
            text:"We Will Develop In Further Version's"
            font_style:"Caption"
            font_size:"19sp"
            pos_hint: {"center_x": 0.5, "center_y": .5} 

        MDIcon:       
            icon: "heart"
            halign: "center"
            theme_text_color: "Custom"
            text_color: (1, 0, 0, 1)
            pos_hint: {"center_x": 0.5, "center_y": .4} 

        MDLabel:
            text:"Made with        by team BW"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.65, "center_y": .4} 

        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="one"
        BottomNavigation:




<About_Us>:
    name:"about"
    FloatLayout:  
        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}


        MDLabel:
            text:"\\nWe The Students from AIML Department of Class EPSILON Developed An  App for helping MRU espicially AIML Epsilon students to clear their backlogs \\n\\nDEVELOPED BY \\n\\nRAJU-CODING & UI DESIGN \\nMANIKANTA & NIKHIL-LOGO \\nSRAVANI & SIRI-Collecting of Sources"
            font_style:"Subtitle2"

        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="one"
        BottomNavigation:

<Maths>:
    name:"p"
    FloatLayout:  
        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text:"  PYTHON"
            icon: "star"
            icon_size:"18sp" 
            pos_hint: {"center_x": 0.5, "center_y": 0.8}


        MDFillRoundFlatIconButton:
            text: "SYLLABUS"
            icon:"book"    
            icon_size:"20sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.65}


        MDFillRoundFlatIconButton:
            text: "VIDEO LECTURES"
            icon:"play"
            icon_size:"20sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
            on_press:root.manager.current="v1"

        MDFillRoundFlatIconButton:
            text: "PDF'S"
            icon:"draw"
            icon_size:"25sp" 
            pos_hint: {"center_x": 0.5, "center_y": 0.45}

        MDFillRoundFlatIconButton:
            text: "MOCK QUESTION PAPER"
            icon: "math-integral-box"
            icon_size:"25sp" 
            pos_hint: {"center_x": 0.5, "center_y": 0.35}


        MDFillRoundFlatIconButton:
            text: "IMPORTANT NOTES &QA"
            icon:"finance"
            icon_size:"25sp" 
            pos_hint: {"center_x": 0.5, "center_y": 0.25}




        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="four"

        BottomNavigation:   

<videolectures>:

    name:"v1"
    FloatLayout:  
        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text:"  Choose Chapter"
            icon: "star"
            icon_size:"18sp" 
            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDFillRoundFlatIconButton:
            text:"Chapter-1"
            icon: "play"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            on_press:root.manager.current="01"

        MDFillRoundFlatIconButton:
            text: "Chapter-2"
            icon:"play"
            icon_size:"18sp"  
            pos_hint: {"center_x": 0.2, "center_y": 0.5}
            on_press:root.manager.current="02"


        MDFillRoundFlatIconButton:
            text: "Chapter-3"
            icon:"play"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.5}
            on_press:root.manager.current="03"

        MDFillRoundFlatIconButton:
            text: "chapter-4"
            icon:"play"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.2, "center_y": 0.28}
            on_press:root.manager.current="04"


        MDFillRoundFlatIconButton:
            text: "chapter-5"
            icon:"play"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.28}
            on_press:root.manager.current="05"

        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="p"
        BottomNavigation:    

<screen0>:
    name:"01"
    FloatLayout:  
        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.2, "center_y": 0.2}


        MDBoxLayout:
            orientation:"vertical"
            spacing:"20dp"

            MDTopAppBar: 
                id:"topb "
                title:"MATRICES"
                left_action_items: [["arrow-left", lambda x: app.go_screen()]]
                md_bg_color:"#00B9F1"
                elevation:0
            Widget:

        MDFillRoundFlatIconButton:
            icon:"play"
            text: "UNIT-1(Entire Topics)"
            on_release: app.play_video("https://youtube.com/playlist?list=PLeIE3weEKo4bfOsGyBN3BBGco-ESAfl0x")
            pos_hint: {"center_x": 0.5, "center_y": 0.5}



        BottomNavigation:

<screen1>:
    name:"02"
    FloatLayout:  
        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.2, "center_y": 0.2}


        MDBoxLayout:
            orientation:"vertical"
            spacing:"20dp"

            MDTopAppBar: 
                id:"topb "
                title:"Eigen Values and Vectors"
                md_font_size:"Title"
                left_action_items: [["arrow-left", lambda x: app.go_screen()]]
                md_bg_color:"#00B9F1"
                elevation:0
            Widget:

        MDFillRoundFlatIconButton:
            icon:"play"
            text: "UNIT-2(Entire Topics)"
            on_release: app.play_video("https://youtube.com/playlist?list=PLeIE3weEKo4aYkfAEvyjc-2RsLznwPvxz")
            pos_hint: {"center_x": 0.5, "center_y": 0.5}



        BottomNavigation:

<screen2>:
    name:"03"
    FloatLayout:  
        Image:
            source:"images/bg.png"
            allow_stretch:True
            keep_ratio:True
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:True
            keep_ratio:True
            pos_hint: {"center_x": 0.2, "center_y": 0.2}


        MDBoxLayout:
            orientation:"vertical"
            spacing:"20dp"

            MDTopAppBar: 
                id:"topb "
                title:"1st order differential"
                left_action_items: [["arrow-left", lambda x: app.go_screen()]]
                md_bg_color:"#00B9F1"
                elevation:0
            Widget:

        MDFillRoundFlatIconButton:
            icon:"play"
            text: "UNIT-3"
            on_release: app.play_video("https://www.youtube.com/playlist?list=PLeIE3weEKo4ZlAMFDEJQj9Yv9MnM1DuYQ")
            pos_hint: {"center_x": 0.5, "center_y": 0.5}



    BottomNavigation:


<screen3>:
    name:"04"
    FloatLayout:  
        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.2, "center_y": 0.2}


        MDBoxLayout:
            orientation:"vertical"
            spacing:"20dp"

            MDTopAppBar: 
                id:"topb "
                title:"High Order Differential"
                left_action_items: [["arrow-left", lambda x: app.go_screen()]]
                md_bg_color:"#00B9F1"
                elevation:0
            Widget:

        MDFillRoundFlatIconButton:
            icon:"play"
            text: "UNIT-4(Entire Topics)"
            on_release: app.play_video("https://youtube.com/playlist?list=PLeIE3weEKo4abjzVPTY4YLJiryeggUsOI")
            pos_hint: {"center_x": 0.5, "center_y": 0.5}



        BottomNavigation:


<screen4>:
    name:"05"
    FloatLayout:  
        Image:
            source:"images/bg.png"
            allow_stretch:True
            keep_ratio:True
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:True
            keep_ratio:True
            pos_hint: {"center_x": 0.2, "center_y": 0.2}


        MDBoxLayout:
            orientation:"vertical"
            spacing:"20dp"

            MDTopAppBar: 

                title:"LAPLACE TRANSFORMATIONS"
                anchor_title:"left"
                left_action_items: [["arrow-left", lambda x: app.go_screen()]]
                md_bg_color:"#00B9F1"
                elevation:0
            Widget:

        MDFillRoundFlatIconButton:
            icon:"play"
            text: "UNIT-5(Entire Topics)"
            on_release: app.play_video("https://youtube.com/playlist?list=PLeIE3weEKo4aeVzoSy6tHtojw1wNpSPMD")
            pos_hint: {"center_x": 0.5, "center_y": 0.5}



        BottomNavigation:



<screen5>:
    name:"five"
    FloatLayout:  
        MDLabel:
            text:"BacklogWallah!"
            font_style:"Subtitle1"
            font_size:"19sp"
            pos_hint: {"center_x": 0.83, "center_y": .95}

        MDLabel:
            text:"Get back on track with ease"

            font_style:"Subtitle1"
            font_size:"9sp"
            pos_hint: {"center_x": 1, "center_y": .92}


        Image:
            source:"images/bg.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.9, "center_y": 0.6}

        Image:
            source:"images/1.png"
            allow_stretch:False
            keep_ratio:False
            pos_hint: {"center_x": 0.1, "center_y": 0.2}

        MDFillRoundFlatIconButton:
            text:"Choose Academic Year"
            icon: "star"
            icon_size:"18sp" 
            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDFillRoundFlatIconButton:
            text: "2022-23"
            icon:"arrange-send-to-back"
            icon_size:"18sp"  
            pos_hint: {"center_x": 0.2, "center_y": 0.5}
            on_press:root.manager.current="two"

        MDFillRoundFlatIconButton:
            text: "2023-24"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.5}
            on_press:root.manager.current="none"

        MDFillRoundFlatIconButton:
            text: "2024-25"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.2, "center_y": 0.28}
            on_press:root.manager.current="none"


        MDFillRoundFlatIconButton:
            text: "2025-26"
            icon:"arrange-send-to-back"
            icon_size:"18sp"
            pos_hint: {"center_x": 0.8, "center_y": 0.28}
            on_press:root.manager.current="none"

        MDIconButton:
            icon:"arrow-left-bold-circle-outline"
            icon_size:"30sp"
            pos_hint: {"center_x": 0.1, "center_y": 0.95}
            on_press:root.manager.current="one"

        BottomNavigation:


"""

import re


# Define the screens
class ProfileScreen(Screen):

    def save_profile_details(self):
        name = self.name_input.text
        email = self.email_input.text
        year = self.year_input.text

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_error_message("Invalid email format")
            return

        # Validate name format
        if re.search("[^a-zA-Z\s]", name):
            self.show_error_message("Invalid name format")
            return

        # Save the profile details in a dictionary
        profile_details = {
            'name': name,
            'email': email,
            'year': year,

        }

        # Save the profile details to a JSON file
        with open('profile_details.json', 'w') as file:
            json.dump(profile_details, file)

        # Navigate to the next screen
        self.manager.current = 'one'
        next_screen = self.manager.get_screen('one')
        next_screen.display_profile_details(profile_details)

        # Clear the input fields
        self.name_input.text = ''
        self.email_input.text = ''
        self.year_input.text = ''

    def show_error_message(self, message):
        # Display an error message
        error_dialog = MDDialog(
            title="Error",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: error_dialog.dismiss()
                )
            ]
        )
        error_dialog.open()


class Screen_1(Screen):
    def display_profile_details(self, profile_details):
        name = profile_details['name']
        self.name_label.text = f"Hi, {name}"

    def logout(self):
        self.manager.current = 'login'


class LoginScreen(Screen):
    def on_enter(self):
        # Check if profile details exist in the JSON file
        try:
            with open('profile_details.json', 'r') as file:
                profile_details = json.load(file)
            self.manager.get_screen('profile').name_input.text = profile_details['name']
            self.manager.get_screen('profile').email_input.text = profile_details['email']
            self.manager.get_screen('profile').year_input.text = profile_details['year']

        except FileNotFoundError:
            pass


class Screen_2(Screen):
    pass


class Screen_3(Screen):
    pass


class Screen_4(Screen):
    pass


class Blank(Screen):
    pass


class Maths(Screen):
    pass


class About_Us(Screen):
    pass


class videolectures(Screen):
    pass


class screen0(Screen):
    pass


class screen1(Screen):
    pass


class screen2(Screen):
    pass


class screen3(Screen):
    pass


class screen4(Screen):
    pass


class screen5(Screen):
    pass


class profilepage(Screen):
    pass


class BottomNavigation(MDScreen):
    bottom_navigation_items = [
        {"icon": "home", "text": "home", "pos_hint": {"center_x": 0.1},
         "on_release": lambda x: MDApp.get_running_app().on_nav_button_press(x, "one")},
        {"icon": "bell", "text": "Alerts", "on_release": lambda x: print('menu')},
        {"icon": "account", "text": "account", "on_release": lambda x: MDApp.get_running_app().show_profile_details()},
    ]


sm = ScreenManager()
sm.add_widget(Screen_1(name="one"))
sm.add_widget(Screen_2(name="two"))
sm.add_widget(Screen_3(name="three"))
sm.add_widget(Screen_4(name="four"))
sm.add_widget(Blank(name="none"))
sm.add_widget(Maths(name="p"))
sm.add_widget(About_Us(name="about"))
sm.add_widget(videolectures(name="v1"))
sm.add_widget(screen0(name="01"))
sm.add_widget(screen1(name="02"))
sm.add_widget(screen2(name="03"))
sm.add_widget(screen3(name="04"))
sm.add_widget(screen4(name="05"))
sm.add_widget(screen5(name="five"))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(profilepage(name="page"))


class MyApp(MDApp):
    def build(self):



        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"

        return Builder.load_string(KV)

    def play_video(self, video_url):
        dialog = MDDialog(
            title="Play Video",
            text="Do you want to play this video?",
            buttons=[
                MDFlatButton(text="Cancel",on_release=self.dismiss_dialog),
                MDFlatButton(text="Play", on_release=lambda x: self.open_video(video_url)),
            ],
        )
        dialog.open()

    def open_video(self, video_url):
        webbrowser.open(video_url)

    def dismiss_dialog(self, instance):
        instance.parent.parent.parent.parent.dismiss()

    def go_screen(self):
        current_screen = self.root.current
        if current_screen == "01":
            self.root.current = "v1"
        elif current_screen == "02":
            self.root.current = "v1"
        elif current_screen == "03":
            self.root.current = "v1"
        elif current_screen == "04":
            self.root.current = "v1"
        elif current_screen == "05":
            self.root.current = "v1"

    def on_nav_button_press(self, _, screen_name):
        self.root.current = screen_name

    def login(self):
        profile_screen = self.root.get_screen('profile')
        name_input = profile_screen.name_input.text
        email_input = profile_screen.email_input.text
        year_input = profile_screen.year_input.text

        if name_input and email_input and year_input:
            self.root.current = 'profile'

    def logout(self):
        self.root.current = 'profile'

    def show_profile_details(self):
        profile_details = {}
        try:
            with open('profile_details.json', 'r') as file:
                profile_details = json.load(file)
        except FileNotFoundError:
            pass

        profile_details_screen = self.root.get_screen('page')
        profile_details_screen.ids.name_label.text = f"Name: {profile_details.get('name', '')}"
        profile_details_screen.ids.email_label.text = f"Email: {profile_details.get('email', '')}"
        profile_details_screen.ids.year_label.text = f"Persuing Year: {profile_details.get('year', '')}"
        self.root.current = 'page'


if __name__ == "__main__":
    MyApp().run()
