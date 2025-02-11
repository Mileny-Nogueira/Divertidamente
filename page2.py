from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.config import Config

# Definição das telas em KV
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '390')
kv = """
ScreenManager:
    MenuScreen:
    NoteScreen:
    LoadingScreen:
    MessageScreen:

<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        
        MDLabel:
            text: "Qual emoção está guiando seu dia hoje?"
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H5"
          
        
        MDRaisedButton:
            text: "Tristeza"

            on_release: app.set_note("Tristeza")
        MDRaisedButton:
            text: "Raiva"
            on_release: app.set_note("Raiva")
        MDRaisedButton:
            text: "Alegria"
            on_release: app.set_note("Alegria")
        MDRaisedButton:
            text: "Nojinho"
            on_release: app.set_note("Nojinho")
        MDRaisedButton:
            text: "Medo"
            on_release: app.set_note("Medo")

<NoteScreen>:
    name: 'note'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        
        MDLabel:
            id: note_label
            text: "Conte mais sobre esse sentimento..."
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H5"
        
        MDTextField:
            id: note_input
            hint_text: "Registre aqui uma memória para ser armazenada na Máquina de Pensamentos:"
            multiline: True
        
        MDRaisedButton:
            text: "Continuar"
            on_release: app.show_loading_screen()
            

        MDRaisedButton:
            text: "Voltar"
            on_release: app.root.current = 'menu'

<LoadingScreen>:
    name: "loading"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Processando..."
            font_size: 20
        Label:
            text: "⌛"
            font_size: 40

<MessageScreen>:
    name: 'message'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        
        MDLabel:
            id: message_label
            text: ""
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H5"
        
        MDRaisedButton:
            text: "Voltar ao menu"
            on_release: app.root.current = 'menu'
"""



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
        return Builder.load_string(kv)  # Agora usa o ScreenManager diretamente

    def set_note(self, option):
        self.selected_option = option
        note_screen = self.root.get_screen("note")  # Acessa corretamente o ScreenManager
        note_screen.ids.note_label.text = f"Nota atribuída à opção {option}:"
        note_screen.ids.note_input.text = ""
        self.root.current = "note"


    def show_loading_screen(self):
        note_screen = self.root.get_screen("note")
        self.user_note = note_screen.ids["note_input"].text if "note_input" in note_screen.ids else ""
        self.root.current = "loading"
        Clock.schedule_once(self.show_message, 2)

    def show_message(self, dt):
        note_screen = self.root.get_screen("note")  # Acessa corretamente o ScreenManager
        user_note = note_screen.ids.note_input.text
        message_text = self.messages.get(self.selected_option, "Opção inválida") + f"\nSua nota: {self.user_note}"
        message_screen = self.root.get_screen("message")
        message_screen.ids.message_label.text = message_text
        self.root.current = "message"

if __name__ == "__main__":
    MyApp().run()