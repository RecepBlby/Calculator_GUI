from tkinter import *

def yaz(x): 
    s = len(giris.get())     #indisi arttır
    giris.insert(s,str(x))   #entry text kısmına yerleştir.

hesap = 5
sayi1 = 0

def islemler(x):
    global hesap
    hesap = x
    global sayi1
    sayi1 = float(giris.get())
    print(hesap)
    print(sayi1)
    giris.delete(0,'end') #entry içini temizler birinci sayıdan sonra

sayi2 = 0
def hesapla():
    global sayi2
    sayi2 = float(giris.get())
    print(sayi2)
    global hesap
    sonuc=0
    if(hesap==0):
        sonuc = sayi1 + sayi2
    elif(hesap==1):
        sonuc = sayi1 - sayi2
    elif (hesap == 2):
        sonuc = sayi1 * sayi2
    elif (hesap == 3):
        sonuc = sayi1 / sayi2
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))

pencere = Tk()
pencere.geometry("250x300")
pencere.title("CALCULATOR")

#TEXT ALANI
#HESAP MAKİLERİNDE SAĞDAN YAZMAK İÇİN JUSTIFY HIZALAMA
giris = Entry(font="Verdana 14 bold",width=15,justify=RIGHT)
giris.place(x=20,y=16)

#Butonları tutması amaçlı boş dizi oluştur.
b = []
#1-9 arası butonları oluştur.
for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))
    
sayac=0  #9adet buton var, 3x3 döngü olduğundan sayac kullanalım.
#3x3 Matrix oluşturup, butonları yerleştir
for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1

islem = []
for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold",width=2,command=lambda x=i:islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0,4):
    islem[i].place(x=170,y=50+50*i)

# "0" "." "="
sifirb = Button(text="0",font="Verdana 14 bold",command=lambda x=0:yaz(x))
sifirb.place(x=20,y=200)
noktab = Button(text=".",font="Verdana 14 bold",width=2,command=lambda x=".":yaz(x))
noktab.place(x=70,y=200)
esittirb = Button(text="=",fg ="RED",font="Verdana 14 bold",command=hesapla)
esittirb.place(x=120,y=200)

pencere.mainloop()