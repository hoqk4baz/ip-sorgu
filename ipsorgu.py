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


def dark_ipinfo():
    dark=requests.get(f'https://ipapi.co/{ipadress}/json/')
    res=dark.json()
    ip_data = {
        "İP ADRESİ": ipadress,
        "ŞEHİR": res.get("city"),
        "BÖLGE": res.get("region"),
        "ÜLKE": res.get("country_name"),
        "ÜLKE KODu": res.get("country_code"),
        "SAAT DİLİMİ": res.get("utc_offset"),
        "POSTA KODU": res.get("postal"),
        "DİL": res.get("languages"),
        "PARA BİRİMİ": res.get("currency_name")
    }
    return ip_data

print("")
print(dark_ipinfo())
