"""
This is a blank PyCharm project for you to develop in.
Feel free to make any new files that you want to.
"""


import tkinter                          # graphics library
from simpleimage import SimpleImage     # images library


def main():
    # Uncomment the line "tkinter.mainloop()" below if you are using a
    # graphics canvas to draw graphics, so that graphics window appears.
    # You can delete these lines if you are not using a drawing canvas.
    # tkinter.mainloop()
    pass


# This function is provided to you to create a window with a
# canvas that you can use to make drawings.  You are not required
# to use this function in your program, and can modify it or delete
# it, as you like.  We just provide this function for convenience
# should you wish to use it in a program that displays graphics.
def make_canvas(width, height):
    """
    Creates and returns a drawing canvas
    of the given int size, ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('graphics')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


if __name__ == '__main__':
    main()
