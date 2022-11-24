from fltk import *

class cross(Fl_Window):
	def __int__(self,x,y,w,h,l=None):
		super().__init__(x,y,w,h,l)
		fl_color(FL_BLACK)
	
	def cross(self,n,length,center):
		if n == 0:
			return None
		
		fl_line(center-length,center+length,center+length,center+length)
		fl_line(center-length,center-length,center-length,center+length)
		fl_line(center-length,center-length,center+length,center-length)
		fl_line(center+length,center-length,center+length,center+length)
		
		x = self.round(length)
		return self.cross(n-1,x,center)
		
	
	def round(self,n):
		return round(n/2)
	
	def draw(self):
		Fl_Window.draw(self)
		fl_color(FL_RED)
		
		fl_line(400,0,400,800)
		fl_line(0,400,800,400)
		
		self.cross(6,200,400)
	
app = cross(500,500,800,800,'cross')
app.show()
Fl.run()
