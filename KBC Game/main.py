import random
import time

# KBC Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chattopadhyay", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
        "answer": "B"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Sardar Patel", "D. Dr. B.R. Ambedkar"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["A. Amazon River", "B. Nile River", "C. Ganges River", "D. Yangtze River"],
        "answer": "B"
    },
    {
        "question": "Which is the largest continent in the world?",
        "options": ["A. Africa", "B. Asia", "C. Europe", "D. North America"],
        "answer": "B"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A. Albert Einstein", "B. Alexander Graham Bell", "C. Isaac Newton", "D. Thomas Edison"],
        "answer": "B"
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["A. Holi", "B. Diwali", "C. Eid", "D. Christmas"],
        "answer": "B"
    }
]

# Prize Money Levels
prizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 70000000]
guaranteed_amount = 10000  # Amount given if eliminated after a certain point

# Lifeline Usage
lifelines = {"50:50": True, "Phone a Friend": True, "Audience Poll": True, "Ask the Expert": True}

# Function to use 50:50 Lifeline
def use_50_50(question):
    correct_answer = question["answer"]
    wrong_options = [opt for opt in ["A", "B", "C", "D"] if opt != correct_answer]
    remove_two = random.sample(wrong_options, 2)
    remaining_options = [opt for opt in question["options"] if opt.startswith(correct_answer) or opt[:1] not in remove_two]
    return remaining_options

# Function to use Phone a Friend Lifeline
def use_phone_a_friend(question):
    correct_answer = question["answer"]
    options = ["A", "B", "C", "D"]
    if random.random() < 0.8:  # 80% chance of correct answer
        return f"Your friend thinks the correct answer is: {correct_answer}"
    else:
        wrong_guess = random.choice([opt for opt in options if opt != correct_answer])
        return f"Your friend thinks the correct answer is: {wrong_guess}"

# Function to use Audience Poll Lifeline
def use_audience_poll(question):
    correct_answer = question["answer"]
    percentages = {"A": 0, "B": 0, "C": 0, "D": 0}
    percentages[correct_answer] = random.randint(50, 80)  # Majority votes correct answer
    remaining_votes = 100 - percentages[correct_answer]
    for opt in percentages:
        if opt != correct_answer:
            percentages[opt] = random.randint(0, remaining_votes)
            remaining_votes -= percentages[opt]
    return percentages

# Function to use Ask the Expert Lifeline
def use_ask_the_expert(question):
    return f"The expert suggests that the correct answer is: {question['answer']}"

# KBC Game Function
def play_kbc():
    print("🎉 Welcome to Kaun Banega Crorepati! 🎉")
    print("Answer the questions correctly to win up to ₹7 Crore!\n")
    
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1} for ₹{prizes[i]}:")
        print(question["question"])
        for option in question["options"]:
            print(option)

        # Asking for input
        while True:
            print("\nChoose an option (A, B, C, D) or type 'L' for Lifelines or 'Q' to Quit:")
            user_input = input().strip().upper()

            if user_input in ["A", "B", "C", "D"]:
                if user_input == question["answer"]:
                    print(f"✅ Correct! You have won ₹{prizes[i]} 🎉")
                    if i == len(questions) - 1:
                        print("🏆 Congratulations! You are a Crorepati! 🏆")
                        return
                    break
                else:
                    print(f"❌ Wrong! The correct answer was {question['answer']}.")
                    print(f"You leave with ₹{guaranteed_amount if i >= 4 else 0}.")
                    return
            elif user_input == "L":
                print("\nAvailable Lifelines:", [lifeline for lifeline in lifelines if lifelines[lifeline]])
                chosen_lifeline = input("Choose a lifeline: ").strip().title()
                if chosen_lifeline in lifelines and lifelines[chosen_lifeline]:
                    lifelines[chosen_lifeline] = False
                    if chosen_lifeline == "50:50":
                        print("Remaining options:", use_50_50(question))
                    elif chosen_lifeline == "Phone A Friend":
                        print(use_phone_a_friend(question))
                    elif chosen_lifeline == "Audience Poll":
                        print("Audience Poll:", use_audience_poll(question))
                    elif chosen_lifeline == "Ask The Expert":
                        print(use_ask_the_expert(question))
                else:
                    print("Invalid or already used lifeline.")
            elif user_input == "Q":
                print(f"You chose to quit! You leave with ₹{prizes[i-1] if i > 0 else 0}.")
                return
            else:
                print("Invalid choice. Try again.")

# Start the game
play_kbc()
