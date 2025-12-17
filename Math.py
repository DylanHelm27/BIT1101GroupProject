#Using Tkinter
import tkinter as tk
# Colour Visualizer for Preview and Sliders
def colourvis(_=None):
   #Grabs the values from RGB sliders
   r,g,b = red.get(), green.get(), blue.get()
   #Converts those into a Hex-code usable by tkinter
   hex_colour = hexformatter(r, g, b)
   #calls update functions
   updatevisualizer(hex_colour)
#Helper Function - converts the rgb values into hexcode
def hexformatter(r, g, b):
   #sets r,g,b as an int, makes sure the value is not negative and has a max value of 255
   r = max(0, min(255, int(r)))
   g = max(0, min(255, int(g)))
   b = max(0, min(255, int(b)))
   #Returns the formatted Hexcode
   return f'#{r:02x}{g:02x}{b:02x}'
#Helper Function - updates visualizer with the hexcode
def updatevisualizer(hexcode):
   #sets the background of the preview to the hexcode
   preview.config(bg=hexcode)
#Helper Function to update the text with proper formatting
def updatetext(_=None):
   hueText.set(f'{hueVar.get()}°')
   satText.set(f'{satVar.get()}%')
   valText.set(f'{valVar.get()}%')
#Helper Function - Updates the trough colour
def updatetrough(slider,colour):
   slider.config(troughcolor=colour)
#Converting Tool from RGB to HSV
def hsv(r,g,b):
   r = r / 255
   g = g / 255
   b = b / 255
   cmax = max(r,g,b)
   cmin = min(r,g,b)
   delta = cmax - cmin
   if delta == 0:
       h = 0
   elif cmax == r:
       h = (60 * ((g - b) / delta)) % 360
   elif cmax == g:
       h = (60 * ((b - r) / delta + 2))
   else:
       h = (60 * ((r - g) / delta + 4))
   s = 0 if cmax == 0 else (delta / cmax) * 100
   v = cmax * 100


   hueVar.set(round(h, 2))
   satVar.set(round(s, 2))
   valVar.set(round(v, 2))
   return h,s,v
#Converting Tool from HSV to RGB
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
#hsv sliders moving updates rgb sliders
def updatergb(_=None):
   #calculates the rgb from grabbing hsv slider values
   r,g,b = rgb(hue.get(), sat.get(), val.get())
   # updates the R,G,B sliders
   red.set(r)
   green.set(g)
   blue.set(b)
   #Updates the scales backgrounds so they show how much of each colour they are using
   updatetrough(red,f'#{r:02x}0000')
   updatetrough(green,f'#00{g:02x}00')
   updatetrough(blue,f'#0000{b:02x}')
   #updates the HSV text and the colour preview
   updatetext()
   colourvis()
#rgb sliders moving updates hsv sliders
def updatehsv(_=None):
   #calculates the hsv from grabbing rgb slider values
   h,s,v = hsv(red.get(), green.get(), blue.get())
   #sets hue, saturation, and value sliders to the new numbers
   hue.set(h)
   sat.set(s)
   val.set(v)
   #sets the trough colour dynamically
   updatetrough(hue,hexformatter(*rgb(hueVar.get(), 100, 100)))
   updatetrough(sat,hexformatter(*rgb(hueVar.get(),satVar.get(),100)))
   updatetrough(val,hexformatter(*rgb(0, 0, valVar.get())))
   #updates the HSV text and the colour preview
   updatetext()
   colourvis()
#Creates the window
root = tk.Tk()
#Sets minimum window size
root.minsize(450, 650)
#Title for window and title at the top of the page
root.title("RGB to HSV Converter")
tk.Label(root, text="RGB to HSV Converter",font= ("TkDefaultFont",18, "bold")).pack()
#creates the hsv values for calculations and hsv values for text output
hueVar,satVar,valVar = tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar()
hueText,satText,valText = tk.StringVar(), tk.StringVar(),tk.StringVar()
#RGB & HSV sliders created with a dictionary and a for loop to reduce redundancy
sliderDict = {}
Sliders = [('red', 'Red',255, updatehsv),('green', 'Green',255,updatehsv),('blue', 'Blue',255,updatehsv),('hue','Hue',360, updatergb),('sat','Saturation',100,updatergb),('val', 'Value', 100, updatergb)]
for name, label,maxVal, command in Sliders:
   sliderDict[name] = tk.Scale(root, from_=0, to=maxVal, orient="horizontal", label= label, foreground= '#ffffff', background= "dark grey",  command=lambda v, cmd=command: cmd(v), borderwidth=5, relief="ridge")
   sliderDict[name] .pack(fill="x", padx=20, pady=5)
red = sliderDict["red"]
green = sliderDict["green"]
blue = sliderDict["blue"]
hue = sliderDict["hue"]
sat = sliderDict["sat"]
val = sliderDict["val"]
#HSV values as text for easy reference created in a structure & for loop to reduce redundancy
rows = [("Hue:",hueText),("Saturation:",satText),("Value:",valText)]
for name, textVar in rows:
   row = tk.Frame(root)
   tk.Label(row, text=name).pack(side="left")
   tk.Label(row, textvariable= textVar).pack(side="left")
   row.pack()
#Colour Visualizer
tk.Label(root, text="Colour Preview",font= ("TkDefaultFont",18, "bold")).pack()
#Sets minimum height to 150 so preview is not squished on bottom
preview = tk.Label(root, borderwidth=5,relief="ridge", height=150)
preview.pack(fill= "both", padx= 5, pady=5, expand=True)
#Runs colourVis and the main loop
colourvis(None)
root.mainloop()
