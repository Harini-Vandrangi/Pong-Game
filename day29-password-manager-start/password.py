# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class Password:
    def __init__(self):
        self.password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
        self.password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
        self.password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]
        self.password_list = []
        self.password = self.generate()

    def generate(self):
        self.password_list = self.password_letters + self.password_symbols + self.password_numbers
        random.shuffle(self.password_list)

        password = "".join(self.password_list)

        return password
