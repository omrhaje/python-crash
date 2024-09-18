# Match case statements (switch): An alternative to using many 'elif' statements
#                                 Execute some code if a value matches a 'case'
#                                 Benefits: cleaner and syntax is more readable

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("sunday".capitalize()))