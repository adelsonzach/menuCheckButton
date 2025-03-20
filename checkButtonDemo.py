'''
Chapter 9 Example (Pages 253 - 254)
Program: checkButtonDemo.py
3/18/25

**NOTE: the module breezypython.py MUST be in the same directory as this file for the app to run over properly!

GUI-based app demonstrating the use of the check button (checkbox) graphic component to create a food order.
'''

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class Header (class name will change from project to project)
class CheckButtonDemo(EasyFrame):

	# Definiton of our classes' constructor method
	def __init__(self):
		
		# Call to the EasyFrame class constructor
		EasyFrame.__init__(self, title = "Check Button Demo", width = 240, height = 160, resizable = False, background = "#A3C9A8")
		# Other components are added here
		self.addLabel(text = "Today's Menu", row = 0, column = 0, sticky = "NEWS", columnspan = 2, background = "#A3C9A8", foreground = "black", font = Font(size = 25, family = "Elephant"))
		# Add four check buttons
		self.chickCB = self.addCheckbutton(text = "Chicken", row = 1, column = 0)
		self.tatorCB = self.addCheckbutton(text = "French Fries", row = 1, column = 1)
		self.beanCB = self.addCheckbutton(text = "Grean Beans", row = 2, column = 0)
		self.sauceCB = self.addCheckbutton(text = "Applesause", row = 2, column = 1)

		# Change some color properties of the check buttons
		self.chickCB["background"] = "#A3C9A8"
		self.tatorCB["background"] = "#A3C9A8"
		self.beanCB["background"] = "#A3C9A8"
		self.sauceCB["background"] = "#A3C9A8"

		# Add the comand button
		self.button = self.addButton(text = "Place Order", row = 3, column = 0, columnspan = 2, command = self.placeOrder)
		self.button["background"] = "#50808E"
		self.button["foreground"] = "white"
		self.button["width"] = 24
		self.button["height"] = 2

		

	# Definition of the placeOrder() method which is the event handler
	def placeOrder(self):
		''' Display a pop-up box with the order summary. '''
		message = ""

		# Analyze the Check Button to see if they have been checked
		if self.chickCB.isChecked():
			message += "Chicken\n\n"

		if self.tatorCB.isChecked():
			message += "French Fries\n\n"

		if self.beanCB.isChecked():
			message += "Green Beans\n\n"

		if self.sauceCB.isChecked():
			message += "Applesause\n\n"

		if message == "":
			message = "Sorry, no food ordered! Try again!"

		# Now that we have looked at every check button, lets push the message string to a pop-up
		self.messageBox(title = "Customer Order", message = message, height = 10)




# End of class block

# Global definition of the main() function
def main():
	# Instatiate an object from the class into mainloop()
	CheckButtonDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()
#ZADE