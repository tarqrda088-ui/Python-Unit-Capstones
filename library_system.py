your_library = []
book = input("enter the name of a book you own: ")
another_book = input("enter the name of another book you own, or press 'enter' to skip: ")

your_library.append(book)
your_library.append(another_book)
print("your library is: ", your_library)

my_wishlist = []
wish_list = input("enter the name of a book you wish to have in the future: ")
another_wish = input("enter the name of another book you wish to have in the future or press 'enter' to skip: ")

my_wishlist.append(wish_list)
my_wishlist.append(another_wish)
print("your wishlist is: ", my_wishlist)

have_wishlist = input("enter the name of a book from your wishlist that you have now or press 'enter' to skip: ")
my_wishlist.append(have_wishlist)

updated_library = []
updated_wishlist = []

updated_library = your_library
updated_library.append(have_wishlist)
my_wishlist.remove(have_wishlist)

updated_wishlist = my_wishlist

print("your updated library is: ", updated_library)
print("updated wishlist is: ", updated_wishlist)

donation = input("enter the name of a book you wish to donate or press 'enter' to skip: ")
if donation in updated_library:
    updated_library.remove(donation)

final_library = updated_library
print("your final library after donation is: ", final_library)
