def rup(doll):  # Void
    print(f"{doll} dollars are {doll*72} rupees")


def rupee(doll):  # Non-Void
    return doll * 72


doll = float(input("ENTER DOLLARS\n >> "))
rup(doll)
rupee(f"{doll} dollars are {rupee(doll)} rupees")
