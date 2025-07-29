"""
Miles to Kilometres Converter
Man Kit Wong
28/10/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres"""

    message = StringProperty()

    def build(self):
        """build Kivy app from the kv file"""
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation, output result to label widget """
        value = float(self.get_validated_miles())
        result = value * MILES_TO_KM
        self.message = str(result)

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()