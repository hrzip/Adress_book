import json

DATOTEKA_ADRESARA = "adresar.json"

def ucitaj_podatke() -> dict:
    """
    Učitava podatke iz JSON datoteke. Ako datoteka ne postoji ili je oštećena, vraća prazan adresar.

    Returns:
        dict: Podaci o kontaktima iz JSON datoteke ili prazan adresar.
    """
    pass

def spremi_podatke(podaci: dict) -> None:
    """
    Spremi podatke u JSON datoteku.

    Args:
        podaci (dict): Podaci koji će biti pohranjeni u datoteku.
    """
    pass

def provjeri_telefon(telefon: str) -> bool:
    """
    Provjerava je li telefon sastavljen samo od brojki.

    Args:
        telefon (str): Broj telefona.

    Returns:
        bool: True ako telefon sadrži samo brojke, inače False.
    """
    pass

def provjeri_email(email: str) -> bool:
    """
    Provjerava sadrži li email znak '@'.

    Args:
        email (str): Email adresa.

    Returns:
        bool: True ako email sadrži '@', inače False.
    """
    pass

def dodaj_kontakt(ime: str, telefon: str, email: str, adresa: str) -> None:
    """
    Dodaje kontakt u adresar ako su svi podaci ispravni.

    Args:
        ime (str): Ime kontakta.
        telefon (str): Telefon kontakta.
        email (str): Email kontakta.
        adresa (str): Adresa kontakta.
    """
    pass

def prikazi_kontakte() -> None:
    """
    Prikazuje sve kontakte u adresaru.
    """
    pass

def pretrazi_kontakt(ime: str) -> None:
    """
    Pretražuje adresar prema imenu kontakta.

    Args:
        ime (str): Ime kontakta za pretragu.
    """
    pass

def obrisi_kontakt(ime: str) -> None:
    """
    Briše kontakt iz adresara prema imenu.

    Args:
        ime (str): Ime kontakta koji će biti obrisan.
    """
    pass

def main() -> None:
    """
    Glavna funkcija koja omogućava korisniku da bira opcije u adresaru.
    """
    while True:
        print("\nAdresar - Odaberite opciju:")
        print("1. Dodaj kontakt")
        print("2. Prikaži sve kontakte")
        print("3. Pretraži kontakt")
        print("4. Obriši kontakt")
        print("5. Izlaz")
        
        izbor = input("Unesite broj opcije: ")
        if izbor == "1":
            ime = input("Unesite ime: ")
            telefon = input("Unesite broj telefona: ")
            email = input("Unesite email: ")
            adresa = input("Unesite adresu: ")
            dodaj_kontakt(ime, telefon, email, adresa)
        elif izbor == "2":
            prikazi_kontakte()
        elif izbor == "3":
            ime = input("Unesite ime za pretragu: ")
            pretrazi_kontakt(ime)
        elif izbor == "4":
            ime = input("Unesite ime za brisanje: ")
            obrisi_kontakt(ime)
        elif izbor == "5":
            print("Izlaz iz aplikacije.")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo.")

if __name__ == "__main__":
    main()