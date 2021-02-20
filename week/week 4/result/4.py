import re, csv

file = open("abc.txt", "r", encoding="utf-8")
text = file.read() 

BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
BIN = re.search(BINPattern, text).group("BIN")

NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"
NDS = re.search(NDSPattern, text).group("NDS")

ZNMPattern = r"\nЗНМ:.*(?P<ZNM>\b[A-Z].+)"
ZNM = re.search(ZNMPattern, text).group("ZNM")

KassaPattern = r"\nКасса\s(?P<Kassa>.*)"
Kassa = re.search(KassaPattern, text).group("Kassa")

ReceiptPattern = r"\nЧек\s(?P<chek>.*)"
Receipt = re.search(ReceiptPattern, text).group("chek")

TimePattern = r"\nВремя:\s(?P<time>.*)"
Time = re.search(TimePattern, text).group("time")

AddressPattern = r"\n(?P<adres>г.*)"
Address = re.search(AddressPattern, text).group("adres")

itemPatternText = r"\n{1}(?P<name>.*)\n{1}(?P<count>.*)x(?P<cost>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)


items = [["БИН", "ЗНМ", "Касса", "Чек", "Наименование товара", "Цена за единицу", "Кол-во", "Сумма", "Дата и Время", "Адрес"]]

for x in re.finditer(itemPattern, text):
    items.append((BIN, ZNM, Kassa, Receipt, x.group("name"), x.group("cost"), x.group("count"), x.group("total1"), Time, Address))

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)

file.close()
