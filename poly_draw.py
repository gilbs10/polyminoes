
import cairo
from math import ceil
from utils import get_all_neighbors

fg_colors = {"black": (0,0,0), "red": (0.9,0.8,0.8), "white": (1,1,1)}
bg_colors = {"black": (0.8,0.8,0.8), "red": (1,0.9,0.9), "white": (1,1,1)}

def draw_cell(cr,x_shift,y_shift,cell_size,color = "black"):
	if color in bg_colors:
		cr.set_source_rgb(*bg_colors[color])
		cr.rectangle(x_shift,y_shift, cell_size	, cell_size)
		cr.fill()
	if color in fg_colors:
		cr.set_source_rgb(*fg_colors[color])
		cr.set_line_join(cairo.LINE_JOIN_MITER)
		cr.set_line_width(1)
		cr.rectangle(x_shift,y_shift, cell_size, cell_size)
		cr.stroke()

def draw_poly(cr,poly,x_shift,y_shift, main_color, perimeter_color,cell_size= 5):
	min_x = min([p[0] for p in poly])
	max_y = max([p[1] for p in poly])
	for p in poly:
		for n in get_all_neighbors(p):
			if n not in poly:
				draw_cell(cr,x_shift+cell_size*(n[0]-min_x),y_shift+cell_size*(max_y-n[1]),cell_size,perimeter_color)
	for p in poly:
		draw_cell(cr,x_shift+cell_size*(p[0]-min_x),y_shift+cell_size*(max_y-p[1]),cell_size,main_color)

def draw_poly_list(poly_list,name,main_color = "black",perimeter_color="red", tabular = True):
	cols = 4.0 if tabular else 1.0
	poly_size = 100
	margin = 50
	n = len(poly_list)
	rows = ceil(n/cols)
	ps = cairo.PDFSurface(name+".pdf", cols*poly_size+2*margin	, rows*poly_size+2*margin)
	cr = cairo.Context(ps)
	for i,poly in enumerate(poly_list):
		r,c = divmod(i,cols) if tabular else 0,0
		draw_poly(cr,poly,c*poly_size+margin,r*poly_size+margin, main_color, perimeter_color)
