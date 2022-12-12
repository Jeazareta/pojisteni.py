class Pojistenec:

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor pro pojištěnece s jeho atributy
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """
        Textový výpis pojištěnce

        """
        return f"{self.jmeno}\t {self.prijmeni}\t {self.vek}\t {self.telefon}\t"

