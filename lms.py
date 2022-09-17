
class Library:
    def __init__(self,list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 1
        with open(self.list_of_books) as book:
            content = book.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),"lender_name": "","Status":"Available"}})
            Id = Id+1

    def display_books(self):
        print("-------------------List of Books-------------------")
        print("Books ID","\t"," All book's Titles")
        print("------------------------------------------------------------")
        
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"), "- (--",value.get("Status"),"--)")

    def Issue_books(self):
        books_id = input("Please enter the book ID which you want to Issue: ")
        
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This books is already been issued to {self.books_dict[books_id]['lender_name']} \
                    on {self.books_dict[books_id]}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Books Issued Successfully.Thank You  !!! \n")
        else:
            print("Books ID not found . !!!")
        
    def return_books(self):
        books_id = input("Enter books ID which you want to return: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your book ID.")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print(" Book Returned Successfully . Thank you!!! \n")
            else:
                print("Book ID is not found !!!")


try:
    LB = Library("List_of_books.txt","Python's")
    press_key_list = {"D": "Display Books","I":"Issue Books","R":"Return Books","Q":"Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n------------------Welcome to {LB.library_name} Library------------\n")
        for key,value in press_key_list.items():
            print("Press",key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press =="i":           
            LB.Issue_books()
        
        elif key_press == "d":            
            LB.display_books()

        elif key_press == "r":            
            LB.return_books()

        elif key_press == "q":
            print("Thanks for using this library ... Visit again  !!!!")
            break

        else:
            continue
except Exception as e:
    print("Something went wrong Please check your input or try again later....  !!!")



