# Password-Generator
This is a password generator programmed with the Python Programming Language.

# Which File to Use
The main.py is for the following: Running locally in your console/terminal
The app.py needs to be paired up with the templates folder and made sure all packages are installed in requirements.txt for the following: To run the web preview of the code, using Flask ---> More information in Testing and Use Section

# Testing and Use
You can test the code fully by running the app.py file (while ultimately making sure you have every package in requirements.txt installed), which is a web preview of the code in action using Flask. (HTML, CSS, PYTHON)
FROM AUTHOR: This project is 100% Open-Source and free of use, however, I would highly appreciate if you could include my name, or this repository if used for public necessities. It's not a must, but a highly appreciated action.

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

General Information
-------------------
