try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	# Python 2
	import Tkinter as tk
	import ttk

import parser

class TkGUI(tk.Tk):
	FONT_LARGE = ("Calibri", 35)  	# selects the font of the text inside buttons
	FONT_MED = ("Calibri", 30)

	# Max rows and columns in the GUI
	MAX_ROW = 101 
	MAX_COLUMN = 101
	i = 0
	NEW_OPERATION = False

	def __init__(self):
		try:
			super(TkGUI, self).__init__()
		except TypeError:
			# Python 2
			tk.Tk.__init__(self)

		self.title('Math Buddy')
		self.resizable(width=101, height=101)

		# Configure default theme
		style = ttk.Style(self)
		self.configure(bg="aquamarine")
		
		for row in range(self.MAX_ROW):
			self.columnconfigure(row,pad=25)

		for column in range(self.MAX_COLUMN):
			self.rowconfigure(column,pad=25)

		self.display = tk.Entry(self, bg="yellow", font=("Calibri", 30))
		self.display.grid(row=1, columnspan=101, sticky=tk.W + tk.E)

		self._init_ui()
        
	def _init_ui(self):
		one = tk.Button(
			self, text="1", command=lambda: self.get_variables(1), font=self.FONT_LARGE)
		one.grid(row=2, column=1)
		two = tk.Button(
			self, text="2", command=lambda: self.get_variables(2), font=self.FONT_LARGE)
		two.grid(row=2, column=25)
		three = tk.Button(
			self, text="3", command=lambda: self.get_variables(3), font=self.FONT_LARGE)
		three.grid(row=2, column=50)

		four = tk.Button(
			self, text="4", command=lambda: self.get_variables(4), font=self.FONT_LARGE)
		four.grid(row=4, column=1)
		five = tk.Button(
			self, text="5", command=lambda: self.get_variables(5), font=self.FONT_LARGE)
		five.grid(row=4, column=25)
		six = tk.Button(
			self, text="6", command=lambda: self.get_variables(6), font=self.FONT_LARGE)
		six.grid(row=4, column=50)

		seven = tk.Button(
			self, text="7", command=lambda: self.get_variables(7), font=self.FONT_LARGE)
		seven.grid(row=6, column=1)
		eight = tk.Button(
			self, text="8", command=lambda: self.get_variables(8), font=self.FONT_LARGE)
		eight.grid(row=6, column=25)
		nine = tk.Button(
			self, text="9", command=lambda: self.get_variables(9), font=self.FONT_LARGE)
		nine.grid(row=6, column=50)

		cls = tk.Button(self, text="AC", command=self.clear_all,
						font=self.FONT_LARGE, foreground="red")
		cls.grid(row=8, column=1)
		zero = tk.Button(
			self, text="0", command=lambda: self.get_variables(0), font=self.FONT_LARGE)
		zero.grid(row=8, column=25)
		result = tk.Button(self, text="=", command=self.calculate,
						   font=self.FONT_LARGE, foreground="red")
		result.grid(row=8, column=50)

		plus = tk.Button(
			self, text="+", command=lambda: self.get_operation("+"), font=self.FONT_LARGE)
		plus.grid(row=2, column=75)
		minus = tk.Button(
			self, text="-", command=lambda: self.get_operation("-"), font=self.FONT_LARGE)
		minus.grid(row=4, column=75)
		multiply = tk.Button(
			self, text="*", command=lambda: self.get_operation("*"), font=self.FONT_LARGE)
		multiply.grid(row=6, column=75)
		divide = tk.Button(
			self, text="/", command=lambda:  self.get_operation("/"), font=self.FONT_LARGE)
		divide.grid(row=8, column=75)

		# adding new operations
		undo_button = tk.Button(
			self, text="<-", command=self.undo, font=self.FONT_LARGE, foreground="red")
		undo_button.grid(row=2, column=100)
		
		right_bracket = tk.Button(
			self, text=")", command=lambda: self.get_operation(")"), font=self.FONT_LARGE)
		right_bracket.grid(row=4, column=100)
		
		left_bracket = tk.Button(
			self, text="(", command=lambda: self.get_operation("("), font=self.FONT_LARGE)
		left_bracket.grid(row=6, column=100)
		
		square = tk.Button(
			self, text="^2", command=lambda: self.get_operation("**2"), font=self.FONT_MED)
		square.grid(row=8, column=100)

	def factorial(self, operator):
		"""Calculates the factorial of the number entered."""
		number = int(self.display.get())
		fact = 1
		try:
			while number > 0:
				fact = fact*number
				number -= 1
			self.clear_all()
			self.display.insert(0, fact)
		except Exception:
			self.clear_all()
			self.display.insert(0, "Error")

	def clear_all(self, new_operation=True):
		"""clears all the content in the Entry widget."""
		self.display.delete(0, tk.END)
		self.NEW_OPERATION = new_operation

	def get_variables(self, num):
		"""Gets the user input for operands and puts it inside the entry widget.

		If a new operation is being carried out, then the display is cleared.
		"""
		if self.NEW_OPERATION:
			self.clear_all(new_operation=False)
		self.display.insert(self.i, num)
		self.i += 1

	def get_operation(self, operator):
		"""Gets the operand the user wants to apply on the functions."""
		length = len(operator)
		self.display.insert(self.i, operator)
		self.i += length

	def undo(self):
		"""removes the last entered operator/variable from entry widget."""
		whole_string = self.display.get()
		if len(whole_string):        ## repeats until
			## now just decrement the string by one index
			new_string = whole_string[:-1]
			self.clear_all(new_operation=False)
			self.display.insert(0, new_string)
		else:
			self.clear_all() 
			self.display.insert(0, "Error, press AC")

	def calculate(self):
	    """Evaluates the expression.

	    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
	    """
	    whole_string = self.display.get()
	    try:
	        formulae = parser.expr(whole_string).compile()
	        result = eval(formulae)
	        self.clear_all()
	        self.display.insert(0, result)
	    except Exception:
	        self.clear_all()
	        self.display.insert(0, "Error!")

	def run(self):
		"""Initiate event loop."""
		self.mainloop()
		

from MathBuddy import TkGUI

app = TkGUI()
app.run()
