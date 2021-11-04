import tkinter
okno = tkinter.Tk()

textak = open('aaa.txt', "r")
#vytvorime premennu textak pomocou ktorej otvorime .txt subor; použijeme funkciu r lebo chceme len čítať subor nie doňho pridávať
y = textak.read()
#vytvorime premennu pomocou ktorej precitame predošle otvorený súbor

# zadefinujeme funkciu ktorá sa má odohrať po tom čo stalčíme button
def otvorsubor():
    print(y)
    #vypíšeme/vytlačíme náš prečítaný súbor
  
   

button = tkinter.Button(okno, text="Otvor subor", command=otvorsubor)
#vytvoríme button, ktorý bude mať za úlohu vypísať súbor pomocou funckie otvorsubor
button.grid(column=2, row=2)
#velkosti buttonu

okno.mainloop()
