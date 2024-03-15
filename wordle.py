import requests
import random

class WordleGame:
    def __init__(self):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        words = response.content.decode().split('\n')
        self.five_letter_words = [word for word in words if len(word) == 5]
        self.target_word = random.choice(self.five_letter_words)
        self.max_attempts = 6
        self.attempts = 0

    def target_word_dictionary(self):
        letter_dictionary = {}
        for char in self.target_word:
            letter_dictionary[char] = letter_dictionary.get(char, 0) + 1
        return letter_dictionary

    def is_correct_guess(self, guess):
        return guess == self.target_word

    def give_feedback(self, guess):
        target_dict = self.target_word_dictionary()
        feedback = []
        for i in range(len(guess)):
            if guess[i] == self.target_word[i]:
                feedback.append('G')  # Green for correct letter and position
                target_dict[guess[i]] -= 1
            elif guess[i] in self.target_word and target_dict[guess[i]] > 0:
                feedback.append('Y')  # Yellow for correct letter but wrong position
                target_dict[guess[i]] -= 1
            else:
                feedback.append('B')  # Black for incorrect letter
        return [*guess], feedback

    def play(self):
        while self.attempts < self.max_attempts:
            user_guess = input("Enter your 5-letter guess: ").lower()

            if len(user_guess) != 5 or not user_guess.isalpha():
                print("Invalid input. Please enter a 5-letter word.")
                continue

            if user_guess not in self.five_letter_words:
                print("Word not in list. Please try a different word.")
                continue

            self.attempts += 1  # Increment only for valid guesses
            guess, feedback = self.give_feedback(user_guess)
            print(' '.join(guess))
            print(' '.join(feedback))

            if self.is_correct_guess(user_guess):
                print("Congratulations! You've guessed the word correctly.")
                break

        if not self.is_correct_guess(user_guess):
            print(f"Sorry, you've used all your attempts. The word was: {self.target_word}")

# To play the game, create an instance of the WordleGame class and call the play method
if __name__ == "__main__":
    game = WordleGame()
    game.play()
