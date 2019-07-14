import sqlite3
db = sqlite3.connect("Kitaplar.sqlite")

imlec = db.cursor()

menu="""
[1] Kitap Ara
[2] Yazar Ara
"""
print(menu)
islem=input("işleminiz: ")

if islem =="1":
    isim = input("Kitap Adı: ")
    sorgu = "SELECT * FROM 'kitaplik' WHERE kitap = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
if islem =="2":
    isim = input("Yazar Adı: ")
    sorgu = "SELECT * FROM 'kitaplik' WHERE yazar = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
db.close()
