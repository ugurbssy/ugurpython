import os

def space_occupied(dir):

    total = 0
    try:
        print("to add the size of", dir)

        for link in os.scandir(dir):
            if link.is_file():
                total = total + link.stat().st_size
            elif link.is_dir():
                total = total + space_occupied(link)
    except NotADirectoryError:
        return os.path.getsize(dir)

    return total

print(space_occupied("C:\\Users\ASUS\Desktop\Luis"))
print(space_occupied("C:\\Users\ASUS\Desktop\wt.txt"))
