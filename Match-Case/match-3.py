# Using an additional if with case

mon = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if mon == 5:
        print("A week in May")

    case _:
        print("No match")
