
def seconds_to_minutes_filter(s):
    """Turn seconds into minutes display.
    """
    mins = int(round(s / 60.0))
    return "{} mins".format(mins)


def pretty_minutes_filter(i):
    """Take a number i, make it an integer, tag on 'mins' to the end.
    """
    num = int(round(i))

    if num != 0:
        return "{} mins".format(num)
    else:
        return "Leave now!"


def route_name_map_filter(r):
    """
    CTA API returns weird route names sometimes.  Map them to pretty values here.
    """
    m = {
        "G": "Green"
    }

    return m[r] if r in m else r