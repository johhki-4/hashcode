variabel = open('exempel.txt', 'r')

class Book:
    score = 0
    id = 0

    def __init__(self, score, id):
        self.score = score
        self.id = id


class Library:

    books = []
    signup_day = 0
    shipped_per_day = 0
    id = 0
    lib_score = 0

    def __init__(self, signup_day, shipped_per_day, id, books):
        self.books = books
        self.signup_day = signup_day
        self.shipped_per_day = shipped_per_day
        self.id = id
        self.sort_books()

    def calc_score(self, days):
        remaining_days = days - self.signup_day
        score = 0
        bookpos = 0
        for x in range(0, self.shipped_per_day*remaining_days):
            if len(self.books) > 0:
                score += int(self.books[bookpos].score)
                bookpos += 1
                if bookpos == len(self.books):
                    break
        if (bookpos != 0):
            self.lib_score = (score/self.signup_day)*bookpos
        else:
            self.lib_score = 0

    def sort_books(self):
        self.books.sort(key=lambda book: book.score, reverse=True)

    def handle_library(self, lib):
        for book in lib.books:
            if (book in self.books):
                self.books.remove(book)
                self.lib_score -= int(book.score)/int(self.signup_day)
        if self.lib_score == 0:
            total_libraries.remove(self)


class Output:
    outputlib = [] # [1, 3, 5]
    outputbooks = [] # [[2,3,4],[1,6,7,8,9],[1]]

    def finishlib(self, id, lista):
        self.outputlib.append(id)
        self.outputbooks.append(lista)

    def output(self):
        file = open('output', 'w+')
        file.write(str(len(self.outputlib))+"\n")
        for i in range(0,len(self.outputlib)):
            file.write(str(self.outputlib[i])+" "+str(len(self.outputbooks[i]))+"\n")
            for x in self.outputbooks[i]:
                file.write(str(x.id))
                if not x == self.outputbooks[len(self.outputbooks)-1]:
                    file.write(" ")
            file.write("\n")
        file.close()

# line 1
# listan[0] = B ( number of different books )
# listan[1] = L ( Number of libraries )
# listan[2] = D ( Number of days )

firstLine = variabel.readline().split()
B = int(firstLine[0])
L = int(firstLine[1])
D = int(firstLine[2])

total_books = []
total_libraries = []

# line 2
# B integers score for each book from 0 to b-1
secondLine = variabel.readline().split()

for x in range(0, len(secondLine)):
    total_books.append(Book(secondLine[x], x))


# L lines x2
# L1
# L1[0] = N number of books
# L1[1] = T days for signup
# L1[2] = M shipped per day

# L2
# N integers with book ids

for x in range(0, int(firstLine[1])):
    list1 = variabel.readline().split()
    Nlibbooks = int(list1[0])
    signup = int(list1[1])
    shipped_per_day = int(list1[2])
    listbooks = []
    list2 = variabel.readline().split()
    for y in list2:
        listbooks.append(total_books[int(y)])
    new_lib = Library(signup, shipped_per_day, x,listbooks)
    new_lib.calc_score(int(D))
    total_libraries.append(new_lib)

variabel.close()
output = Output()
old_d = D
old_d_2 = D

while D > 0 and len(total_libraries) > 0:
    for library in total_libraries:
        library.calc_score(D)
    total_libraries.sort(key=lambda library: library.lib_score, reverse=True)
    taken_lib = total_libraries[0]
    total_libraries.remove(taken_lib)
    if (D-taken_lib.signup_day >= 0):
        output.finishlib(taken_lib.id, taken_lib.books)
        for library in total_libraries:
            library.handle_library(taken_lib)
        D -= taken_lib.signup_day
    print(D)

output.output()











