import random


class Guess:
    def __init__(self):
        self.seed = ""
        self.trial = 0
        self.initSeed()

    def checkNumber(self, number):
        self.trial += 1
        if number.isnumeric():
            nb = int(number)
            if nb > self.seed:
                print('Too high')
            elif nb < self.seed:
                print('Too low')
            else:
                if self.trial == 1:
                    print('Congratulations! You got it on your first try!')
                if self.seed == 42:
                    ans = "The answer to the ultimate of life"
                    ans += "the universe and everything is 42"
                    print(ans)
                else:
                    print('You won in ', self.trial, 'attemps!')
                    print("Let's play again")
                self.initSeed()
        elif number == 'exit':
            print('Good bye!')
            exit()
        else:
            print("That's not a number.")

    def initSeed(self):
        self.seed = random.randint(1, 99)
        self.trial = 0


def main():
    print('This is an interactive guessing game!')
    rule = 'You have to enter a number between'
    rule += ' 1 and 99 to find out the secret number.'
    print(rule)
    print("Type 'exit' to end the game.")
    print('Good Luck')
    game = Guess()
    try:
        while True:
            number = input("What's your guess between 1 and 99\n>> ")
            game.checkNumber(number)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
