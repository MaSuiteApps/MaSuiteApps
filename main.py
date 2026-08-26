from kivy.app import App
from kivy.uix.label import Label

class MaApp(App):
    def build(self):
        return Label(text='Salut MaSuiteApps!')

if __name__ == '__main__':
    MaApp().run()
