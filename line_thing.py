from fltk import *

class line(Fl_Window):
	def __init__(self,x,y,w,h,l = None):
		Fl_Window.__init__(self,x,y,w,h,l)
		self.begin()
		self.color(FL_BLACK)
		self.end()
	
	def draw(self):
		Fl_Window.draw(self)
		sep = 10
		fl_color(FL_RED)
		for x in range(0,self.w()+1,sep):
			fl_line(x,501,501,501-x)
		fl_color(FL_YELLOW)
		for x in range(0,self.h()+1,sep):
			fl_line(0,x,501-x,0)
		fl_color(FL_BLUE)
		for x in range(0,self.w()+1,sep):
			fl_line(x,0,501,x)
		fl_color(FL_GREEN)
		for x in range(0,self.h()+1,sep):
			fl_line(x,501,0,x)
		
app = line(0,0,501,501,'line')
app.show()
Fl.run()
