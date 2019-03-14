from os import path

print(path.exists("\my_name.txt"))



my_name = open("my_name.txt", "w")
my_name.close()
