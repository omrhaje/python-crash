# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "9234-5678-9012-3456"

print(credit_number[0])             # Return index 0
print(credit_number[:4])            # End by index 4
print(credit_number[5:9])           # Start by index 5, End by 9
print(credit_number[5:])            # Start by index 5
print(credit_number[-0])            # ?
print(credit_number[::3])           # Run 3 stepwise


last_digits = credit_number[-4:]    # Return first indexes reversed
print(f"XXXX-XXXX-XXXX-{last_digits}")


credit_number = credit_number[::-1]         # ::-1 is for reversing the digits/characters
print(credit_number)