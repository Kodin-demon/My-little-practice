# Match-case statement (switch): An alternative to using many "elif" statements
#                                Execute some code if a value matches a "case"
#                                Benefits: cleaner and syntax more readable

def week_days(day):
    match day:
        case 1:
            return "It is Monday"
        case 2:
            return "It is Tuesday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Sunday"
        case 7:
            return "It is Saturday"
        case _:
            return "It is not a valid day"

def is_weekend(day):
    match day:
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case "Sunday"|"Saturday":
            return True
        case _:
            return False

print(is_weekend("banana".capitalize()))