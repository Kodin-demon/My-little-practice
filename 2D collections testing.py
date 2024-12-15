# so 2d collections is just 2 or more collections inside of collection

Items = ("paper", "pen", "book")
Furniture = ("seat", "table", "lamp")

My_room = (Items, Furniture)

#print(Items)
#print(Furniture)
#print(My_room)

for things in My_room:
    for thing in things:
        print(thing, end=" ")
    print()

#looks easy, atleast for now