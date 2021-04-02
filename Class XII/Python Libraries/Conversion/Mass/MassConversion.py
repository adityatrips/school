kgs_in_tonne = 1000
tonne_in_kgs = 0.001
kgs_in_pound = 2.20462
pound_in_kgs = 0.453592


def kg2tonne(kg):
    "Returns the tonne value in kg"
    return kg * kgs_in_tonne


def tonne2kg(tonne):
    "Returns the kg value in tonnes"
    return tonne / tonne_in_kgs


def kg2lbs(kg):
    "Returns the kg value in pounds"
    return kg * kgs_in_pound


def lbs2kg(lbs):
    "Returns the pounds value in kg"
    return lbs / pound_in_kgs
