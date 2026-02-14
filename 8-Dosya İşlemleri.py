import json
with open("data.json","r") as file:
    data=json.load(file)
with open("data.json","w", encoding="utf-8") as file:
        kitapAdi=input("Kitap Adınızı Giriniz:")
        yazar=input("Yazarınızı Giriniz")
        fiyat=int(input("Fiyatınızı Giriniz:"))
        yayın_tarihi=input("Yayın Tarihini Giriniz:")
        yayıncı=input("Yayıncınızı Giriniz:")
        kategori=input("Kategorinizi Giriniz:")
        müsaitlik=bool(input("Müsaitliğinizi Giriniz:"))
        data.append(
        {
            "kitap_adi":kitapAdi,
            "yazar":yazar,
            "fiyat":fiyat,
            "yayın_tarihi":yayın_tarihi,
            "yayıncı":yayıncı,
            "kategori":kategori,
            "müsaitlik":müsaitlik
        }

    ) 

        json.dump(data,file,indent=4,ensure_ascii=False)


        
     