from VirusKodu import *
from tkinter import messagebox
import tkinter as tk


Giris_kismi1 = "Evet"
Giris_kismi2 = "Hayır"

messagebox.showwarning("Dikkat!","Açtığınız uygulama tehlikeli gözüküyor. (Açılan pencereye bak.)")

arayuz = tk.Tk()
arayuz.title("Önemli!")
arayuz.geometry("300x200")


yazi = tk.Label(text="Virüsü çalıştırmak istediğinden emin misin?(Evet/Hayır)")
yazi.place(x=2,y=20)


yazi2 = tk.Label(text="-->")
yazi2.place(x=20,y=50)

y= tk.StringVar()
Giris = tk.Entry(textvariable=y)
Giris.place(x=46,y=50)

def kontrol():
 gir = y.get()

 if gir == Giris_kismi1:
     arayuz.destroy()
     VirusKodu_f()

 if gir == Giris_kismi2:
     arayuz.destroy()


buton = tk.Button(text="Devam Et",command=kontrol)
buton.place(x=180,y=75)





arayuz.mainloop()


