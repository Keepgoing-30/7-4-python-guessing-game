import getpass  # add the getpass library to hide the correct_number.

correct_number = int(getpass.getpass('Enter your number (it will be hidden): '))
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess_count += 1
  attempts_left = guess_limit - guess_count
  guess = int(input('What is your guess? '))
  if guess == correct_number:
    print('You guessed it!')
    break
  else:
    if guess_count < guess_limit:
      print(f'You have {attempts_left} attempt(s) left! Please try again!')
else:
  print(f'You failed! The correct answer is number {correct_number}.')
