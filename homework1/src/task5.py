#book list
favBooks = [
    ("Percy Jackson", "Rick Riordan"),
    ("The Witcher", "Andrzej Sapkowski"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("1984", "George Orwell"),
    ("The Hobbit", "J.R.R. Tolkien"),
]

#printing the books
print("The first three books")
for book in favBooks[:3]:
    print("The title is ", book[0], "by ", book[1])

#Student data
studentDatabase = {
    "Alice Johnson": "S1001",
    "Bob Smith": "S1002",
    "Charlie Brown": "S1003",
    "Diana Prince": "S1004"
}

#Print data
print("Student Database:")
for name, id in studentDatabase.items():
    print("Name:", name, "ID:", id)
