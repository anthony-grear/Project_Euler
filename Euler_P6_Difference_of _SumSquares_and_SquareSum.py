#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squares = [x**2 for x in range(1,101)]
sum_of_squares = sum(squares)
list_of_integers = [y for y in range(1,101)]
sum_of_integers = sum(list_of_integers)
square_of_sum = sum_of_integers**2
difference = abs(sum_of_squares - square_of_sum)
print(difference) #answer 25164150