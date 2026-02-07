kullanicilar={
    "Kerem":{"sifre":"123","bakiye":160},
    "berivan":{"sifre":"6057","bakiye":20000},
    "mizgin":{"sifre":"1946","bakiye":10000}
}
username=input("kullanici adinizi giriniz")
if username in kullanicilar: 
    hak=3
    while hak>0:
        sifre=input("Şifrenizi giriniz")
        if sifre==kullanicilar[username] ["sifre"]:
            print("hesaba giriş yapıldı")
            break
        else:
            print("şifreniz yanlış")
            hak=hak-1

    if hak==0:
        print("Kartınız Bloke Olmuştur Hayırlı Uğurlu Olsun") 
    else:

        print("""
        (1)Bakiye Görüntüle
        (2)Para Çek
        (3)Para Yatırma
        (4)Çıkış
        Seçiminizi Yapınız:
        """)

        seçim=input("Seçiminizi Yapınız:")
        if seçim=="1":
            bakiye=kullanicilar[username]["bakiye"] 
            print(bakiye)

        
        elif seçim=="2":
            miktar=int(input("kaç tl para çekmek istiyorsunuz?"))
            bakiye=kullanicilar[username]["bakiye"]

            if miktar<=bakiye:
                bakiye=bakiye-miktar

            bakiye=kullanicilar[username]["bakiye"]

            print=("Kalan Bakiyeniz:",bakiye)

            else:
            print("Bakiyeniz yeterli Değil")
        elif seçim=="3":

            miktar=(input("Kaç para Yatıracaksınız?:"))
            bakiye=bakiye+miktar
            print("Toplam Bakiyeniz",bakiye)










        

