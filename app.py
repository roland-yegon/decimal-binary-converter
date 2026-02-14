"""A script that converts decimal numbers to bytes."""

# Introduction text
print('\n\n=====================================')
print('Decimal to Bytes Converter.')
print('=====================================\n')

while True:
    # user inputs the decimal number
    try:
        decimal = int(input('Enter decimal number: '))
    except ValueError:
        print("\nInvalid input. Please enter a valid integer.")
        continue

    # variables to be set
    division_count = 0
    results = []

    # loop that collects the binary 1 & 0
    while division_count < 8:
        remainder = decimal % 2
        decimal = decimal // 2
        results.append(remainder)
        division_count += 1

    # Output the results
    print(f'The byte is: {results[::-1]}\n')

    # Try again
    choices = ['yes', 'no']
    try_again = None

    while try_again not in choices:
        try_again = input('Would you like to try again? (yes/no): ').lower()

    if try_again != 'yes':
        print('Bye!!! Come again anytime.\n\n')
        break
    else:
        continue
