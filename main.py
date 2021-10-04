import kivy

# the App class handles low level code
# which the program will take advantage of
from kivy.app import App

# importing labels and widgets from kivy to use
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.core.audio import SoundLoader 

# this is like the root class
class Grids(Widget):

	def press(self):
		print("Button pressed!")
		sound = SoundLoader.load('assets/button_click.wav')
		sound.play()

class CoolApp(App):

	# build is like an initializing method
	def build(self):

		# we return the grid class to get
		# grid properties (width, widgets, etc.)
		# returning this in this method means
		# we can draw to the screen anything which
		# we want to create in our grid class.
		return Grids()

# to make the app run
if __name__ == "__main__":
	CoolApp().run()