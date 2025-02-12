from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '390')
from datetime import datetime
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput

# Estilo
kv = """
<FirstScreen>:
    canvas.before:
        Rectangle:
            source: 'assets/img/fundo_home.png'
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        padding: dp(10)
        spacing: dp(10)

        Label:
            id: time_label
            text: "00:00"
            font_name: "assets/fonts/Montserrat-Bold.ttf"
            font_size: "60sp"
            color: [1, 1, 1, 1]
            size_hint_y: None
            height: dp(40)
            halign: 'center'
            padding: 0, dp(80), 0, 0

        Label:
            id: date_label
            text: "dia, mês"
            font_name: "assets/fonts/Montserrat-Light.ttf"
            font_size: "25sp"
            color: [1, 1, 1, 1]
            size_hint_y: None
            height: dp(40)
            halign: 'center'
            padding: 0, dp(80), 0, 0

        Widget:
            size_hint_y: 2

        Button:
            size_hint: None, None
            size: dp(60), dp(60)
            pos_hint: {"center_x": 0.5}
            background_normal: 'assets/img/button.png'
            background_down: 'assets/img/button_click.png'
            on_release: app.root.current = "menu"

<CanvasButton@Button>:
    background_normal: ""
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: 0.3, 0.6, 1, 1
        Ellipse:
            pos: self.pos
            size: self.size

<MenuScreen>:
    name: 'menu'
    canvas.before:
        Color:
            rgba: (42/255, 38/255, 105/255, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(8)
        padding: dp(15)
        halign: "left"
        
        MDBoxLayout:
            orientation: "horizontal"
            spacing: dp(10)
            size_hint_y: None
            height: dp(50)

            MDLabel:
                text: "Qual emoção está guiando seu dia hoje?"
                halign: "left"
                font_name: "assets/fonts/Montserrat-Italic.ttf"
                font_size: "27sp"
                color: [1, 1, 1, 1]

            Image:
                source: "assets/img/cloud.png"
                size_hint: None, None
                size: dp(60), dp(60)
        

        Button:
            background_normal: 'assets/img/btn_tristeza.png'
            size_hint: None, None
            size: dp(206), dp(50)
            pos_hint: {"center_x": 0.5}
            on_release: app.set_note("Tristeza")

        Button:
            background_normal: 'assets/img/btn_raiva.png'
            size_hint: None, None
            size: dp(206), dp(50)
            pos_hint: {"center_x": 0.5}
            on_release: app.set_note("Raiva")

        Button:
            background_normal: 'assets/img/btn_alegria.png'
            size_hint: None, None
            size: dp(206), dp(50)
            pos_hint: {"center_x": 0.5}
            on_release: app.set_note("Alegria")
        
        Button:
            background_normal: 'assets/img/btn_nojinho.png'
            size_hint: None, None
            size: dp(206), dp(50)
            pos_hint: {"center_x": 0.5}
            on_release: app.set_note("Nojinho")
        
        Button:
            background_normal: 'assets/img/btn_medo.png'
            size_hint: None, None
            size: dp(206), dp(50)
            pos_hint: {"center_x": 0.5}
            on_release: app.set_note("Medo")        

<NoteScreen>:
    name: 'note'
    canvas.before:
        Color:
            rgba: (42/255, 38/255, 105/255, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(60)
        
        MDLabel:
            id: note_label
            text: "Conte mais sobre esse sentimento..."
            halign: "left"
            font_name: "assets/fonts/Montserrat-Italic.ttf"
            font_size: "27sp"
            color: [1, 1, 1, 1]
        
        MDTextField:
            id: note_input
            multiline: True
            font_name: "assets/fonts/Montserrat-ThinItalic.ttf" 
            font_size: "20sp"
            max_text_length: 200
            color: [1, 1, 1, 1]

            canvas.before:
                Color:
                    rgba: (246/255, 139/255, 188/255, 1)
                Line:
                    width: 1
                    points: self.x, self.y, self.x, self.top
        
        MDRaisedButton:
            text: "         Armazenar Orbe         "
            on_release: app.show_loading_screen()
            font_name: "assets/fonts/Montserrat-Light.ttf"
            font_size: "20sp"
            size_hint_y: None
            md_bg_color: (246/255, 139/255, 188/255, 1)
            

<LoadingScreen>:
    name: "loading"
    canvas.before:
        Rectangle:
            source: 'assets/img/loading.png'
            pos: self.pos
            size: self.size

<MessageScreen>:
    name: 'message'
    canvas.before:
        Color:
            rgba: (42/255, 38/255, 105/255, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        
        MDLabel:
            id: message_label
            text: ""
            halign: "left"
            font_name: "assets/fonts/Montserrat-Italic.ttf"
            font_size: "22sp"
            color: [1, 1, 1, 1]
 
        MDRaisedButton:
            text: "Voltar ao menu"
            on_release: app.root.current = 'menu'
            md_bg_color: (246/255, 139/255, 188/255, 1)
            font_size: "20sp"
            font_name: "assets/fonts/Montserrat-Light.ttf"
"""

Builder.load_string(kv)

class FirstScreen(Screen):
    def update_time(self, *args):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%A, %d %B").capitalize()

        self.ids.time_label.text = current_time
        self.ids.date_label.text = current_date

    def on_enter(self):
        self.update_time()
        Clock.schedule_interval(self.update_time, 1)

    def on_leave(self):
        Clock.unschedule(self.update_time)

class MenuScreen(Screen):
    pass

class NoteScreen(Screen):
    pass

class LoadingScreen(Screen):
    pass

class MessageScreen(Screen):
    pass

class MyApp(MDApp):
    messages = { 
        "Tristeza": "'A tristeza pode ser uma forma de aprender e crescer. Permita-se sentir, mas também busque o apoio e as coisas que te fazem bem.'",
        "Raiva": "'A raiva pode ser um sinal de que algo importante precisa mudar. Respire fundo e transforme essa energia em ação positiva.'",
        "Alegria": "'Que incrível! A vida é cheia de pequenos momentos mágicos... Aproveite cada um deles! Continue espalhando essa energia contagiante.'",
        "Nojinho": "'Nem tudo é agradável, e tá tudo bem sentir isso. O importante é saber escolher o que te faz bem e manter distância do que não faz.'",
        "Medo": "'O medo é um lembrete de que você é corajoso por enfrentar desafios. Confie no seu potencial — você é mais forte do que pensa.'" 
    }

    def build(self):
        self.title = "Divertidamente"
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='home'))
        sm.add_widget(MenuScreen(name='menu'))  
        sm.add_widget(NoteScreen(name='note'))
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(MessageScreen(name='message'))
        return sm
    
    def set_note(self, option):
        self.selected_option = option
        note_screen = self.root.get_screen("note") 
        note_screen.ids.note_input.text = ""
        self.root.current = "note"

    def show_loading_screen(self):
        note_screen = self.root.get_screen("note")
        self.user_note = note_screen.ids["note_input"].text if "note_input" in note_screen.ids else ""
        self.root.current = "loading"
        Clock.schedule_once(self.show_message, 3)

    def show_message(self, dt):
        note_screen = self.root.get_screen("note")  # Acessa corretamente o ScreenManager
        user_note = note_screen.ids.note_input.text
        message_text = self.messages.get(self.selected_option, "Opção inválida") + f"\nSua nota: {self.user_note}"
        message_screen = self.root.get_screen("message")
        message_screen.ids.message_label.text = message_text
        self.root.current = "message"

MyApp().run()
