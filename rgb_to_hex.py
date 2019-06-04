def hex_number(number):
    if number <= 0:
        return "00"
    elif len(hex(number)) == 3:
        return "0{0:x}".format(number).upper()
    elif number > 255:
        return "{0:x}".format(255).upper()
    else:
        return "{0:x}".format(number).upper()


def rgb(r, g, b):
    return "{}{}{}".format(hex_number(r), hex_number(g), hex_number(b))


def rgb_best_practice(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))