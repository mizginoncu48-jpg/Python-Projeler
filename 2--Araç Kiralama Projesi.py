yas=int(input("kaç yaşındasınız?"))
ehliyet=input("Ehliyetin var mı? e/h:")
hasar=input("Hasar kaydınız:? e/h:")

if yas>=25:
    print("Yaşınız tutuyor")
    if ehliyet=="e":
        print("ehliyetiniz vardır")
        if hasar=="e":
            print("araç kiralanamaz")
            
        else:
            print("depozito ücreti ile kiralanabilir")

    else:
        print("ehliyetiniz yoktur")     


else:
    print("Yaşınız tutmuyor")
   

