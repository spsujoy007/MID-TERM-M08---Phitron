class Star_Cinema:
    hall_list = []

    def entry_hall(self, hallOBJ):
        self.hall_list.append(hallOBJ)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self._hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [[0 for _ in range(self.cols)]for _ in range(self.rows)]

    def book_seats(self, movie_id, seat_info):
        if movie_id in self._seats:
            row, col = seat_info
            if 0 <= row <= self.rows and 0 <= col and col <= self.cols:
                if self._seats[movie_id][row][col] == 0:
                    self._seats[movie_id][row][col] = 1
                    print(f'Your seat no: [{row}][{col}] is booked!')
                else:
                    print(f'This seat is already booked. So sorry')
            else:
                print(f'[{row}][{col}] this seat no is invalid!') 
        else:
            print(f'Enterd movie id is invalid!')
    
    def view_show_list(self):
        for movieinfo in self._show_list:
            movie_id, movie_name, time = movieinfo
            print(f"{movie_name} is played on cinemahall at {time}. Movie ID: [{movie_id}]\n")
    
    def view_available_seats(self, movie_id):
        if movie_id in self._seats:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self._seats [movie_id][row][col] == 0:
                        # changable line 
                        print(f'AVAILABLE SEAT: [{row},{col}]')
        else:
            print(f'Your entered movie id - {movie_id} is not available')


print("========================================== \n      Welcome to Amazone movie show \n==========================================")

# our halls 
shapla = Hall(6, 6, 1)
shapla = Hall(7, 6, 2)
shapla = Hall(8, 8, 3)
shapla = Hall(5, 5, 4)

# all shows
shapla.entry_show(1, 'Red Stone', "08:10PM")
shapla.entry_show(2, 'Super 30', "06:10PM")
shapla.entry_show(3, 'Amazon', "04:10PM")
shapla.entry_show(4, 'Total Dhamal', "08:10PM")
shapla.entry_show(5, 'Golmal', "10:10AM")

print("\nChose an option: \n___________________")
print(f"OPTION 1: BOOK SEATS \nOPTION 2: VIEW_SHOW_LIST \nOPTION 3: VIEW AVAILABLE SEATS \nOPTION 4: EXIT")


while True:
    option = int(input("CHOSE A OPTION: "))
    if option == 1:
        print(f'Give me the movie id, seat row and col')
        id = int(input())
        row = int(input())
        col = int(input())
        shapla.book_seats(id, (row, col))
    elif option == 2:
        shapla.view_show_list()
    elif option == 3:
        print("Enter the show id: ")
        id = int(input())
        shapla.view_available_seats(id)
    elif option == 4:
        print("Stay with us and thank you.")
        break
    else:
        print("You chose a invalid option!!!")