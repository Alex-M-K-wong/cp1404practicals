"""
Miles to Kilometres Converter
Man Kit Wong
28/10/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres"""
    def build(self):
        """build Kivy app from the kv file"""
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

MilesConverterApp().run()