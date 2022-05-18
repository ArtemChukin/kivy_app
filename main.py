from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.window import Window

Window.size = (720, 1280)
Window.clearcolor = (0/255, 78/255, 194/255, 1)
Window.title = "Приложение"

class MyApp(App):
	def build(self):
		bl = BoxLayout()
		bl.orientation = "vertical"
		bl.add_widget(Button(text="Push me"))
		bl.add_widget(Label(text="My programm"))

		return bl

if __name__ == "__main__":
	MyApp().run()