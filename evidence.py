from pojisteni import Pojistenec

class Evidence:

    def __init__(self):
        """
        atribut v evidenci
        """
        self.pojistenci = []

    def pridat_pojistence(self):
        """
        metoda vytvoří nového pojišťence

        """
        jmeno = input("Zadejte Vaše křestní jméno: \n").capitalize()
        prijmeni = input("Zadejte Vaše příjmení: \n").capitalize()
        vek = int(input("Zadejte Váš věk: \n"))
        telefon = int(input("Zadejte Vaše telefonní číslo: \n"))
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(novy_pojistenec)

    def zobraz_vsechny(self):
        """
        metoda zobrazí všechny pojištěnce
        """
        for pojistnik in self.pojistenci:
            print(pojistnik)

    def vyhledani_pojistence(self):
        """
        metoda vyhledá pojištěnce podle jeho jména a příjmeni
 
        """
        jmeno = input("Zadejte křestní jméno: \n").capitalize()
        prijmeni = input("Zadejte příjmení \n").capitalize()
        for pojistenec in self.pojistenci:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                print(pojistenec)
