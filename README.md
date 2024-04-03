# email-slicer
The Email Slicer is a Python program designed to take an email address as input and separate it into its username and domain name parts. It consists of two main functionalities:

Email Validation: The program first checks whether the input provided by the user is a valid email address or not. It utilizes regular expressions to validate the email format.
Menu-driven Interaction: After validating the email address, the program displays a menu where the user can choose what information they want to extract from the email address:
Print Username
Print Domain name
Print Both (Username and Domain name)
Exit the program
Features:
Input Validation: Validates the user input to ensure it conforms to the standard email format.
Menu-driven Interaction: Provides a user-friendly menu interface for the user to choose the desired action.
Error Handling: Allows a maximum of three attempts for entering a valid email address. If unsuccessful, the program informs the user and exits.
Separation of Username and Domain: Separates the email address into its username and domain name components based on the user's choice.
Case Insensitivity: Treats domain names case-insensitively by converting them to uppercase for consistency.
