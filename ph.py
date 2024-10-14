class Star_Cinema:
    __hall_list = []
    
    def entry_hall(self, hall):
        self.__hall_list.append(hall)
    

class Hall(Star_Cinema):
    def __init__(self,row,cols,hall_no) -> None:
        self.__row = row
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        super().entry_hall(self)


    def entry_show(self, id,movie_name,time):
        info=(id,movie_name,time)
        self.__show_list.append(info)
        make_seats=[]
        for i in range(self.__row):
            make_seats.append([0]*self.__cols)
        
        self.__seats[id]=make_seats


    def book_seats(self,id,seats):
        if id not in self.__seats:
                print("Show not found")
                return
        for seat in seats:
            row,col = seat
            if row>=self.__row or col>=self.__cols:
                print("Invalid Seat")
                print("No seats booked")
                return
            if self.__seats[id][row][col]==1:
                print(f"Seat at {row+1},{col+1} already booked")
                print("No seats booked")
                return
               
        for seat in seats:
            row,col = seat
            self.__seats[id][row][col]=1
        print("Seats booked for show ID:",id)
        print("Seats booked are:")
        for row,col in seats:
            print(f'Row:{row+1}, Col:{col+1}')


    def view_show_list(self):
        print("-----------------Show List-----------------")
        for show in self.__show_list:
            print(f'ID:{show[0]}, Movie: {show[1]}, Time: {show[2]}')


    def view_available_seats(self,id):
        if id not in self.__seats:
            print("Show not found")
            return
        print("-----------------Available Seats-----------------")
        for seat in self.__seats[id]:
            print(seat)
    


hall1=Hall(10,8,1)
hall1.entry_show("101","The Matrix","16/10/2024 9:00 PM")
hall1.entry_show("102","Spider Man","16/10/2024 11:00 PM")
hall1.entry_show("201","Mohanagar","15/10/2024 4:00 PM")
hall1.entry_show("202","HAWA","17/10/2024 6:00 PM")


while True:
    print("1. View Show List")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice=='1':
        hall1.view_show_list()
    elif choice=='2':
        hall1.view_show_list()
        id = input("Enter Show ID: ")
        hall1.view_available_seats(id)
    elif choice=='3':
        hall1.view_show_list()
        id = input("Enter Show ID: ")
        quantity = int(input("Enter number of seats: "))
        seats = []
        for i in range(quantity):
            row = int(input("Enter row(starts from 1): "))
            col = int(input("Enter col(starts from 1): "))
            seats.append((row-1,col-1))
        hall1.book_seats(id,seats)
    elif choice=='4':
        break
    else:
        print("Invalid Choice")
    print()






