max_time = 100
fizzbuzz_var = 1

for i in range(max_time):
    if fizzbuzz_var % 5 == 0 and fizzbuzz_var % 3 == 0:
        print("FizzBuzz")
    elif fizzbuzz_var % 3 == 0:
        print("Fizz")
    elif fizzbuzz_var % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz_var)
    fizzbuzz_var = fizzbuzz_var + 1
    max_time = max_time - 1
