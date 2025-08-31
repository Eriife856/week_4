# fav_quote = input("enter fav_quote: ")
# print(fav_quote)
# print(fav_quote.title())

# list=[]
# list_1 = input("enter shopping item: ")
# list_2 = input("enter shopping item: ")
# list_3 = input("enter shopping item: ")
# shopping_list = (list_1 ,list_2,list_3)
# print(shopping_list)


# #word counter
# sentence= input(" enter a sentence: ")
# print(sentence.split())
# print(len(sentence))

# #name organizer
# user1 = input("kindly enter your name: ").lower()
# user2 = input("kindly enter your name: ").lower()
# user3 = input("kindly enter your name: ").lower()
# user4 = input("kindly enter your name: ").lower()
# user5 = input("kindly enter your name: ").lower()
# users=(user1,user2,user3,user4,user5)
# print(users)
# print(sorted(users))

#student score tracker
# student_name= []
# student_scores =[]
# for i in range (3):
#  name = input("kindly enter your name: ").upper()
#  score=int(input("input your score: "))
#  student_name.append(name)
#  student_scores.append(score)
# print("\nstudent_score_tracker")
# print(f"name:{student_name}  score:{student_scores}")
# for i in range(3):
#  print(f"name:{student_name[i]}  score:{student_scores[i]}")


 #word analyzer
word = input("enter a word: ")
print(len(word))
print(word[::-1])

#list manipulation
cities= ['oyo', 'lagos','abk','abuja','osogbo']
cities.insert(3,'kogi')
cities.remove('osogbo')
cities.insert(0,'ibadan')
print(cities)
