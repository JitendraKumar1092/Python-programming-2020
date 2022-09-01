# a person want to withdraw money from the atm machine . make a python program to calculate lowest number of notes .
# don' forget a 100 rupees note is compulsotry to with draw(atm machine have only notes 100,500,and 2000
# Input section
amount = int(input("Enter the total amount to be withdraw (in multiople of 100) - "))
#Logic section
amount -= 100
notes_100 = 1
notes_2000 = amount//2000
amount -= notes_2000 * 2000
notes_500 = amount // 500
amount -= notes_500 * 500
notes_100 += amount // 100
# output section
print(f"notes of 100 = {notes_100},notes of 500 = {notes_500}, notes  of 2000 = {notes_2000}")
