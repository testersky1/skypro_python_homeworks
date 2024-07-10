
from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79123456701"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79123456702"))
catalog.append(Smartphone("Google", "Pixel 6", "+79123456703"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79123456704"))
catalog.append(Smartphone("Sony", "Xperia 5", "+79123456705"))

for phone in catalog:
    print(phone)
