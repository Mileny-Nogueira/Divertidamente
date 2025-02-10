from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.config import Config
from datetime import datetime
from kivy.lang import Builder

# Configurações da janela
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '390')

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
            on_release: app.root.current = "next_screen"

<CanvasButton@Button>:
    background_normal: ""
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: 0.3, 0.6, 1, 1
        Ellipse:
            pos: self.pos
            size: self.size
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


class MyApp(App):
    def build(self):
        self.title = "Divertidamente"
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='home'))
        return sm


MyApp().run()
