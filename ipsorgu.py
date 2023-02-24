import requests

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

def get_location():
    response = requests.get(f'https://ipapi.co/{ipadress}/json/').json()
    location_data = {
        "İP ADRESİ": ipadress,
        "ŞEHİR": response.get("city"),
        "BÖLGE": response.get("region"),
        "ÜLKE": response.get("country_name"),
        "ÜLKE KODu": response.get("country_code"),
        "SAAT DİLİMİ": response.get("utc_offset"),
        "POSTA KODU": response.get("postal"),
        "DİL": response.get("languages"),
        "PARA BİRİMİ": response.get("currency_name")
    }
    return location_data


print(get_location())
