from fltk import *

class MyApp(Fl_Window):
	def __init__(self, x,y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		#create lists of (x,y) 61 points along each line
		self.top=[ (x,10) for x in range(0,601,10) ]
		self.left= [ (x, round(1.732*x)+10) for x in range(0, 301, 5) ]
		self.right = [ (x, round(-1.732*x+1039.2)+10) for x in range(300, 601, 5) ]

	def draw(self):
		Fl_Window.draw(self)
		fl_color(FL_BLUE)
		for i in range(61):
			#fl_line(x1,y1,x2,y2) draws a line between (x1,y1) and (x2,y2)
			fl_line(self.top[i][0], self.top[i][1], self.left[60-i][0], self.left[60-i][1])

		fl_color(FL_RED)
		for i in range(61):
			fl_line(self.top[i][0], self.top[i][1], self.right[60-i][0], self.right[60-i][1])

		fl_color(FL_GREEN)
		for i in range(61):
			fl_line(self.left[i][0], self.left[i][1], self.right[i][0], self.right[i][1])

size=601
app = MyApp(0,0, size, size)
app.resizable(app)
app.show()
Fl.run()
