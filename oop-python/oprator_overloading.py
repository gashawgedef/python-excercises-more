
class Books:
    def __init__(self,pages) -> None:
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    

book1=Books(100)
book2=Books(150)
print(book1.__add__(book2))