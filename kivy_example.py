from kivy.app import App
from kivy.uix.button import Button

# python -m pip install --upgrade pip setuptools virtualenv
# python -m virtualenv kivy_venv
# kivy_venv\Scripts\activate
# python -m pip install kivy[base] kivy_examples
# python kivy_example.py


class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()