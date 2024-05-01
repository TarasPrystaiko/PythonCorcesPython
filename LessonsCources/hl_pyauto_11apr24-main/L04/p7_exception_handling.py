"""
Request number from user and output square of number.
If user entered 'q', stop program
"""

while True:
    user_input = input('Enter number If you want to stop enter Q: ')
    if user_input.lower() == 'q':
        break
    else:
        try:
            number = int(user_input)
            print(number * number)

        except ValueError:
            raise Exception('Entered value can"t be casted to int')
        except KeyError:
            print('Caught')
        else:
            print('Successfully calculated')
        finally:
            print('Another round')
