import json
#vazifa -1

data = {"Model" : "Nexia2", "Rang" : "Oq", "Yil":2016, "Narh":10000}
data_json = json.dumps(data)
print(data_json)

#vazifa -2

talaba_json = """{"ism":"Azizbek","familiya":"yusupov","tyil":2008}"""
talaba = json.loads(talaba_json)
print(f"Talabaning ismi: {talaba['ism']}")
print(f"Talabaning familiyasi: {talaba['familiya']}")
print(f"Talabaning yili: {talaba['tyil']}")

#vazifa -3

with open('data.json','w') as f:
    json.dump(data, f)

with open('talaba.json','w') as f:
    json.dump(talaba,f)
