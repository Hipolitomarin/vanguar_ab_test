# For values greater than 360 minutes, convert to hours instead
def convert_duration(x):
    if x > 360:
        return round(x / 60, 2)  # convert to hours, rounded to 2 decimals
    else:
        return round(x, 2)       # keep as minutes, rounded to 2 decimals

