import tkinter as tk
#Defines Colour Visualizer for Preview and Sliders
def colourvis(_=None):
    #Grabs the values from RGB sliders
    r,g,b = red.get(), green.get(), blue.get()
    #Converts those into an Hexcode useable by tkinter
    hex_colour = hexformatter(r, g, b)
    hue.config(troughcolor=hexformatter(*rgb(hueVar.get(), 100, 100)))
    sat.config(troughcolor=hexformatter(*rgb(hueVar.get(),satVar.get(),100)))
    val.config(troughcolor=hexformatter(*rgb(0, 0, valVar.get())))

    #calls update functions
    update_rgb_scales(r,g,b)
    updatevisualizer(hex_colour)
#Helper Function - converts the rgb values into hexcode
def hexformatter(r, g, b):
    r = max(0, min(255, int(r)))
    g = max(0, min(255, int(g)))
    b = max(0, min(255, int(b)))
    return f'#{r:02x}{g:02x}{b:02x}'
#Helper Function - Updates the scales backgrounds so they only show how much of each colour they are using
def update_rgb_scales(r,g,b):
    red.config(troughcolor= f'#{r:02x}0000')
    green.config(troughcolor= f'#00{g:02x}00')
    blue.config(troughcolor= f'#0000{b:02x}')
#Helper Function -updates visualizer with the hexcode
def updatevisualizer(hexcode):
    preview.config(bg=hexcode)
#Converting Tool from RGB to HSV
def hsv(r,g,b):
    r = r / 255
    g = g / 255
    b = b / 255
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
    s = 0 if Cmax == 0 else (delta / Cmax) * 100
    v = Cmax * 100

    hueVar.set(round(h, 2))
    satVar.set(round(s, 2))
    valVar.set(round(v, 2))
    return h,s,v
#Converting from HSV values to RGB
def rgb(h,s,v):
    s /= 100
    v /= 100
    C = v * s
    X = C * (1 - abs((h / 60) % 2 - 1))
    m = v - C
    if 0 <= h < 60:
        Rp, Gp, Bp = C, X, 0
    elif 60 <= h < 120:
        Rp, Gp, Bp = X, C, 0
    elif 120 <= h < 180:
        Rp, Gp, Bp = 0, C, X
    elif 180 <= h < 240:
        Rp, Gp, Bp = 0, X, C
    elif 240 <= h < 300:
        Rp, Gp, Bp = X, 0, C
    else:
        Rp, Gp, Bp = C, 0, X

    r = int((Rp + m) * 255)
    g = int((Gp + m) * 255)
    b = int((Bp + m) * 255)
    return r,g,b
#update functions allows for real-time colour change
#hsv sliders moving changes rgb
def updatehsv():
    r,g,b = rgb(hueVar.get(), satVar.get(), valVar.get())
    # updates the R,G,B sliders
    red.set(r)
    green.set(g)
    blue.set(b)
    hueText.set(f'{hueVar.get()}°')
    satText.set(f'{satVar.get()}%')
    valText.set(f'{valVar.get()}%')
    colourvis()
#rgb sliders moving changes hsv
def updatergb():
    h,s,v = hsv(red.get(), green.get(), blue.get())
    hue.set(h)
    sat.set(s)
    val.set(v)
    hueText.set(f'{hueVar.get()}°')
    satText.set(f'{satVar.get()}%')
    valText.set(f'{valVar.get()}%')
    colourvis()
#Creating the window
root = tk.Tk()
#Minimum window size
root.minsize(450, 650)
root.title("RGB to HSV Converter")
tk.Label(root, text="RGB to HSV Converter",font= ("TkDefaultFont",18, "bold")).pack()
#creates the hsl values for calculations and hsl values for text output
hueVar,satVar,valVar = tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar()
hueText,satText,valText = tk.StringVar(), tk.StringVar(),tk.StringVar()
#RGB sliders
red = tk.Scale(root, from_=0, to=255, orient="horizontal", label= 'Red', foreground= '#ffffff', background= "dark grey", command=lambda v: updatergb(), borderwidth=5, relief="ridge")
red.pack(fill="x",padx= 20 , pady = 10)
green = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Green", foreground= '#ffffff', background= "dark grey", command=lambda v: updatergb(), borderwidth=5, relief="ridge")
green.pack(fill="x",padx= 20 , pady = 10)
blue = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Blue", foreground= '#ffffff', background= "dark grey", command=lambda v: updatergb(), borderwidth=5, relief="ridge")
blue.pack(fill = "x", padx= 20 , pady= 10)
#HSV Sliders
hue = tk.Scale(root, from_=0, to=360, orient="horizontal", label= 'Hue', foreground= '#ffffff', background= "dark grey", variable=hueVar, command=lambda v: updatehsv(), borderwidth=5, relief="ridge")
hue.pack(fill="x",padx= 20 , pady = 10)
sat = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Saturation", foreground= '#ffffff', background= "dark grey",variable = satVar, command=lambda v: updatehsv(), borderwidth=5, relief="ridge")
sat.pack(fill="x",padx= 20 , pady = 10)
val = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Value", foreground= '#ffffff', background= "dark grey", variable= valVar,command=lambda v: updatehsv(), borderwidth=5, relief="ridge")
val.pack(fill = "x", padx= 20, pady = 10)
#HSV values as text for easy reading
hueRow = tk.Frame(root)
tk.Label(hueRow, text="Hue: ").pack(side = 'left')
tk.Label(hueRow, textvariable= hueText, font= 'bold').pack(side ='left')
hueRow.pack()
satRow = tk.Frame(root)
tk.Label(satRow, text="Saturation: ").pack(side ='left')
tk.Label(satRow,textvariable= satText).pack(side ='left')
satRow.pack()
valRow = tk.Frame(root)
tk.Label(valRow, text="Value: ").pack(side = 'left')
tk.Label(valRow,textvariable= valText).pack(side ='left')
valRow.pack()
#Colour Visualizer
tk.Label(root, text="Colour Preview",font= ("TkDefaultFont",18, "bold")).pack()
preview = tk.Label(root, borderwidth=2,relief="solid", height=150)
preview.pack(fill= "both", padx= 5, pady=5, expand=True)
colourvis(None)
root.mainloop()
