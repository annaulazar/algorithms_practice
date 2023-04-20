from datetime import date
import json

def date_from_str(str):
    """
    функция получает строку в виде "дд.мм.гггг" и возвращает дату
    """
    return date(*map(int, str.split('.')[::-1]))


params = {}
with open("input.txt", encoding='utf-8') as file:
    s = file.readline()
    for line in file:
        line = line.split()
        params[line[0]] = line[1]
prod = json.loads(s)

#print(prod)
#print(params)

res_prod = []
for p in prod:
    if (int(params['PRICE_GREATER_THAN']) <= p['price'] <= int(params['PRICE_LESS_THAN'])
     and p['name'].lower().find(params['NAME_CONTAINS']) > -1
     and date_from_str(params['DATE_AFTER']) <= date_from_str(p['date']) <= date_from_str(params['DATE_BEFORE'])):
        res_prod.append(p)
res_prod.sort(key=lambda x: x['id'])
print(res_prod)      
