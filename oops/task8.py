class Library:
    total_books=100
    def __init__(self,borrowed_books=0):
        self.borrowed_books=borrowed_books
    def reduce_book(self,num):
        if num<=Library.total_books:
            self.borrowed_books+=num
            Library.total_books-=num
            print(f"total books borrowed are {num} and total books avilable are {Library.total_books}")
        else:
            print(f"not enough books available to borrow")
        