direction=input("Enter a direction").lower()

match direction:
    case("north"):
        print(up)
    case("south"):
        print(down)
    case("east"):
        print(right)
    case("west"):
        print(left)
    case _:
        print("not a valid direction")