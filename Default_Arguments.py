# default arguments = a default value for a certain parameters
#                     default is used when argument is omitted
#                     make your functions more flexible,reduces # of arguments

def net_price(list_price, discount = 0, tax = 0.05):
    #         ^^ this is a positional parameter
    #                       ^^ this is a default parameter
    return list_price * (1 - discount) * (1 + tax)

print(net_price(450))
#               ^^ they are used when no arguments were present, here we have only list_price

import time

def count(end, start = 0):
    #     ^^ default parameters should be after positional
    for i in range(start, end + 1):
        #                   ^^ adding 1 to the end, because range don´t count the last number
        print(i)
        time.sleep(1)
    print("Done!!!")

print(count(10))