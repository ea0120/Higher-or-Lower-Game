from game.card import Card

class Director:
    """The class who directs the game.
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.total_points = 300
        self.is_playing = True
        self.userChoice = ''
        self.card = Card()
        self.currentCard = 0
        self.nextCard = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.show_player_card()
            self.get_user_answer()
            self.choose_next_card()
            self.calculatePoints()
            self.playAgain()

    def show_player_card(self):
        """Show user first card.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        #Pick Random Card
        self.card.pick()
        #Store the card value
        self.currentCard = self.card.value
        #Display the card to the user
        print("The card is: " + str(self.currentCard))

    def get_user_answer(self):
        """Ask the user if the next card is higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        self.userChoice = input("Higher or lower? [h/l] ")
        if self.userChoice != 'h' and self.userChoice != 'l':
            print("Please enter h or l.")
            self.get_user_answer()

    def choose_next_card(self):
        """Choose next card to compare.

        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return 

        #Pick Random Card
        self.card.pick()
        #Store the card value
        self.nextCard = self.card.value
        #Display the next card to the user
        print("Next card is: " + str(self.nextCard))

    def calculatePoints(self):
        """Calculate and display points.
            If player is right add 100 points.
            If player is wrong remove 75 points.
            If points go below 0 game over. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        #if was lower
        #print(str(self.currentCard) + ',' + str(self.nextCard))
        if self.currentCard > self.nextCard:
            #print("It was lower")
            if self.userChoice == 'l':
                self.total_points += 100
            else:
                self.total_points -= 75
        
        if self.currentCard < self.nextCard:
            #print("It was higher")
            if self.userChoice == 'h':
                self.total_points += 100
            else:
                self.total_points -= 75

        print("Your score is: " + str(self.total_points))

        if self.total_points <= 0:
            print("You Loose, Game Over!!!")
    
    def playAgain(self):
        """Ask user if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        again = input("Play again? [y/n] ")
        if again != 'y' and again != 'n':
            print("Please enter y or n.")
            self.playAgain()
        if again == 'n':
            self.is_playing = False