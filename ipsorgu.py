import requests
import json

print("  _____             _      ______                ")
print(" |  __ \           | |    |  ____|               ")
print(" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ ")
print(" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |")
print(" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |")
print(" |_____/ \__,_|_|  |_|\_\ |______|_| |_/___\__,_|")
print(" İP İNFO                           TG: @dark_enza")
print(" ----- Gemiler Batınca Acırmı Denizin Canı? -----")
print("")
print("Kişinin İP Adresinden Nereli Olduğunu Bulun ")
print("")

ipadress=input("İP ADRESİ GİR: ")


dark=requests.get(f'https://ipapi.co/{ipadress}/json/')
res=dark.json()
print("")
print("SORGULANAN İP:",ipadress,"\n"+"ŞEHİR:",res.get("city"),"\n"+"BÖLGE:",res.get("region"),"\n"+"ÜLKE:",res.get("country_name"),"\n"+"ÜLKE KODU:",res.get("country_code"),"\n"+"SAAT DİLİMİ:",res.get("utc_offset"),"\n"+"POSTA KODU:",res.get("postal"),"\n"+"DİL:",res.get("languages"),"\n"+"PARA BİRİMİ:",res.get("currency_name"))
    
print("")
print("Sonuçlar Bunlar")
