# keyword arguments = an argument preceded by an identifier
#                     helps with readability, order of arguments doesn't matter

for num in range(1, 10):
    print(num, end=", ")
    #          ^^ that is a KEYWORD argument, but without it function will use DEFAULT end - a new line

def get_phone(country, area, first, middle = "", last = ""):
    return f"{country}-{area}-{first}-{middle}-{last}"

phone_num = get_phone(country="+49", area="176", first="411", middle="975", last="36")
#                              ^^ because I made default a string the input also should be a string
#                     ^^ keyword arguments also have to be after positional one

print(phone_num)