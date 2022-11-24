from fltk import *

class connect_dots(Fl_Window):
	def __init__(self,x,y,w,h,l=None):
		super().__init__(x,y,w,h,l)
		fl_color(FL_WHITE)
	
	def triangle(self,a,b,c,n):
		if n == 0:
			return None
		fl_line(a[0],a[1],b[0],b[1])
		fl_line(a[0],a[1],c[0],c[1])
		fl_line(b[0],b[1],c[0],c[1])
		
		a2 = self.midpoint(a,b)
		b2 = self.midpoint(b,c)
		c2 = self.midpoint(a,c)
		
		return self.triangle(a,a2,c2,n-1),self.triangle(b,b2,a2,n-1),self.triangle(c,c2,b2,n-1)
		
	def draw(self):
		Fl_Window.draw(self)
		fl_color(FL_RED)
		a = (350,10)
		b = (4,610)
		c = (696,610)
		self.triangle(a,b,c,7)
		
	def midpoint(self,a,b):
		a2 = (round((a[0]+b[0])/2),round((a[1]+b[1])/2))
		return a2
		
app = connect_dots(400,400,700,700,'thing')
app.show()
Fl.run()
