from adress import Adress
from mailing import Mailing

to_adress = Adress("135795", "Москва", "Ленина", "12", "21")
from_adress = Adress("426846", "Казань", "Пушкина", "13", "31")

mailing = Mailing(to_adress, from_adress, 1234, "AB321654")
print(f"Отправление №{mailing.track} из г. {mailing.from_address.city}, ул. {mailing.from_address.street}, д. {mailing.from_address.house} - {mailing.from_address.apartment} в г. {mailing.to_address.city}, ул. {mailing.to_address.street}, д. {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} руб.")