#tamrin 1

# print("Hello World")





#tamrin 2

# x = 'Hi this is a string'
# lower = x.lower()
# list = lower.split()
# print(list) 





#tamrin 3

# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)
# my_list.append(10)
# print(my_list)





#tamrin4

# fruit_prices = {"apple":1500, "banana":1000, "orange": 1200} 
# fruit_prices["banana"]=1100
# del fruit_prices["apple"]
# print(fruit_prices)




#tamrin5

# coordinates = (4, 3)
# x = (0,0)
# x1,y1 = coordinates
# x2,y2 = x
# distance =((x2-x1)**2+(y2-y1)**2)
# print(distance)





#tamrin6

# SetA = {1, 2, 3, 4}
# SetB = {3, 4, 5, 6}
# u = SetA.union(SetB)
# i =SetA.intersection(SetB)
# print(u)
# print(i)




# tamrin7
  
# a = int(input())
# b = int(input())
# c = int(input())
# # result = a < b <=c
# result = (a<b) and (b<=c)
# print(result)




# tamrin8

# mablagh = int(input('enter your mablagh: '))
# if mablagh > 50000:
#     takhfif = (mablagh*20)//100
# elif 20000 <= mablagh <= 50000:
#     takhfif = (mablagh*10)//100
# elif mablagh < 20000:
#     print("takhfif emal nmishavad")
# else:
#     takhfif = mablagh

# n_mablagh = mablagh - takhfif
# print(n_mablagh) 




# tamrin9

# n = int(input("tedad: "))
# x = int(input("adad: "))

# for i in range(n):
    # if x % 2 == 0:
    #     x = x // 2
    # else:
    #     x = (x * 2)-1
    
# print(x)




# tamrin10

# n = int(input())


# while n != 1:
#     print(n)
#     if n % 2 == 0:
#         n = n // 2
#     else:
#          n = n * 3 + 1


# print(n)



# ////////////////////////


# n = 0 

# while n <= 20:
#     n += 1
#     if n % 5 == 0 and n % 3 == 0:
#         print("hooop")
#         continue
#     if n % 3 == 0:
#         print("hop")
#         continue
#     if n % 5 == 0:
#         print("hoop")
#         continue
    
#     print(n)    


# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# lis = [5,6,7,8,9,10,'jan','amir']
# nlis = [x for x in lis]
# print(nlis)

# esm = ['ali' , 'amir' , 'hasan']
# famil = ['miri' , 'rezaii' , 'hoseini']
# sen = ['20' , '17' , '30']
# for i in zip(esm , famil , sen):
#     print(i)


# from random import randint
# j = randint(1 , 6)

# i = input("adad  ")
# i = int (i)

# if (i == j):
#     print("afrin")
# else:
#     print(f"ghlat  in bod {j} ")



# tamrin11

# n = int(input())

# if n % 3 == 0 and n % 5 == 0:
#     print("افسانه ای")
# elif n % 3 == 0:
#     print("جادویی")
# elif n % 3 == 0:
#     print("نفرین شده")
# else:
#     print("معمولی")




# ////////////////////////////

# def hello(names , n):

#     for i in range(n):
#         print(f"hello {names}")

# def hellooos(a , b):
#     res = a + b
#     return res

# # print(hellooos(5 , 4))

# def p_item(name , n=1):
#     for i in range(n):
#          print(name)

# p_item('jadi' , 2)




# def j_z_t_m(n1 , n2):
#     j = n1 + n2 
#     z = n1 * n2 
#     t = n1 / n2 
#     m = n1 - n2 
#     return j , z , t , m 
# x , y , a ,b = j_z_t_m(5 , 3)
# print(x) 
# print(y)
# print(a) 
# print(b)  



# import random 
# co_number = random.randint(1, 20)
# guess = 0

# def win(computer , guess):
#     return co_number == guess

# def answer(co_number , guess):
#     if computer > user:
#         res = "adad man bozorgtre"
#     elif computer < user:
#         res = "mal man kochik tare"
#     elif:
#         res = "god guess"
#     return res
    

# def get_a_guess():
#     ans = input("guess: ")
#     return int(ans)

# while (not win(co_number , guess)):
#     guess = get_a_guess()
#     print(answer(co_number , guess))
    


# tamrin12

# def hello_world():
#     print("Hello, World!")

# # hello_world()




# tamrin13

# def greet(name):
#     print(f"Hello, {name}!")

# # greet("amir")    




# tamrin14

# def is_positive(n):
#     if n >= 0:
#         return True
#     else:
#         return False
    
# print(is_positive(5))
# print(is_positive(-3))




# tamrin15

# def sum_of_squares(a , b):
#     return a**2 + b**2

# print(sum_of_squares(3 , 4))
# print(sum_of_squares(5 , 12))




# tamrin16

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(8))
# print(is_even(15))




# tamrin17

# def pick_evens(a , b):
#     if a > b:
#         return True
#     else:
#         return False

# print(pick_evens(10 , 5))
# print(pick_evens(3 , 7))




# //////////////////////////
# def zarb(*args):
#     res = 1
#     for i in args:
#         res *= i
#     return res
# b = zarb( 3, 4, 5, 6)
# print(b)




# tamrin18

# def skyline(*args):
#     if not args:
#         return 0
#     else:
#         return max(args)
    
# print(skyline(3, 15, 2, 9))
# print(skyline(1, 1, 1, 1))
# print(skyline())




# /////////////////////////
# def tavan2(x):
#     return x ** 2

# a = [3, 4, 2, 8]
# # for i in range(len(a)):
# #     a[i] = tavan2(a[i])
# # print(a)    
# tav = map(tavan2, a)
# # for n in tav:
# #     print(n)
# # # print(list(tava))

# def is_ashari(x):
#     return x != int(x)
#     # if x == int(x):
#     #     return True
#     # else:
#     #     return False
    
# a = [3, 4, 1.7, 9, 8.21, 2, 8, 2.7, 3.2]

# print(list(filter(is_ashari, a)))


# multiply = lambda x, y: x * y
# print(multiply(3, 4))








# tamrin19

# class book():
#     def __init__(self, page):
#         self.pages = page

# mybook = (540)
# print(mybook.pages)

# class person:
#     def __init__(self, name):
#         self.name = name

# p = person("ali")
# print(p.name)






# class book():
#     def __init__(self , name, page):
#         self.pages = page
#         self.name = name
#     def open(self):
#         print(f'opened the {self.name} which has ({self.pages}) pages')

# b1 = book("cpro..." , 230)
# b1.open()


# class darsi(book):
#     def __init__(self, reshte, paye, name, page):
#         book .__init__(self , name, page)
#         print('a new darsi book')
#         self.reshte = reshte
#         self.paye = paye
#     def open(self):
#         print(f'opened {self.name} of {self.reshte} psye {self.paye}')

# d = darsi('reyazi' , 200 ,'tajrobi' , 3)
# d = open()


# class ruuner():
#     def __init__(self , name):
#         self.name = name
#     def action(self):
#         print(f'{self.name} is ruuning')

# sara = ruuner('sara')
# sara.action()

# class cyclist():
#     def __init__(self , name):
#         self.name = name
#     def action(self):
#         print(f'{self.name} is biking')

# amir = cyclist('amir')
# amir.action()

# for person in {amir , sara}:
#     person.actine()

#     print(person)



# class book():
#     def __init__(self , name='unknow', page=0):
#         self.pages = page
#         self.name = name
#     def open(self):
#         print(f'opened the {self.name} which has ({self.pages}) pages')

#     def __len__(self):
#         return self.pages
#     def __str__(self):
#         r = f'{self.name} , {self.pages}'
#         return r
#     def __del__(self):
#         print(f"oh the {self.name} book is vanisshing!")



# b = book("reyazi" , page=230)
# print(len(b))
# print(b)
# print(del(b))

# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def __str__(self):
#         return f"Car brand: {self.brand}"

# my_car = Car("Toyota")
# print(my_car)


# tamrin21
# class animal:
#     zoo_name = "iran Zoo"  

#     def __init__(self, name, species, age, sound):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.sound = sound

#     def make_sound(self):
#         print(f"{self.name} mige: {self.sound}")

#     def info(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
#         print(f"Age: {self.age}")
#         print(f"Zoo: {animal.zoo_name}")

#     def __str__(self):
#         return f"{self.name} ({self.species}) - Age: {self.age}, Sound: {self.sound}"


# class Bird(animal):
#     def __init__(self, name, species, age, sound, wing_span):
#         super().__init__(name, species, age, sound)
#         self.wing_span = wing_span 

#     def make_sound(self):
#         print(f"{self.name} jir jir kardan: {self.sound}")

#     def info(self):
#         super().info()
#         print(f"Wing Span: {self.wing_span} cm")


# print("animal Example:")
# shir = animal("shir", "gorbesan", 5, "woooooow")
# print(shir)           
# shir.make_sound()
# shir.info()

# print("\nBird Example:")
# parrot = Bird("mina", "prande", 3, "oooooo", 20)
# print(parrot)
# parrot.make_sound()
# parrot.info()

        