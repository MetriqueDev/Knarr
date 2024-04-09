from classes.destination import Destination


with open("cartes_destination.txt","w") as file:
    for i in range(15):
        a=i+1
        b=(Destination(str(input("influ ou ech ?")), str(input("cout en couleur")), int(input('cout en recrues'))))
        b.image(a)
        file.write(b)