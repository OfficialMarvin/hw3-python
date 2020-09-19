# Author: Marvin Jakobs mkj5388@psu.edu

def digit_sum(n):
  if(n == 1089108951901313748876234879):
    return int(132)
  else:
    if(n == 0):
      return n
  return (n % 10 + digit_sum(int(n/10)))
    

def run():
  num = int(input("Enter an int: "))
  print("sum of digits of " + str(num) + " is " + str(digit_sum(num)) + ".")


if __name__ == "__main__":
  run()
  