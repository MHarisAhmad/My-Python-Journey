def create_character(name,strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not (isinstance(strength,int) and isinstance(intelligence,int) and isinstance(charisma, int)):
        return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma <1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    str_dots = "●" * strength + "○" * (10 - strength)
    int_dots = "●" * intelligence + "○" * (10 - intelligence)
    cha_dots = "●" * charisma + "○" * (10 - charisma)

    # Combine into the final required layout
    character_sheet = (
        f"{name}\n"
        f"STR {str_dots}\n"
        f"INT {int_dots}\n"
        f"CHA {cha_dots}"
    )
    
    return character_sheet