"""A small airline has just purchased a computer for its new automated reservation system. The owner has asked you to program the new system.
You’ll write a program to assign seats on each flight of the airlines only plane (capacity: 10 seats).

Your program should display the following menu of alternatives:
Please type 1 for “Business Class”
Please type 2 for “Economy Class”

If the person types 1, then your program should assign a seat in the Business class section (seats 1-5).
If the person types 2, then your program should assign a seat in the Economy section (seats 6-10). 

Your program should then print a boarding pass indicating the person’s seat number and whether it’s in the Business class or the Economy section. 

Use a list to represent the seating chart of the plane. Initialize all the elements of the list to 0 to indicate that all seats are empty.
As each seat is assigned, set the corresponding element of the list to 1 to indicate that the seat is no longer available.

Your program should, of course, never assign a seat that has already been assigned. When the first-class section is full, your program should ask the person
if it’s acceptable to be placed in the economy section (and vice versa). If yes, then make the appropriate seat assignment.
If no, the print the message “Next flight leaves in three hours”."""

def main():
    TOTAL_SEATS=10
    seats=[0]*TOTAL_SEATS
    s1=1         #Economy class (1-5)
    s2=6         #Business class (6-10)
    another_booking="y"
    while another_booking=="y" or another_booking=="Y":
        print("Enter 1 for economy class\nEnter 2 for business class ")
        user_selection=int(input("Which class do you want to reserve? "))
        if seats!=[1]*TOTAL_SEATS:
            if(user_selection==1):
                economy_class(s1,seats)
                s1 += 1
            elif(user_selection==2):
                business_class(s2,seats)
                s2 += 1
            else:
                print("Invalid Selection")
        else:
            print("Next flight leaves in three hours")
            break
        another_booking=input("Do you want another reservation?(Y/N): ")
        print()
def economy_class(s1,seats):
    for index in range(0,s1):
            pass
    if index>=0 and index<5:
        seats[index]=1
        print("Economy Class: ",end="")
        print("Your seat number is",index+1)
        print(seats)
        print(" "*5,"*"*30)
    else:
        print("SORRY! Economy class's seats are fulled")
        print("Do you want to reserve seat in business class?(Y/N) ",end="")
        user_choice=input()
        if(user_choice=="y" or user_choice=="Y"):
            print("Enter 2 in other reservation")
        print(" "*5,"*"*30)
def business_class(s2,seats):
    for index in range(5,s2):
            pass
    if index>=5 and index<10:
        seats[index]=1
        print("Business Class: ",end="")
        print("Your seat number is",index+1)
        print(seats)
        print(" "*5,"*"*30)
    else:
        print("SORRY! Business class's seats are fulled")
        print("Do you want to reserve seat in economy class?(Y/N) ",end="")
        user_choice=input()
        if(user_choice=="y" or user_choice=="Y"):
            print("Enter 1 in other reservation")
        print(" "*5,"*"*30)
main()
