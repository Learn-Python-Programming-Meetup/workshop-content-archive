import tkinter as tk

def canvas_draw(event):
    print(event)
    idx = canvas.create_line(root.start[0], root.start[1], event.x, event.y, tags="drawn")
    root.start = event.x, event.y
    return

def canvas_press1(event):
    print(event)
    root.start = event.x, event.y

def canvas_release1(event):
    print(event)
    root.start = None

def clear_fn():
    canvas.delete("drawn")

def create_menu(master):
    menubar = tk.Menu(master)
    file_m = tk.Menu(menubar, tearoff=0)
    file_m.add_command(label="Clear", command=clear_fn)
    menubar.add_cascade(menu=file_m, label="File")
    menubar.add_cascade(menu=None, label="Help")
    return menubar

def make_controls(master):
    frame = tk.Frame(master)
    clear_but = tk.Button(frame, text="Clear", command=clear_fn)
    clear_but.pack(side=tk.LEFT)
    return frame

def make_canvas(master):
    canvas = tk.Canvas(root, background='wheat', relief=tk.SOLID, bd=2)
    canvas.bind('<Button-1>', canvas_press1)
    canvas.bind('<ButtonRelease-1>', canvas_release1)
    canvas.bind('<B1-Motion>', canvas_draw)
    return canvas

root = tk.Tk()
root.title('Drawing')

menubar = create_menu(root)
root.config(menu=menubar)

canvas = make_canvas(root)
controls = make_controls(root)
canvas.grid(row=0, column=0)
controls.grid(row=1, column=0)

root.mainloop()
