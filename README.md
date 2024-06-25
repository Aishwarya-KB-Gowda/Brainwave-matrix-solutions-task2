



# Password Strength Checker

Welcome to the Password Strength Checker project! This tool is designed to help users assess the strength of their passwords by analyzing various factors such as length, complexity, and uniqueness. It provides immediate feedback on the entered password's strength, helping users create more secure passwords.

### Repository URL:
[Brainwave Matrix Solutions Task 2](https://github.com/Aishwarya-KB-Gowda/Brainwave-matrix-solutions-task2)

### File Name:
`pass.py`

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Algorithm Explanation](#algorithm-explanation)
6. [Example Outputs](#example-outputs)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Overview

The **Password Strength Checker** is a Python-based tool that evaluates passwords based on various criteria and provides feedback on their strength. This tool is ideal for users who want to improve their password security. It considers the length of the password, the presence of different character types (lowercase, uppercase, digits, and special characters), and assigns a strength rating from "Very Weak" to "Very Strong".

---

## Features

- **Length Analysis**: Evaluates the length of the password and how it contributes to its strength.
- **Complexity Analysis**: Checks for the presence of lowercase letters, uppercase letters, digits, and special characters.
- **Strength Feedback**: Provides a rating for the password's strength ranging from "Very Weak" to "Very Strong".
- **Simple and Interactive**: Easy to use, prompting users for input and displaying results directly.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Aishwarya-KB-Gowda/Brainwave-matrix-solutions-task2.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Brainwave-matrix-solutions-task2
   ```

---

## Usage

1. **Run the Script**:
   ```bash
   python pass.py
   ```

2. **Enter a Password**:
   - The script will prompt you to enter a password.
   - Enter the password you want to check and press Enter.

3. **Receive Feedback**:
   - The tool will analyze your password and print out its strength.

---

## Algorithm Explanation

The `password_strength_check` function in `pass.py` evaluates the password based on the following criteria:

1. **Length**:
   - Less than 8 characters: **Very Weak**
   - 8-11 characters: Adds 1 to the strength score.
   - 12-15 characters: Adds 2 to the strength score.
   - 16 or more characters: Adds 3 to the strength score.

2. **Complexity**:
   - Contains lowercase letters: Adds 1 to the strength score.
   - Contains uppercase letters: Adds 1 to the strength score.
   - Contains digits: Adds 1 to the strength score.
   - Contains special characters (e.g., `!@#$%^&*()_+=-{}[]:;'\"<>,./?~`): Adds 1 to the strength score.

3. **Strength Levels**:
   - Total score 1: **Weak**
   - Total score 2 or 3: **Medium**
   - Total score 4: **Strong**
   - Total score 5 or higher: **Very Strong**

---

## Example Outputs

1. **Password**: `123456`
   - **Strength**: `Very Weak`
   
2. **Password**: `Password123`
   - **Strength**: `Medium`
   
3. **Password**: `StrongPass!123`
   - **Strength**: `Very Strong`

4. **Password**: `Short!`
   - **Strength**: `Very Weak`

5. **Password**: `LongAndComplex1!`
   - **Strength**: `Very Strong`

---

## Contributing

Contributions to enhance the Password Strength Checker are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Aishwarya-KB-Gowda/Brainwave-matrix-solutions-task2/blob/main/LICENSE) file for details.

---

## Contact

For any inquiries or issues, please contact [Aishwarya K B Gowda](https://github.com/Aishwarya-KB-Gowda).

---

Thank you for using the Password Strength Checker! Your feedback is appreciated and will help us improve the tool.

---
