#Write a program to calculate the number of notes in the given amount

amount=int(input("Give a number"))


note_1=amount//100

note_2=(amount%100)//50

note_3=((amount%100)%50)//10

print("Note of 100:", note_1)

print("Note of 50:" ,note_2)

print("Note of 10:", note_3)