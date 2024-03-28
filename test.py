from location import Location

location = Location('numbers_test.txt')
if location.get_code() == 801:
    print('Test passed')
else:
    print('Test failed')
