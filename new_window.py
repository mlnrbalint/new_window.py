from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    pass


class SecondWindow(Screen, BoxLayout):
    clear = False

    def calculate(self):
        expression = self.ids["display"].text

        try:
            exp = str(eval(expression))
        except:
            exp = "Invalid operation!"
            self.clear = True

        self.ids["display"].text = exp

    def button_pressed(self, btn):
        if self.clear:
            self.ids["display"].text = ""
            self.clear = False

        text = btn.text
        self.ids["display"].text += text


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('new_window.kv')


class Calculator(App):
    def build(self):
        return kv


if __name__ == '__main__':
    Calculator().run()
