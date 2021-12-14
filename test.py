# File Not Found

# try:
#     file = open("data1.txt")
# except FileNotFoundError:
#     print("Not found")
#     file = open("data1.txt", "w")
#     file.write("Something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")

fruits = ["apple", "Pear", "Orange"]

# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
# try:
#     make_pie(2)
# except IndexError as error_message:
#     print(f"Error Occurred {error_message}")
#     print("Fruit Pie")

facebook_post =[
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 20, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {"Comments": 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_post:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(total_likes)
