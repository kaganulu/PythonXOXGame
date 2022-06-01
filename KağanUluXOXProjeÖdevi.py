print("""
                                     XOX Oyununa HOŞ GELDİNİZ
          
         Bu projeyi yapma amacım temel olarak öğrendiğimiz bilgilerle ve birkaç araştırma
         sonucu bulduğum bilgileri birleştirerek basit bir XOX oyunu projesi yapmak istedim.
         Kodlarken hem eğlendim hem de yeni şeyler öğrendim. 
         
         
          Kodların yanında açıklama satırları bulunmaktadır.

        

         EK  tkinter kütüphanesinden messagebox kullanılmıştır.

         Options(Seçenekler) menüsü oluşturulmuştur çalıştırıldığında en tepede gözükmektedir
         ve oyun bittiğinde o seçenekten tekrar oyunu başlatmak istiyorsak tıklanır.


           Bu program KAĞAN ULU tarafından yazılmıştır!
           20202425039
      
     
      """)
      
from tkinter import *
from tkinter import messagebox





#Pencere oluşturuldu
root = Tk()
root.title("Kağan ile  XOX  Oyunu ") #Pencere başlığı verildi




tiklandi = True
sayac= 0



def butonlari_devre_disi_birak(): #button devre dışı bırak fonksiyonu tanımlandı
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    
    

def tiklaKazan(): # oyunun çalışma algoritması burada yazıldı
    global kazanan
    kazanan = False
    
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        
       
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        
       
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak() 
        
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        
        
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
    
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        
        
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu X Kazandınız" )
        butonlari_devre_disi_birak()
        
    
        
    # O için
    
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        
       
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        
        
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        
       
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
    
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        
      
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
    elif b3["text"] == "O" and b5["text"] == "0" and b7["text"] == "0":
        
       
        kazanan=True
        messagebox.showinfo("XOX ", "TEBRİKLER! Oyuncu O Kazandınız" )
        butonlari_devre_disi_birak()
        
   
    if sayac == 9 and kazanan == False:
         messagebox.showinfo("Beraberlik","Berabere Kaldınız")
         butonlari_devre_disi_birak()
         
        
        
    
def tikla(b): # Tıkladığımızda X VE O olması için fonksiyon yazıldı
   global tiklandi,sayac
    
    
   if b["text"] == " " and tiklandi == True:
        
        b["text"] = "X"
        tiklandi = False
        sayac +=1
        tiklaKazan()
        
       
   elif b["text"] == " " and tiklandi == False:
        
        b["text"] = "O"
        tiklandi = True
        sayac +=1
        tiklaKazan()
   else:
        print("Buraya tıklandı... Başka yere tıklayın!")
    
    
     
        
    
    
def reset(): # Oluşturulan Options seçeneğinde oyunu resetleme fonksiyonu yazıldı
    global b1,b2,b3,b4,b5,b6,b7,b8,b9 
    global tiklandi,sayac
    tiklandi=True
    sayac=0


#text="" boş bırakıldı çünkü tikla fonksiyonun da text boş ise ve tiklanma durumuna göre X veya O yazıldı
#lambda  fonksiyonu birden fazla veri göndermemize izin verir.

    b1=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b1))
    b1.grid(row = 0, column = 0)

    b2=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b2))
    b2.grid(row = 0, column = 1)

    b3=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b3))
    b3.grid(row = 0, column = 2)

    b4=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b4))
    b4.grid(row = 1, column = 0)

    b5=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b5))
    b5.grid(row = 1, column = 1)

    b6=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b6))
    b6.grid(row = 1, column = 2)

    b7=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b7))
    b7.grid(row = 2, column = 0)

    b8=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b8))
    b8.grid(row = 2, column = 1)

    b9=Button(root,text=" ",width=10,height=5,command=lambda: tikla(b9))
    b9.grid(row = 2, column = 2)


# Menü Oluşturuldu
menubar = Menu(root)
root.config(menu=menubar) 

#Seçenekler menüsü oluşturuldu
options_menu = Menu(menubar, tearoff=False) # tearoff=False menü deki kesik çizgiyi kaldırıyor
menubar.add_cascade(label="Seçenekler",menu=options_menu)
options_menu.add_cascade(label="Oyunu tekrar başlat",command=reset)

reset()

root.mainloop()
