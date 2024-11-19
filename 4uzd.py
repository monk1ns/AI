def analizet_noskanojumu_vienkarsi(teikums):
    pozitivi_vardi = ["lielisks", "apmierināts", "patīk"]
    negativi_vardi = ["vīlies", "slikts", "neatbilst"]

    teikums = teikums.lower()
    if any(vards in teikums for vards in pozitivi_vardi):
        return "Pozitīvs"
    elif any(vards in teikums for vards in negativi_vardi):
        return "Negatīvs"
    else:
        return "Neitrāls"

teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]


for teikums in teikumi:
    print(f"'{teikums}' - Noskaņojums: {analizet_noskanojumu_vienkarsi(teikums)}")
