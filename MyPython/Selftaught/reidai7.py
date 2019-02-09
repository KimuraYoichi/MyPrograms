# import pathlib

# p_file = pathlib.Path('Users/zx7y-kmr/OneDrive/Sources/python/test.txt/')


# print(p_file)
# print(type(p_file))


with open("test.txt","w") as f:
    f.write("test")


with open("test.txt","a",encoding="utf-8") as f:
    f.write("arigatou2")

with open("test.txt","r") as f:
    print(f.read())


    
    

