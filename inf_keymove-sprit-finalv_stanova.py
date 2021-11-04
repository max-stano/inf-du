from tkinter import *
tk = Tk()
platno = Canvas(tk, width=600, height=800)
platno.pack()

current_image = PhotoImage(file='C:/Users/Jana/Documents/max skola/inf seminar/tkinter/sprites1.gif') 
image_id = platno.create_image(5, 5, image=current_image, anchor=NW) #image_id bude ta postavička ktoru momentalne ukazuje
other_image = PhotoImage(file='C:/Users/Jana/Documents/max skola/inf seminar/tkinter/sprites2.gif')

def zmena(): #vytvoríme fukciu pomocou ktorej sa budu menit obrázky
    global current_image, other_image, image_id #platí to na celý kod
    x, y = platno.coords(image_id) 
    platno.delete(image_id)#vymažeme momentálny obrázok
    image_id = platno.create_image(x, y, image=other_image, anchor=NW) #nahradíme ho dalším obrázkom
    current_image, other_image = other_image, current_image
   
    
def pohyb(event): #vytvorime funkciu pohyb pomocou ktorej ked sa tukne istá kláves stane sa istý akcia
    if event.keysym == 'Up': #stalčíme tlačíko up
        platno.move(image_id, 0, -4) #momentálny obrázok sa posunie hore o 4 pixeli
        zmena()#a zároveň sa zmení obrázok
    elif event.keysym == 'Down':
        platno.move(image_id, 0, 4)
        zmena()
    elif event.keysym == 'Left':
        platno.move(image_id, -4, 0)
        zmena()
    elif event.keysym == 'Right':
        platno.move(image_id, 4, 0)
        zmena()

platno.bind_all('<KeyPress-Up>', pohyb)
platno.bind_all('<KeyPress-Down>', pohyb)
platno.bind_all('<KeyPress-Left>', pohyb)
platno.bind_all('<KeyPress-Right>', pohyb)


    
tk.mainloop()
