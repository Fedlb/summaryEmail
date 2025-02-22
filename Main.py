import random
import time


def periodic_table_game():
    # Dictionary of elements with their types (expanded list)
    elements = {
        'Iron': 'metal',
        'Gold': 'metal',
        'Silver': 'metal',
        'Copper': 'metal',
        'Aluminum': 'metal',
        'Zinc': 'metal',
        'Lead': 'metal',
        'Nickel': 'metal',
        'Platinum': 'metal',
        'Titanium': 'metal',
        'Chromium': 'metal',
        'Tungsten': 'metal',
        'Manganese': 'metal',
        'Cobalt': 'metal',
        'Palladium': 'metal',
        'Tin': 'metal',
        'Iridium': 'metal',
        'Mercury': 'metal',
        'Bismuth': 'metal',
        'Helium': 'gas',
        'Neon': 'gas',
        'Argon': 'gas',
        'Krypton': 'gas',
        'Xenon': 'gas',
        'Radon': 'gas',
        'Hydrogen': 'gas',
        'Nitrogen': 'gas',
        'Oxygen': 'gas',
        'Fluorine': 'gas',
        'Chlorine': 'gas',
        'Bromine': 'gas',
        'Iodine': 'gas',
        'Astatine': 'gas',
        'Carbon dioxide': 'gas'
    }
    
    score = 0
    total_questions = 35
    
    print("Welcome to the Extended Periodic Table Quiz!")
    print("Choose the correct classification for each element.")
    print(f"This quiz contains {total_questions} questions.")
    print("Let's begin!\n")
    
    # Convert dictionary to list of tuples for random selection
    element_list = list(elements.items())
    
    start_time = time.time()
    
    for i in range(total_questions):
        # Select random element
        element, correct_type = random.choice(element_list)
        
        # Generate wrong options
        options = ['metal', 'gas', 'liquid', 'nonmetal']
        if correct_type in options:
            options.remove(correct_type)
        
        # Create answer choices
        choices = [correct_type] + random.sample(options, 3)
        random.shuffle(choices)
        
        # Display question
        print(f"\nQuestion {i+1}/{total_questions}")
        print(f"What is the classification of {element}?")
        for idx, choice in enumerate(['A', 'B', 'C', 'D']):
            print(f"{choice}) {choices[idx]}")
        
        # Get user answer
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Please enter A, B, C, or D")
        
        # Check answer
        user_choice = choices[ord(answer) - ord('A')]
        if user_choice == correct_type:
            print("Correct! ✨")
            score += 1
        else:
            print(f"Wrong! {element} is a {correct_type}.")
        
        # Show progress
        print(f"Current score: {score}/{i+1}")
        time.sleep(0.5)
    
    # Calculate time taken
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    
    # Display final results
    print("\n" + "="*40)
    print("QUIZ COMPLETED!")
    print("="*40)
    print(f"Time taken: {time_taken} seconds")
    print(f"Final score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage}%")
    
    # Performance evaluation
    if percentage == 100:
        print("Perfect score! You're a chemistry master! 🌟")
    elif percentage >= 90:
        print("Outstanding performance! Almost perfect! 🎉")
    elif percentage >= 80:
        print("Great job! You really know your elements! 👍")
    elif percentage >= 70:
        print("Good work! Keep studying! 📚")
    elif percentage >= 60:
        print("Not bad! But there's room for improvement! 💪")
    else:
        print("Keep practicing! You'll get better with time! 🔬")
    
    # Offer to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
    if play_again == 'yes':
        periodic_table_game()

if __name__ == "__main__":
    periodic_table_game()


