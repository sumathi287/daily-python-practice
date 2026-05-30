from random import choice as random_choice

RANGE_START = 1
RANGE_END   = 100
GUESS_PROMPTS = [
    "Guess a Number: ",
    # "What did your guess now?",
    # "Want to give up? keep guessing:",
    # "You think you are almost there? Guess now: ",
    # "Are you a god-guesser? What was you guess again? "
]
GUESS_PROMPT_LOWER = [
    "Too Low"
    # "You guessed lower",
    # "That's too low!",
    # "You should be guessing higher!",
    # "Try a bigger number"
]
GUESS_PROMPT_HIGHER = [
    "Too High"
    # "You guessed higher",
    # "That's too high!",
    # "You should be guessing lower!",
    # "Try a smaller number"
]
GAME_QUIT_KEY = 'q'
GAME_QUIT_MESSAGE = "Game quit"
GAME_WIN_MESSAGE = f"congratulations you found the correct number{"\U0001F44F"}{"\U0001F389"}!!!"


class NumberGuesser:
    def __init__(self):
        self.guess_range = range(RANGE_START, RANGE_END)
        self.target_number = random_choice(self.guess_range)
        self.__game_end = False

    def disp_console(self):
        print(
            f"---------------------------------\n"
            f"------NUMBER GUESSING GAME-------\n"
            f"---------------------------------\n"
            f"***Rules of the Game: *** Guess a number!\n"
            f"If you want to quit, Enter 'q', else keep guessing a number between {RANGE_START} - {RANGE_END} 😉\n\n"
        )

    def play(self):
        self.disp_console()

        while(not self.__game_end):
            self.user_guess = input(random_choice(GUESS_PROMPTS))
            if GAME_QUIT_KEY in self.user_guess.lower():
                return GAME_QUIT_MESSAGE
            self.user_guess = int(self.user_guess)
            self.__game_end = True if self.user_guess == (self.target_number) else False
            if self.__game_end:
                break
            hint_prompt = random_choice(GUESS_PROMPT_LOWER) if self.user_guess < self.target_number else random_choice(GUESS_PROMPT_HIGHER)
            print(f"{hint_prompt}")
            
        return GAME_WIN_MESSAGE



def play():
    game_console = NumberGuesser()
    game_return = game_console.play()
    # if GAME_QUIT_KEY in game_return.lower():
    print(game_return)


if __name__ == "__main__":
    play()

