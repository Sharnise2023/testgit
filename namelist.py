Guestlist = ['John', 'Blake', 'Quita']
print (Guestlist)
print (Guestlist[0])
message = "You are invited to dinner " + Guestlist[0].title() + '.'
print (message)

message = "You are invited to dinner " + Guestlist[1].title() + '.'
print (message)

message = "You are invited to dinner "+ Guestlist[2].title() + '.' 
print (message)

message = Guestlist[2].title()  + " cant make it"  + '.'
print (message)


Guestlist[2] = 'Lisa'
print (Guestlist)
message = "You are invited to dinner " + Guestlist[0].title() + '.'
print (message)
message = "You are inited to dinner " + Guestlist[1].title() + '.'
print (message)
message = "You are invited to dinner " + Guestlist[2].title() + '.'
print (message)
message = Guestlist[1].title() + " I have a bigger table for more people" + '.'
print (message)

Guestlist = ['John' , 'Blake' , 'Lisa']
Guestlist.insert(0, 'Javon')
print (Guestlist)
Guestlist = ['Javon', 'John' , 'Blake' , 'Lisa']
Guestlist.insert(2, 'Barney')
print (Guestlist)
Guestlist = ['Javom', 'John', 'Barney', 'Blake', 'Lisa']
Guestlist.insert(5, 'Joseph')
print (Guestlist)
message = Guestlist[0].title() + " You are invited to the dinner" + '.'
print (message)
message = Guestlist[1].title() + " You are invited to the dinner" + '.'
print (message)
message = Guestlist[2].title() + " You are invited to the dinner" + '.'
print (message)
message = Guestlist[3].title() + " You are invited to the dinner" + '.'
print (message)

message = "Sorry to inform everyone the table will not arrive in time. "
print (message)
message = "I can only invite two people. "
print (message)
Guest_list = ['Javon' , 'John' , 'Barney' , 'Blake' , 'Lisa' , 'Joseph']
print (Guest_list)
First_guest = Guest_list.pop(0)
print (Guest_list)
print (First_guest)
print ('Im sorry i had to remove you from the guest list ' + First_guest.title() + '.')
Second_guest = Guest_list.pop(1)
print (Guest_list)
print (Second_guest)
print ('Im sorry to i had to remove you from the guest list ' + Second_guest.title() + '.')
Third_guest = Guest_list.pop(3)
print (Guest_list)
print (Third_guest)
print ('Im sorry i had to remove you from the guest list ' + Third_guest.title() + '.')
Fourth_guest = Guest_list.pop(2)
print (Guest_list)
print (Fourth_guest)
print ('Im sorry i had to remove you from guest list ' + Fourth_guest.title() + '.')
message = (Guest_list[0].title() + " You are still on the guest list " + '.' )
print (message)
message = (Guest_list[1].title() + " You are still on the guest list " + '.')
print (message)
Guest_list.remove('John')
print (Guest_list)
Guest_list.remove('Blake')
print (Guest_list)
Vacationlist = ['Jamaica', 'Florida', 'Mexico']
print ("Here is the original list: ")
print (Vacationlist)
print ("\nHere is the original list: ")
print (sorted(Vacationlist))
print ("\nHere is the original list again: ")
print (Vacationlist)
print (sorted(Vacationlist, reverse = True))
print (Vacationlist)
Vacationlist.reverse()
print (Vacationlist)
Vacationlist.reverse()
print (Vacationlist)
Vacationlist.sort()
print (Vacationlist)
Vacationlist.sort(reverse = True)
print (Vacationlist)
Guestlist = ['John' , 'Blake']
Hobbylist = ['massages', 'seafood', 'movies', 'skiball']
print (Hobbylist)
print (sorted(Hobbylist))
print (Hobbylist)
print (sorted(Hobbylist, reverse = True))
print (Hobbylist)
Hobbylist.reverse()
print (Hobbylist)
Hobbylist.reverse()
print (Hobbylist)
print (sorted(Hobbylist))
print (Hobbylist)
print (sorted(Hobbylist, reverse = True))
Hobbylist.sort()
print (Hobbylist)
Hobbylist.sort(reverse = True)
print (Hobbylist)