print("daar gaan we")
print("nog een statement!!!")

class Gemeente:
    aantalinwoners = 0
    stadsnaam = "ntb"
    def opgavegerichtwerken(_self):
        print("wij ", _self.stadsnaam, "werken oggricht")

gemeente1 = Gemeente()
gemeente1.aantalinwoners = 15000
gemeente1.stadsnaam = input("Hoe heet jouw stad?")

print("Gemeente1: ", gemeente1.aantalinwoners, " inwoners")
print("De naam is: ", gemeente1.stadsnaam)

gemeente1.opgavegerichtwerken()