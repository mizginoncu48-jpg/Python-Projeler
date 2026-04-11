import json

with open("data.json","r",encoding="utf-8)") as file:
    data=json.load(file) 



while True:
    print("""
    (1)Kitap Ekle
    (2)Kitap Sil
    (3)Kitap vermek
    (4)Kitap Lİstele
    (5)Çıkış

    
    
    """) 

    seçim=input("Seçiminizi Yapınız:")
     
    if seçim=="1":
        with open("data.json","w",encoding="utf-8") as file:
            kitap_adi=input("Kitap Adınızı Giriniz:")
            yazar=input("Yazarınızı Giriniz:")
            fiyat=int(input("Fiyatınızı Giriniz:"))
            yayın_tarihi=input("Yayın Tarihinizi Giriniz:")
            yayıncı=input("Yayıncınızı Giriniz:")
            kategori=input("Kategorinizi Giriniz")
            müsaitlik=bool(input("Müsaitliğinizi Giriniz:"))

            data.append({
                "kitap_adi":kitap_adi,
                "yazar":yazar,
                "fiyat":fiyat,
                "yayın_tarihi":yayın_tarihi,
                "yayıncı":yayıncı,
                "kategori":kategori,
                "müsaitlik":müsaitlik
            })

        

            json.dump(data,file,indent=4,ensure_ascii=False)
            

    elif seçim=="2":
        with open("data.json","w", encoding="utf-8")as file:
            kitap_adi=input("Silinecek Kitap Adını Giriniz:")
            for kitap in data:
                if kitap["kitap_adi"]==kitap_adi:
                    data.remove(kitap)
                    break
                else:
                    print("Bu kitap Bulunamadı")



    elif seçim=="4":
        for kitap in data:
            print(f"Kitap Adı:,kitap[kitap_adi]")
            print("yazar:",kitap["yazar"]) 
            if kitap["müsaitlik"]:
                print("müsaitlik:Evet")
            else:
                print("Müsaitlik:Hayır")
            print("-"*50)
