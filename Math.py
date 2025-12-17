import tkinter as tk
#Defines Colour Visualizer
def colourVis(self):
    r = red.get()
    g = green.get()
    b = blue.get()
    hex_colour = f'#{r:02x}{g:02x}{b:02x}'
    red.config(background= f'#{r:02x}0000')
    green.config(background= f'#00{g:02x}00')
    blue.config(background= f'#0000{b:02x}')
    preview.config(bg=hex_colour)

#Defines Converting Tool
def hue():
    r = red.get() / 255
    g = green.get() / 255
    b = blue.get() / 255
    Cmax = max(r,g,b)
    Cmin = min(r,g,b)
    delta = Cmax - Cmin

    if delta == 0:
        h = 0
    elif Cmax == r:
        h = (60 * ((g - b) / delta)) % 360
    elif Cmax == g:
        h = (60 * ((b - r) / delta + 2))
    else:
        h = (60 * ((r - g) / delta + 4))
    hueVar.set(round(h,2))

def saturation():
    r = red.get() / 255
    g = green.get() / 255
    b = blue.get() / 255
    Cmax = max(r, g, b)
    Cmin = min(r, g, b)
    delta = Cmax - Cmin
    s = 0 if Cmax == 0 else (delta / Cmax) * 100
    satVar.set(round(s,2))

def value():
    r = red.get() / 255
    g = green.get() / 255
    b = blue.get() / 255
    Cmax = max(r, g, b)
    v = Cmax * 100
    valVar.set(round(v,2))

root = tk.Tk()
root.title("RGB to HSV Converter")
#RGB sliders
red = tk.Scale(root, from_=0, to=255, orient="horizontal", label= 'Red', foreground= '#ffffff',  command=colourVis)
red.set(0)
red.pack(fill="x",padx= 10)
green = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Green", foreground= '#ffffff', command=colourVis)
green.set(0)
green.pack(fill="x",padx= 10)
blue = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Blue", foreground= '#ffffff', command=colourVis)
blue.set(0)
blue.pack(fill = "x", padx= 10)

convert = tk.Button(root, text="Convert to HSV", command=lambda:[hue(),saturation(),value()], width = 10).pack()

hueVar = tk.StringVar()
satVar = tk.StringVar()
valVar = tk.StringVar()

tk.Label(root, text="Hue (In Degrees)").pack()
tk.Label(root,textvariable= hueVar).pack()
tk.Label(root, text="Saturation (Percentage)").pack()
tk.Label(root,textvariable= satVar).pack()
tk.Label(root, text="Value (Percentage)").pack()
tk.Label(root,textvariable= valVar).pack()

tk.Label(root, text="Colour Preview", ).pack()
preview = tk.Label(root, borderwidth=2,relief="solid")
preview.pack(fill= "both", padx= 5, pady=5, expand=True)

colourVis(None)
root.mainloop()
