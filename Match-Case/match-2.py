# Combine cases using |

day = input("Enter the day of the week:")
day = int(day)

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")
