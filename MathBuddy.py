# Tkinter Module import.
try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	import Tkinter as tk
	import ttk
	
import parser

class TkGUI(tk.Tk):
    # Font of the text inside buttons.
	FONT_LARGE = ("Calibri", 35)  	
	FONT_MED = ("Calibri", 30)

	# Customized rows and columns in the GUI.
	MAX_ROW = 101 
	MAX_COLUMN = 101
	i = 0
	NEW_OPERATION = False

	def __init__(self):
		try:
			super(TkGUI, self).__init__()
		except TypeError:
			tk.Tk.__init__(self)

		self.title('Math Buddy')
		self.resizable(width=101, height=101)

		# GUI theme.
		style = ttk.Style(self)
		self.configure(bg="aquamarine")
		
		for row in range(self.MAX_ROW):
			self.columnconfigure(row,pad=25)

		for column in range(self.MAX_COLUMN):
			self.rowconfigure(column,pad=25)

		self.display = tk.Entry(self, bg="yellow", font=("Calibri", 30))
		self.display.grid(row=1, columnspan=101, sticky=tk.W + tk.E)
                
		self._init_ui()
		print("")
		print("                                  /|         ,")
		print("                               ,///        /|")
		print("                              // //     ,///")
		print("                             // //     // //")
		print("                            // //     || ||")
		print("                           || ||    // //")
		print("                           || ||   // //")
		print("                           || ||  // //")
		print("                           || || || ||")
		print("                           \\,\|,|\_//")
		print("                            \\)\)\\|/")
		print("                            )-."" .-(")
		print("                           //^\` `/^\\")
		print("                          //  |   |  \\")
		print("                        ,/_| 0| _ | 0|_\,")
		print('                      /`    `"=.v.="`    `\ ')
		print('                     /`    _."{_,_}"._    `\ ')
		print("                     `/`  ` \  |||  / `  `\` ")
		print('                      `",_  \\=^~^=//  _,"` ')
		print("                          '=,\'-=-'/,=' ")
		print("")
		print("         HELLO! YOU ARE NOW SUCESSFULLY RUNNING MathBuddy.py V3!")
		print("")
		
	def _init_ui(self):
	    # GUI Buttons Functionality.
		one = tk.Button(
			self, text="1", command=lambda: self.get_variables(1), font=self.FONT_LARGE, foreground="green")
		one.grid(row=2, column=1)
		two = tk.Button(
			self, text="2", command=lambda: self.get_variables(2), font=self.FONT_LARGE, foreground="green")
		two.grid(row=2, column=25)
		three = tk.Button(
			self, text="3", command=lambda: self.get_variables(3), font=self.FONT_LARGE, foreground="green")
		three.grid(row=2, column=50)

		four = tk.Button(
			self, text="4", command=lambda: self.get_variables(4), font=self.FONT_LARGE, foreground="green")
		four.grid(row=4, column=1)
		five = tk.Button(
			self, text="5", command=lambda: self.get_variables(5), font=self.FONT_LARGE, foreground="green")
		five.grid(row=4, column=25)
		six = tk.Button(
			self, text="6", command=lambda: self.get_variables(6), font=self.FONT_LARGE, foreground="green")
		six.grid(row=4, column=50)

		seven = tk.Button(
			self, text="7", command=lambda: self.get_variables(7), font=self.FONT_LARGE, foreground="green")
		seven.grid(row=6, column=1)
		eight = tk.Button(
			self, text="8", command=lambda: self.get_variables(8), font=self.FONT_LARGE, foreground="green")
		eight.grid(row=6, column=25)
		nine = tk.Button(
			self, text="9", command=lambda: self.get_variables(9), font=self.FONT_LARGE, foreground="green")
		nine.grid(row=6, column=50)

		cls = tk.Button(self, text="AC", command=self.clear_all,
						font=self.FONT_LARGE, foreground="red")
		cls.grid(row=8, column=1)
		zero = tk.Button(
			self, text="0", command=lambda: self.get_variables(0), font=self.FONT_LARGE, foreground="green")
		zero.grid(row=8, column=25)
		result = tk.Button(self, text="=", command=self.calculate,
						   font=self.FONT_LARGE, foreground="red")
		result.grid(row=8, column=50)

		plus = tk.Button(
			self, text="+", command=lambda: self.get_operation("+"), font=self.FONT_LARGE, foreground="blue")
		plus.grid(row=2, column=75)
		minus = tk.Button(
			self, text="-", command=lambda: self.get_operation("-"), font=self.FONT_LARGE, foreground="blue")
		minus.grid(row=4, column=75)
		multiply = tk.Button(
			self, text="*", command=lambda: self.get_operation("*"), font=self.FONT_LARGE, foreground="blue")
		multiply.grid(row=6, column=75)
		divide = tk.Button(
			self, text="/", command=lambda:  self.get_operation("/"), font=self.FONT_LARGE, foreground="blue")
		divide.grid(row=8, column=75)

		# Custom new operations.
		undo_button = tk.Button(
			self, text="<-", command=self.undo, font=self.FONT_LARGE, foreground="red")
		undo_button.grid(row=2, column=100)
		
		right_bracket = tk.Button(
			self, text=")", command=lambda: self.get_operation(")"), font=self.FONT_LARGE, foreground="blue")
		right_bracket.grid(row=4, column=100)
		
		left_bracket = tk.Button(
			self, text="(", command=lambda: self.get_operation("("), font=self.FONT_LARGE, foreground="blue")
		left_bracket.grid(row=6, column=100)
		
		square = tk.Button(
			self, text="^2", command=lambda: self.get_operation("**2"), font=self.FONT_MED, foreground="blue")
		square.grid(row=8, column=100)
    
	def factorial(self, operator):
		# Function calculates the factorial of the number entered.
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
		# Function clears all the content in the Entry widget.
		self.display.delete(0, tk.END)
		self.NEW_OPERATION = new_operation
	def get_variables(self, num):
		# Function gets the user input for operands and puts it inside the entry widget.
		if self.NEW_OPERATION:
			self.clear_all(new_operation=False)
		self.display.insert(self.i, num)
		self.i += 1
		print("")
		print("              SPONGE-BOB")
		print('      .--..--..--..--..--..--.')
		print("    .' \  (`._   (_)     _   \ ")
		print("  .'    |  '._)         (_)  |")
		print("  \ _.')\      .----..---.   /")
		print("  |(_.'  |    /    .-\-.  \  |")
		print("  \     0|    |   ( O| O) | o|")
		print("   |  _  |  .--.____.'._.-.  |")
		print("   \ (_) | o         -` .-`  |")
		print("    |    \   |`-._ _ _ _ _\ /")
		print("    \    |   |  `. |_||_|   |")
		print("    | o  |    \_      \     |     -.   .-.")
		print("    |.-.  \     `--..-'   O |     `.`-' .'")
		print("  _.'  .' |     `-.-'      /-.__   ' .-'")
		print(".' `-.` '.|='=.='=.='=.='=|._/_ `-'.'")
		print("`-._  `.  |________/\_____|    `-.'")
		print("   .'   ).| '=' '='\/ '=' |")
		print("   `._.`  '---------------'")
		print("           //___\   //___\ ")
		print("             ||       ||")
		print("             ||_.-.   ||_.-.")
		print("            (_.--__) (_.--__)")
		print("")
		print("GREAT JOB! KEEP UP THE GOOD WORK! YOU HAVE SELECTED AN INTEGER...")
		print("")
                      
	def get_operation(self, operator):
		# Function gets the operator that the user wants to apply to the expression.
		length = len(operator)
		self.display.insert(self.i, operator)
		self.i += length
		print("")
		print("                  SPIDER-MAN")
		print("                     ,,,, ")
		print("               ,;) .';;;;',")
		print("  ;;,,_,-.-.,;;'_,|I\;;;/),,_")
		print("   `';;/:|:);{ ;;;|| \;/ /;;;\__")
		print("        L;/-';/ \;;\',/;\/;;;.') \ ")
		print("       .:`''` - \;;'.__/;;;/  . _'-._")
		print("     .'/   \     \;;;;;;/.'_7:.  '). \_")
		print("   .''/     | '._ );}{;//.'    '-:  '.,L")
		print(" .'. /       \  ( |;;;/_/         \._./;\   _,")
		print("  . /        |\ ( /;;/_/             ';;;\,;;_,")
		print(" . /         )__(/;;/_/                (;;'''''")
		print("  /        _;:':;;;;:';-._             );")
		print(" /        /   \  `'`   --.'-._         \/")
		print("        .'     '.  ,'         '-,")
		print("      /    /   r--,..__       '.\ ")
		print("    .'    '  .'        '--._     ]")
		print("    (     :.(;>        _ .' '- ;/")
		print("    |      /:;(    ,_.';(   __.'")
		print("     '- -' |;:/    (;;;;-'--'")
		print("           |;/      ;;(")
		print("           ''      /;;|")
		print("                   \;;|")
		print("                    \/")
		print("")
		print("EXCELLENT! KEEP UP THE GOOD WORK! YOU HAVE SELECTED AN OPERATOR...")
		print("")

	def undo(self):
		# Function removes the last entered value from the entry widget.
		whole_string = self.display.get()
		if len(whole_string):        
			new_string = whole_string[:-1]
			self.clear_all(new_operation=False)
			self.display.insert(0, new_string)
			print("")
			print("         SQUIDWARD")
			print("      .--'''''''''--. ")
			print("   .'      .---.      '.")
			print("  /    .-----------.    \ ")
			print(" /        .-----.        \ ")
			print(" |       .-.   .-.       |")
			print(" |      /   \ /   \      |")
			print("  \    | .-. | .-. |    /")
			print("   '-._| | | | | | |_.-'")
			print("       | '-' | '-' |")
			print("        \___/ \___/")
			print("     _.-'  /   \  `-._")
			print("   .' _.--|     |--._ '.")
			print("   ' _...-|     |-..._ '")
			print("          |     |")
			print("          '.___.'")
			print("            | |")
			print("           _| |_")
			print("          /\( )/\ ")
			print("         /  ` '  \ ")
			print("        | |     | |")
			print("        '-'     '-'")
			print("        | |     | |")
			print("        | |     | |")
			print("        | |-----| |")
			print("     .`/  |     | |/`.")
			print("     |    |     |    |")
			print("     '._.'| .-. |'._.'")
			print("           \ | /")
			print("           | | |")
			print("           | | |")
			print("           | | |")
			print("          /| | |\ ")
			print("        .'_| | |_`.")
			print("        `. | | | .'")
			print("          /  |  \ ")
			print("    /o`.-'  / \  `-.`o\ ")
			print("   /o  o\ .'   `. /o  o\ ")
			print("   `.___.'       `.___.'")
			print("")
			print("YOUR ENTRY HAS BEEN BACKSPACED...")
			print("")
                        
		else:
			self.clear_all() 
			self.display.insert(0, "Error, press AC")

	def calculate(self):
	    # Function evaluates the expression.        
	    whole_string = self.display.get()
	    try:
	        formulae = parser.expr(whole_string).compile()
	        result = eval(formulae)
	        self.clear_all()
	        self.display.insert(0, result)
	        print("")
	        print("          MICKEY MOUSE")
	        print('            .-"""-.  ')
	        print("           /       \ ")
	        print("           \       / ")
	        print('    .-"""-.-`.-.-.<  _')
	        print("   /      _,-\ ()()_/:) ")
	        print("   \     / ,  `     `| ")
	        print("    '-..-| \-.,___,  / ")
	        print("          \ `-.__/  / ")
	        print("         / `-.__.-\` ")
	        print("        / /|    ___\ ")
	        print("       ( ( |.- `   `'\ ")
	        print("        \ \/    {}{}  | ")
	        print("         \|           / ")
	        print("          \        , / ")
	        print("          ( __`;-;'__`) ")
	        print("          `//'`   `||` ")
	        print("         _//       || ")
	        print(' .-"-._,(__)     .(__).-""-.')
	        print("/          \    /           \ ")
	        print('\          /    \           /')
	        print(" `'-------`      `--------'`")
	        print("")
	        print("                                    _____")
	        print("                                .d88888888bo.")
	        print("                              .d8888888888888b.")
	        print("                              8888888888888888b")
	        print("                              888888888888888888")
	        print("                              888888888888888888")
	        print("                               Y8888888888888888")
	        print("                         ,od888888888888888888P")
	        print("                      .'`Y8P'```'Y8888888888P'")
	        print("                    .'_   `  _     'Y88888888b")
	        print("                   /  _`    _ `      Y88888888b   ____")
	        print("               _  | /  \  /  \      8888888888.d888888b.")
	        print("              d8b | | /|  | /|      8888888888d8888888888b")
	        print("             8888_\ \_|/  \_|/      d888888888888888888888b")
	        print("             .Y8P  `'-.            d88888888888888888888888")
	        print("            /          `          `      `Y8888888888888888")
	        print("           |                        __    888888888888888P")
	        print("            \                       / `   dPY8888888888P'")
	        print("             '._                  .'     .'  `Y888888P`")
	        print("                ` '-.,__    ___.-'    .-'")
	        print("                    `-._````  __..--'`")
	        print("                        ``````")
	        print("")
	        print("")
	        print(" NICE WORK! YOU HAVE SUCCESSFULLY CALCULATED THE EXPRESSION...")
	        print("")
	    except Exception:
	        self.clear_all()
	        self.display.insert(0, "Error!")
                
	def run(self):
		# Internal infinite loop.
		self.mainloop()

                      
		
print("             _    _      _                            _____     ")
print("            | |  | |    | |                          |_   _|    ")
print("            | |  | | ___| | ___ ___  _ __ ___   ___    | | ___  ")
print("            | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ ")
print("            \  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |")
print("             \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/ ")
print("")
print("          ___  ___      _   _      ______           _     _       ")
print("          |  \/  |     | | | |     | ___ \         | |   | |      ")
print("          | .  . | __ _| |_| |__   | |_/ /_   _  __| | __| |_   _ ")
print("          | |\/| |/ _` | __| '_ \  | ___ \ | | |/ _` |/ _` | | | |")
print("          | |  | | (_| | |_| | | | | |_/ / |_| | (_| | (_| | |_| |")
print("          \_|  |_/\__,_|\__|_| |_| \____/ \__,_|\__,_|\__,_|\__, |")
print("                                                             __/ |")
print("                                                            |___/ ")

app = TkGUI()
app.run()

print(" _____ _                 _         ______           _   _     _             ")
print("|_   _| |               | |        |  ___|         | | | |   (_)            ")
print("  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __  | | | |___ _ _ __   __ _ ")
print("  | | | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | | | / __| | '_ \ / _` |")
print("  | | | | | | (_| | | | |   <\__ \ | || (_) | |    | |_| \__ \ | | | | (_| |")
print("  \_/ |_| |_|\__,_|_| |_|_|\_\___/ \_| \___/|_|     \___/|___/_|_| |_|\__, |")
print("                                                                      __/ |")
print("                                                                     |___/ ")
print
print("          ___  ___      _   _      ______           _     _       ")
print("          |  \/  |     | | | |     | ___ \         | |   | |      ")
print("          | .  . | __ _| |_| |__   | |_/ /_   _  __| | __| |_   _ ")
print("          | |\/| |/ _` | __| '_ \  | ___ \ | | |/ _` |/ _` | | | |")
print("          | |  | | (_| | |_| | | | | |_/ / |_| | (_| | (_| | |_| |")
print("          \_|  |_/\__,_|\__|_| |_| \____/ \__,_|\__,_|\__,_|\__, |")
print("                                                             __/ |")
print("                                                            |___/ ")
