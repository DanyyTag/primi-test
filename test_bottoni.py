import tkinter as tk

root = tk.Tk()

root.title("Il Mio Fantastico Bot")

firsr=1 

def aggiungi_bottone():
    print("Ciao2!")
    global firsr
    if firsr == 1:
     tk.Button(root, text="Nuovo Bottone", command=lambda: print("Ciao3!")).pack()
     firsr=0




tk.Button(root, text="Clicca", command=lambda: print("Ciao!")).pack()
tk.Button(root, text="Clicca2", command=aggiungi_bottone).pack()







root.mainloop()
