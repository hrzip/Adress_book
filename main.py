import json

DATOTEKA_ADRESARA = "adresar.json"

def ucitaj_podatke() -> dict:
    """
    Učitava podatke iz JSON datoteke. Ako datoteka ne postoji ili je oštećena, vraća prazan adresar.

    Returns:
        dict: Podaci o kontaktima iz JSON datoteke ili prazan adresar.
    """

    try:
        with open(DATOTEKA_ADRESARA, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"Kontakti": {}}


def spremi_podatke(podaci: dict) -> None:
    """
    Spremi podatke u JSON datoteku.

    Args:
        podaci (dict): Podaci koji će biti pohranjeni u datoteku.
    """


    with open(DATOTEKA_ADRESARA, 'w', encoding='utf-8') as file:
        json.dump(podaci, file, indent=4)
        



def provjeri_telefon(telefon: str) -> bool:
    """
    Provjerava je li telefon sastavljen samo od brojki.

    Args:
        telefon (str): Broj telefona.

    Returns:
        bool: True ako telefon sadrži samo brojke, inače False.
    """
    return telefon.isdigit()

def provjeri_email(email: str) -> bool:
    """
    Provjerava sadrži li email znak '@'.

    Args:
        email (str): Email adresa.

    Returns:
        bool: True ako email sadrži '@', inače False.
    """
    return '@' in email

def dodaj_kontakt(ime: str, telefon: str, email: str, adresa: str) -> None:
    """
    Dodaje kontakt u adresar ako su svi podaci ispravni.

    Args:
        ime (str): Ime kontakta.
        telefon (str): Telefon kontakta.
        email (str): Email kontakta.
        adresa (str): Adresa kontakta.
    """

    if not ime.strip():
        print("Ime ne smije biti prazno!")
        return
    
    if not provjeri_telefon(telefon):
        print("Telefon mora imati samo brojke!")
        return
    if not provjeri_email(email):
        print("Email adresa mora imati znak @, upišite ispravnu adresu")
        return
    
    podaci = ucitaj_podatke()

    podaci["Kontakti"][ime] = {
        "Telefon": telefon,
        "Email": email,
        "Adresa": adresa
    }

    spremi_podatke(podaci)
    print(f"Kontakt {ime} je uspješno dodan")




def prikazi_kontakte() -> None:
    """
    Prikazuje sve kontakte u adresaru.
    """
    podaci = ucitaj_podatke()
    kontakti = podaci["Kontakti"]

    if not kontakti:
        print("Adresar je prazan")
        return
    print("\nSvi kontakti:")
    for ime, info in kontakti.items():
        print(f"\nIme: {ime}")
        print(f"\nTelefon: {info['Telefon']}")
        print(f"\nEmail: {info['Email']}")
        print(f"\nAdresa: {info['Adresa']}")
        print("-" * 30)

def pretrazi_kontakt(ime: str) -> None:
    """
    Pretražuje adresar prema imenu kontakta.

    Args:
        ime (str): Ime kontakta za pretragu.
    """
    podaci = ucitaj_podatke()
    kontakti = podaci["Kontakti"]

    if ime in kontakti:
        info = kontakti[ime]
        print(f"\nKontakt pronađen:")
        print(f"Ime: {ime}")
        print(f"\nTelefon: {info['Telefon']}")
        print(f"\nEmail: {info['Email']}")
        print(f"\nAdresa: {info['Adresa']}")
    else:
        print(f"Kontakt s imenom {ime} nije pronađen")




def obrisi_kontakt(ime: str) -> None:
    """
    Briše kontakt iz adresara prema imenu.

    Args:
        ime (str): Ime kontakta koji će biti obrisan.
    """
    podaci = ucitaj_podatke()
    kontakti = podaci["Kontakti"]

    if ime in kontakti:
        del kontakti [ime]
        spremi_podatke(podaci)
        print(f"Kontakt {ime} je obrisan")
    else:
        print(f"Kontakt {ime} nije pronađen")

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
