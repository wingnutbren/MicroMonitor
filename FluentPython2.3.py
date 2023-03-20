colors = ['black','white']
sizes = "S M L".split()

tshirts = [(cl, sz) for cl in colors for sz in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color,size))
