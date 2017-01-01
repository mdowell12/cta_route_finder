
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

