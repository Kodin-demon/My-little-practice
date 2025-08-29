# try: n/ except: n/ finally:
# may be very handy for many situation

try:
    number = int(input("What is your number: "))
    print(1/number)
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("We accept only numbers")
except Exception:
    print("Sorry, something went wrong")
finally:
    print("Doing a cleanup")