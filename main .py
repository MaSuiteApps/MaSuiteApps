from kivy.app import App
from kivy.uix.label import Label

class MaSuiteApp(App):
    def build(self):
        return Label(text='Salut MaSuiteApps !')

MaSuiteApp().run()
