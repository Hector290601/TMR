numbers = [1, 2, 3, 4, 5]

"""
def evenOrOdd(number):
    
    return number % 2 == 0

print(list(filter(evenOrOdd, numbers)))"""

print(list(filter(lambda number: number %2 == 0, numbers)))