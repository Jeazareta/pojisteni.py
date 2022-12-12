from evidence import Evidence
from system import System

sys = System()
ev = Evidence()

if __name__ == "__main__":

    while True:

        sys.vypis_uvod()
        operace = input("")
        if operace == "1":
            ev.pridat_pojistence()
            input("Vaše data jsou uložena. Pokračujte klávesou Enter.")
            print()
        elif operace == "2":
            ev.zobraz_vsechny()
            input("Pokračujte klávesou Enter.")
            print()
        elif operace == "3":
            ev.vyhledani_pojistence()
            input("Pokračujte klávesou Enter.")
            print()
        else:
            exit(0)
