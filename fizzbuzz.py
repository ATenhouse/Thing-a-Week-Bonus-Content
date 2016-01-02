# **Fizz Buzz**
# Prompt:
# Write a program that prints the numbers from 1 to 100.
# For multiples of 5, print FIZZ. for multiples of 3, print BUZZ.
# for multiples of both, print FIZZBUZZ.


@profile
def jam(n):
    for num in xrange(1, n + 1):
        msg = ""
        if num % 3 == 0:
            msg += "Fizz"
        if num % 5 == 0:
            msg += "Buzz"
        # I like to print the number and string for validation.
        print msg or num

jam(100)
