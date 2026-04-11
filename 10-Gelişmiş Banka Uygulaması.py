import json
from pickle import FALSE
import random
from sys import float_repr_style



with open ("bankamatik.json","r", encoding="utf-8")as file:
    data=json.load(file)

    while True:
      mail=input("Mail Adresinizi Giriniz")
      giris=False

      for user in data:
        if user["mail"]==mail:
          password=input("Şifrenizi Giriniz:")
          if user["sifre"]==password:
            print("Giriş Başarılı")
            giris=True
            break 
          else:
            print("Şifreniz YanlIŞ")
            giris=False
            break 
      if giris==False:
        secim=input("Yeni kullanıcı oluşturmak istiyor musunuz?(e/h)")
        if secim=="e":
          new_mail=input("Mail Adresinizi Giriniz:")
          new_password=input("Şifrenizi Giriniz:")
          hesap_var=False
          for user in data:
            if user["mail"]==new_mail:
              print("Bu mail Adresi zaten Kullanılıyor")
              hesap_var=True 
              break
            else:
              with open("bankamatik.json","w",encoding="utf-8")as file:
                data.append({
                  "mail":new_mail,
                  "sifre":new_password,
                  "bakiye":{
                    "TL":0,
                    "USD":0,
                    "EUR":0,
                    "GOLD":0                  

                  }
                })

                json.dump(data,file,indent=4,ensure_ascii=False)
                print("hesap oluşturuldu")
                

    



        