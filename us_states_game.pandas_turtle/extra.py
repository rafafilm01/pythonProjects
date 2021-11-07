# new_range =[num *2 for num in range(1,5)]
# print(new_range)
# names = ['john', 'Mike']
# captalised_names = [name.upper() for name in names ]
# print(captalised_names)

# with open('file1.txt') as data1:
#     f1 =data1.readlines()
#     print(f1)

# with open('file2.txt') as data2:
#     f2 = data2.readlines()
#     print(f2)

# result = [int(num) for num in f1 if  num in f2]
# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
# Write your code below:
# split = sentence.split()
# for word in split:
#     word_count= len(word)
#     print( word + ' '+str(word_count))


# result = [word:len(word) for word in sentence.split()]
result = {word: len(word) for word in sentence.split()}
# print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# Write your code 👇 below:

weather_f = {day :((temp * 9/5) + 32 ) for (day, temp ) in weather_c.items()}

print(weather_f)
