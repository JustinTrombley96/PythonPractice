# print("Justin Trombley")
# name = input("What's your name? ")
# print('Hello ' + name)

#Fundamental Data Types

#int
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(2 **3)
print( 5 // 2)
print(5 % 4)
#float
print(type(2 / 4))
print(type(1.1 + 9.9))
#math functions
print(round(3.9))
print(abs(-15))

#operator precedence (PEMDAS)
print(20 - 5 * 4)
#() 
# **
# * /
# + -


#bool
#str
print(type("Hello I am a string."))
username = 'Hexley'
password = 'IsTheKiller'
descriptions = '''
I'm a doctor.
I have a crush on Lillian.
My daughter means the world to me.
I am definitely not the killer.
'''
print(descriptions)
first_name = 'Max'
last_name = 'Hexley'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation
print('Hello ' + 'Hexley')

#type conversion
print(type(int(str(100))))

#list
#tuple
#set
#dict

#Classes -> custom types
#Supercar

#Specialized Data Types
#Modules

#None 

#binary representation
print(bin(5))
print(int('0b101', 2))

#variables
user1_iq = 180
user2_iq = 190
user3_iq = 210 
user2_lowered_iq = user2_iq / 2
a, b, c, = 1, 2, 3
print(a, b, c)
print(a)
print(b)
print(c)
print(user2_iq)
print(user2_lowered_iq)


#constants are all in caps
PI = 3.14

#augmented assignment operator
cash = 5
cash = cash + 2
cash += 2
cash -= 2
cash *= 2
print(cash)