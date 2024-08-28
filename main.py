meme_dict = {
            "CRINGE": "(Garip ya da utandırıcı bir şey)",
            "LOL": "(Komik bir şeye verilen cevap)",
            "lol": "(Komik bir şeye verilen cevap)",
            "cringe": "(Garip ya da utandırıcı bir şey)",
            
            }
            
word = input("Bana Bir KEY Ver Önerim meme Sözcüklerini dene): ")
if word in meme_dict.keys(): 
    print(meme_dict[word], "bunu yazdın")
else:
    print("ben bunu bilmiyorum")
