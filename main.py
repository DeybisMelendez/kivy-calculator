import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Main(BoxLayout):
	value1 = None
	value2 = None
	operation = None
	def set_value(self, value):
		self.ids.operation.text += value
	def add(self):
		self.operation = "+"
		self.checkOp()
	def sub(self):
		self.operation = "-"
		self.checkOp()
	def mul(self):
		self.operation = "*"
		self.checkOp()
	def div(self):
		self.operation = "/"
		self.checkOp()
	def delete(self):
		temp = len(self.ids.operation.text)
		self.ids.operation.text = self.ids.operation.text[:temp - 1]
	def clear(self):
		self.ids.operation.text = ""
		self.value1 = None
		self.value2 = None
		self.operation = None
	def equal(self):
		if self.value1 != None and self.operation != None:
			result = None
			if self.operation == "+":
				self.value2 = float(self.ids.operation.text)
				result = self.value1 + self.value2
			if self.operation == "-":
				self.value2 = float(self.ids.operation.text)
				result = self.value1 - self.value2
			if self.operation == "*":
				self.value2 = float(self.ids.operation.text)
				result = self.value1 * self.value2
			if self.operation == "/":
				self.value2 = float(self.ids.operation.text)
				result = self.value1 / self.value2
			self.ids.operation.text = str(result)
			self.value1 = None #result
			self.value2 = None
			self.operation = None
	def checkOp(self):
		try:
			if self.value1 == None:
				self.value1 = float(self.ids.operation.text)
				self.ids.operation.text = ""
			elif self.operation != None:
				self.equal()
		except:
			pass

class MainApp(App):
	title = "Kivy Calculator"
	def build(self):
		return Main()

if __name__ == '__main__':
    MainApp().run()
