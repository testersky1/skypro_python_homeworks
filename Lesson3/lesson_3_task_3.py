from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "20", "10")

mail = Mailing(to_address, from_address, 350, "AB123456789CD")

print(mail)