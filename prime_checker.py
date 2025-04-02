def is_prime(number):
  """
  Checks if a given number is a prime number.

  Args:
    number: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if not isinstance(number, int):
    return False  # Not an integer, can't be prime

  if number <= 1:
    return False  # 1 and numbers less than 1 are not prime

  if number <= 3:
    return True   # 2 and 3 are prime

  if number % 2 == 0 or number % 3 == 0:
    return False  # Divisible by 2 or 3, not prime

  # Optimized loop: Check divisibility only up to the square root of the number
  # and only check numbers of the form 6k ± 1
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6

  return True  # If no divisors found, it's prime


def get_user_input_and_check_prime():
  """
  Prompts the user for a number, checks if it's prime, and prints the result.
  """
  try:
    user_input = input("Enter a number: ")
    number = int(user_input)  # Convert the input to an integer

    if is_prime(number):
      print(f"{number} is a prime number.")
    else:
      print(f"{number} is not a prime number.")

  except ValueError:
    print("Invalid input. Please enter an integer.")


# Example usage:
if __name__ == "__main__":
  get_user_input_and_check_prime()