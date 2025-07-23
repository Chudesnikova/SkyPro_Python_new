from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "Iphone 15 ProMax", "+79031234567"),
    Smartphone("Honor", "GT Pro", "+79012345678"),
    Smartphone("Huawei", "Nova 14", "+79023456789"),
    Smartphone("LG", "Wing", "+79045678901"),
    Smartphone("Motorola", "Edge", "+79056789012")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
