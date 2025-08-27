
class Bookshelf:

    def __init__(self, title="Unnamed", autor=None, num_pages=0):
        self.title = title
        self.autor = autor
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.autor}"
    # ^^ prints this instead of memory address by directly printing argument name

    def __eq__(self, other):
        # ^^ stands for //equal//
        return self.title == other.title and self.autor == other.autor
    # ^^ allow us to see if two arguments are equal or not

    def __lt__(self, other):
        #^^ stands for //lower than//
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        # ^^ stand for //greater than//
        return self.num_pages > other.num_pages
    #^^ both of these functions just allow comparison for two arguments

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    #^^ allow addition

    def __contains__(self, key):
        return key in self.title or key in self.autor
    #^^ literally a thing that allows you to search keyword in given parameter

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'autor':
            return self.autor
        elif item == 'pages':
            return self.num_pages
        else:
            return f"Given attribute '{item}' was not found"
    #^^ I assume it is self-explanatory. let you use argument[item you want to get]

book = Bookshelf("Kaltes Blut", "Dittrich Roland", 48)
book2 = Bookshelf("In the land of unlearned lessons", "Geraskina Lija", 96)
book3 = Bookshelf("The Lion, The Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Bookshelf()

print(book4)
print(book == book2)
print(book3 > book)
print("the" in book3)
print(book4['date'])