import tkinter as tk

def clear_fn():
    text.delete('1.0', text.index('1.0 lineend')) # tk.END) # first index, last index

def red_fn():
    ranges = text.tag_ranges(tk.SEL) # 'sel'
    if ranges:
        text.tag_add('red', ranges[0], ranges[1]) # *ranges)

def make_controls(master):
    frame = tk.Frame(master)
    root.img = tk.PhotoImage(file='./smiley.png')
    clear_but = tk.Button(frame, image=root.img, text="Clear", compound=tk.TOP, command=clear_fn)
    clear_but.pack(side=tk.LEFT)
    red_but = tk.Button(frame, text='Red', command=red_fn)
    red_but.pack(side=tk.LEFT)
    return frame

def make_text(master):
    text = tk.Text(master)
    text.tag_config('red', foreground='red')
    text.pack()
    return text

root = tk.Tk()
root.title('Editor')

text = make_text(root)
text.pack(side=tk.TOP)

controls = make_controls(root) # container
controls.pack(side=tk.TOP)

root.mainloop()
