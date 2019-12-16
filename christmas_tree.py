# pylint: disable=unused-wildcard-import

import math
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import Tk, Canvas, Frame, BOTH

TREE_SIDE_LEN = 1.5
GUI_UNIT = 400
TREE_INITIAL_POINT = (400, 20)

def tree(TREE_ANGLE, TREE_SEGMENTS):
    left_bottom_point = (
        TREE_INITIAL_POINT[0] - math.sin(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT,
        TREE_INITIAL_POINT[1]+math.cos(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT)
    right_bottom_point = (
        TREE_INITIAL_POINT[0] + math.sin(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT, 
        TREE_INITIAL_POINT[1]+math.cos(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT)
    top_point = TREE_INITIAL_POINT
    return top_point, right_bottom_point, left_bottom_point, top_point


def tree_point(TREE_ANGLE, TREE_SEGMENTS):
    left_bottom_point = (
        math.sin(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT, 
        math.cos(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT)
    right_bottom_point = (
        math.sin(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT, 
        math.cos(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT)
    #top_point = TREE_INITIAL_POINT
    left_i_points = ()
    right_i_points = ()
    for i in range(1,TREE_SEGMENTS):
        left_i_points +=(
            TREE_INITIAL_POINT[0] - left_bottom_point[0]/TREE_SEGMENTS*(i), 
            TREE_INITIAL_POINT[1] + left_bottom_point[1]/TREE_SEGMENTS*(i))
    for i in range(1,TREE_SEGMENTS):
        right_i_points +=(
            TREE_INITIAL_POINT[0] + right_bottom_point[0]/TREE_SEGMENTS*i, 
            TREE_INITIAL_POINT[1] + right_bottom_point[1]/TREE_SEGMENTS*i)
    i_points = ()
    for i in range(TREE_SEGMENTS-1):
        i_points += (right_i_points[2*i], right_i_points[2*i+1])
        #i_points += right_i_points[2*i+1]
        i_points += (left_i_points[2*i], left_i_points[2*i+1])
        #i_points += left_i_points[2*i+1]
    #return top_point, right_bottom_point, left_bottom_point, top_point
    i_points += (
        TREE_INITIAL_POINT[0] + math.sin(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT, 
        TREE_INITIAL_POINT[1]+math.cos(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT)
    return i_points

def tree_chain(TREE_ANGLE, TREE_SEGMENTS):
    tree_chain_points = tree_point(TREE_ANGLE, TREE_SEGMENTS) + (

        TREE_INITIAL_POINT[0] - math.sin(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT,
        TREE_INITIAL_POINT[1]+math.cos(math.radians(TREE_ANGLE/2))*TREE_SIDE_LEN*GUI_UNIT)
    chain_len = 0
    for i in range(int(len(tree_chain_points)/2.0)-1):
        a = (tree_chain_points[2*i], tree_chain_points[2*i+1])
        b = (tree_chain_points[2*i+2], tree_chain_points[2*i+3])
        chain_len += math.sqrt( ((a[0]-b[0])**2)+((a[1]-b[1])**2) )

    return chain_len/GUI_UNIT



class Controls(Frame):

    def __init__(self, drawings):
        super().__init__()
        self.drawings = drawings

    def setup_iu(self):

        self.pack(fill=BOTH, expand=0)

        self.lbl = Label(self, text="What is the angle in your tree?")
        self.lbl.grid(column=0, row=1)
        
        self.txt = Entry(self, width=10, textvariable=IntVar(value=45)) 
        self.txt.grid(column=1, row=1)

        lbl2 = Label(self, text="How many segments do you want?")
        lbl2.grid(column=0, row=0)

        self.spin = Spinbox(self, from_=0, to=100, width=5, textvariable=IntVar(value=4))
        self.spin.grid(column=1,row=0)

        self.btn = Button(self, text="Show", command=self.clicked)
        self.btn.grid(column=2, row=1)



    def clicked(self):
        tree_angle = int(self.txt.get())
        TREE_SEGMENTS = int(self.spin.get())
        self.drawings.print_tree(tree_angle, TREE_SEGMENTS)
        chain = tree_chain(tree_angle, TREE_SEGMENTS)
        print(chain)
        messagebox.showinfo('Chain tree length', str(chain))



class Drawing(Frame):

    def __init__(self):
        super().__init__()

    def setup_ui(self):
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    def print_tree(self, tree_angle, TREE_SEGMENTS):
        self.canvas.delete("all")
        self.canvas.create_polygon(
            *tree(tree_angle, TREE_SEGMENTS),
            outline="darkgreen",
            fill="#381",
            width=8)
        self.canvas.create_line(
            *tree_point(tree_angle, TREE_SEGMENTS),
            fill= "darkgreen",
            width=8)
        



def main():

    root = Tk()
    root.title("Lines")
    _drawing = Drawing()
    _controls = Controls(_drawing)
    _controls.setup_iu()
    _drawing.setup_ui()
    root.geometry("800x700")

    
    root.mainloop()


if __name__ == '__main__':
    main()





(329.1171425740336, 128.6666554575202, 
212.64857227789923, 345.9999663725606, 
358.23428514806716, 237.33331091504039, 
241.76571485193284, 237.33331091504039, 
387.35142772210077, 345.9999663725606, 
270.8828574259664, 128.6666554575202, 
300, 20)






