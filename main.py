
class Library:

    books = []

    def __init__(self,  books_count, signup_time, scan_time, books):
        self.scan_time = scan_time
        self.signup_time = signup_time
        self.books_count = books_count
        self.books = books

    def get_book_to_score(self):
        count = 0
        book_to_score = {}
        for data in self.books:
            book_to_score[count] = data
            count += 1
        book_to_score = sorted(book_to_score.items(), key=lambda x: x[1])
        book_to_score.reverse()
        return book_to_score


class Scanner:

    libraries = []
    scores = []

    def __init__(self, books_number, library_number, days):

        self.books_number = books_number
        self.books_number = books_number
        self.library_number = library_number
        self.days = days

    def get_amount_of_signup(self, path):
        lib_to_signup_time = {}
        count = 0


        for data in self.libraries:
            lib_to_signup_time[count] = data.signup_time
            count += 1
        lib_to_signup_time = sorted(lib_to_signup_time.items(), key=lambda x: x[1])
        lib_to_signup_time.reverse()
        day_count = 0
        signup_count = 0

        while day_count < self.days and signup_count < self.library_number:
            if day_count + lib_to_signup_time[signup_count][1] <= self.days:
                day_count += lib_to_signup_time[signup_count][1]

                signup_count += 1
            else:
                break
        output = open(f"{path}_output", 'w')
        output.write(f'{signup_count}\n')
        test_count = 0
        while test_count < signup_count:
            library = self.libraries[lib_to_signup_time[test_count][0]]
            book_to_score = dict(library.get_book_to_score())
            library.books = list(map(lambda x: str(x), library.books))
            remaining_days = self.days - lib_to_signup_time[test_count][1]
            output.write(f'{lib_to_signup_time[test_count][0]} {remaining_days}\n')
            book_to_score = list(map(lambda x: str(x), book_to_score.keys()))
            iii = ' '.join(book_to_score[: (library.scan_time * remaining_days)])
            output.write(f"{iii}\n")
            test_count += 1
        output.close()
        return signup_count


def clean_list(the_list):
    data = []
    for a in the_list:
        data.append(list(map(lambda x: int(x), a)))
    return data


def take_input(path):
    file = open(path, 'r')
    data = file.readlines()
    data = list(map(lambda x: x.replace("\n", "").split(), data))
    data = clean_list(data)
    scanner = Scanner(data[0][0], data[0][1], data[0][2])
    scanner.scores = list(map(lambda x: int(x), data[1]))
    print(data)
    count = 0
    while count < scanner.library_number:
        focus = data[2 + count*2]
        scanner.libraries.append(Library(focus[0], focus[1], focus[2], data[3 + count*2]))
        count += 1

    return scanner


def main(path):
    a = take_input(path)
    sign_up_count = a.get_amount_of_signup(path)
    print(sign_up_count)




if __name__ == "__main__":
    main("a_example.txt")
    main("b_read_on.txt")
    main("c_incunabula.txt")
    main("d_tough_choices.txt")
    main("e_so_many_books.txt")
    main("f_libraries_of_the_world.txt")