mile_in_km = 1.60934
km_in_mile = 0.621371
ft_in_inch = 0.0833333
inch_in_ft = 12


def mil2km(mil):
    "Returns value in kilometer from miles"
    return mil * mile_in_km


def km2mil(km):
    "Returns value in mile from kilometer"
    return km / km_in_mile


def ft2inch(ft):
    "Returns value in inch from feet"
    return ft * inch_in_ft


def inch2ft(inch):
    "Returns value in feet from inch"
    return inch / inch_in_ft
