from random import randint 

tutulan_sayi=randint(1,10)
hak=3
print(tutulan_sayi)
while True:
    tahmin_sayi=int(input("1-10 Arasında Sayı Tahmininizi Yazınız:"))
    
    if hak==0:
        print("Hakkınız Kalmadı")
        print(tutulan_sayi)
        break
    else:
        hak-=1
        if tahmin_sayi==tutulan_sayi:
           print("Tahmininiz Doğru Tebrikler")
           break

        elif tutulan_sayi>tahmin_sayi:
            print("Daha büyük bir sayı giriniz")
        elif tutulan_sayi<tahmin_sayi:
            print("Daha Küçük Bir Sayı Giriniz")
    

           