def get_full_name(a: str, b: str, c: int):
    full_name = a.title() + " " + b.title()  # Großschreibung der Initialen mit .title()
    age = c
    return full_name + " is " + str(age) + " years old"


vorname = "viktor"
nachname = "maier"
alter = 35

print(get_full_name(vorname, nachname, alter))
