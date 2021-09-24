def fizzbuzz(num):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        if len(output) > 0:
            output += " "
        output += "Buzz"
    if len(output) > 0:
        return output
    else:
        return num
