# Password-Generator
This is a password generator programmed with the Python Programming Language.

# How it works
The Password-Generator works by taking the user's input for the desired password length, and then it utilizes the 'random' module in Python to create a randomized password using a predefined set of characters.

This happens in order by the following steps:
1. The program starts by collecting the desired length of the password as an integer using the input() function.
2. It defines a list of characters called characters that the password will be generated from. These characters include uppercase and lowercase letters, digits, and some special symbols.
3. The program shuffles the characters list to randomize the order of the characters.
4. Next, it iterates through the characters list, selecting random characters to create the password of the desired length. The selected characters are stored in the password list.
5. The password list is then shuffled again to mix up the characters even further.
6. The password list, which now contains the randomized characters for the password, is converted into a string.
7. Finally, the generated password is printed to the console.

