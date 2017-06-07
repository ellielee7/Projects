def draw_stars(array):
    for x in array:
        print x * "*"

num = [4, 6, 1, 3, 5, 7, 25]
draw_stars(num)

def stars(array):
    for x in array:
        if isinstance(x, int):
            print x * "*"
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print length * letter

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)
