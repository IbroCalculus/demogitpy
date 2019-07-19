import tkinter as tk

root = tk.Tk()
nameL = tk.Label(text='I am\nA python programmer, and an\nEngr by Profession.',
                 borderwidth=10,
                 justify = tk.LEFT,
                 relief = "groove",
                 height = 6,
                 width = 40,
                 anchor = tk.NW,
                 bg='black',
                 fg='red',
                 )
nameL.pack()

val = 0

def pressCom():
    global val
    if val == 0:
        nameL['bg'] = 'white'
        nameL['anchor'] = tk.SE
        press['bg'] = 'green'
        press['fg'] = 'blue'
        press['text'] = 'Swap Back'
        nameL['justify'] = tk.RIGHT
        val = 1
    elif val == 1:
        nameL['bg'] = 'black'
        nameL['anchor'] = tk.NW
        press['bg'] = 'blue'
        press['fg'] = 'green'
        press['text'] = 'Press Here'
        nameL['justify'] = tk.LEFT
        val = 0
    

press = tk.Button(root, text='Press Here',
                  highlightcolor = 'yellow',
                  width=10, command=pressCom)
press.pack()
root.mainloop()
