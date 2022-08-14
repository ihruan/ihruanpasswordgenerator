import random

print("V's Password Generator 1.0")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

passwordLength = int(input("Input Password Length Here " ""))

newPassword = []
for x in range(passwordLength):
  newPassword.append(random.choice(characters))

  finalPassword = ''.join(map(str, newPassword))

  print("\n This is your new password: ", finalPassword)
