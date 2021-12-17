from lab_oop.rectangle import Rectangle
from lab_oop.circle import Circle
from lab_oop.square import Square


def main():
    r = Rectangle("Синего", 7, 0)
    c = Circle("Красного", 13)
    s = Square("Желтого", 14)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()