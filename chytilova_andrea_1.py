import json
slovnik = {}
with open('alice.txt', encoding = 'utf-8') as file:
    text = file.read()
    text_maly = text.lower()
for znak in text_maly:
    if znak in slovnik:
        slovnik[znak] += 1
    else:
        slovnik[znak] = 1
slovnik.pop(" ")
slovnik.pop("\n")       
serazeny = dict(sorted(slovnik.items()))
for znak, cetnost in serazeny.items():
    print(f"{znak}: {cetnost}")

with open('ukol1_output.json', mode='w', encoding='utf-8') as output:
    json.dump(serazeny,output, ensure_ascii=False,indent=4)