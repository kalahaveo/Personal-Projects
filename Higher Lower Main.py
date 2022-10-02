from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def check_followers(followers_A, followers_B, user_choice):
    if followers_A > followers_B:
        return user_choice == "a"
    else:
        return user_choice =="b"

def game():
    should_continue = True
    user_score = 0
    print(logo)
    # Chose a random person from game_data
    person_A = random.choice(data)
    person_B = random.choice(data)
    while should_continue:
        person_A = person_B
        person_B = random.choice(data)
        # Make sure choices aren't the same
        while person_A == person_B:
            person_B = random.choice(data)
        
        print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}.")
        print(vs)
        print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}.")
        
        # Input choice
        user_choice = input("Who has more followers? Type 'A' or type 'B': ").lower()
        # Compare choices
        followers_A = person_A['follower_count']
        followers_B = person_B['follower_count']
        is_correct = check_followers(followers_A, followers_B, user_choice)
        clear()
        print(logo)
        if is_correct:
            user_score += 1
            print(f"You're right! Current score is {user_score}")
        else:
            print(f"Wrong. Final score: {user_score}")
            should_continue = False
        
game()



    
