times=float(input("otoparkta ne kadar süre kaldınız:"))
car_type=input("Araç Tipiniz Nedir(otomobil,motor,kamyon):")
vip=input("VIP misiniz? (e/h):")
no_ticket=input("Kayıp Bilet Var mı? (e/h):") 
if car_type=="otomobil":
    clock_price=30
elif car_type=="kamyon":
    clock_price=60
elif car_type=="motor":
    clock_price=20
else:
  print("hatalı giriş! araç tipi bulunamadı")

if times<=1 and times>=0: 
    total_price=0
    print( "1 saatten az kaldığınız için ücret ödemiyorsunuz")
elif times>10:
    total_price=(times*clock_price)*1.20
    print("%20 uzun süre zammı uygulandı")
    print(total_price)  
elif times>1 :
    if vip=="e" and no_ticket=="h" :
        total_price=(times*clock_price)*0.70
        print(total_price) 
    elif vip=="h":
        total_price=times*clock_price
        print("Toplam Tutar:",total_price)
    elif no_ticket=="e":
         total_price=(times*clock_price)+200
         print("200 lira ceza kesildi!",total_price)
    else:
        print("hatalı bir işlem yaptınız")
else:    
         print("Süre ile ilgili hatalı giriş yaptınız")
         


