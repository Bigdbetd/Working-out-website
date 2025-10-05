import random

# workout schedule dictionary
workout_schedule = {
    "monday": "Chest and Triceps",
    "tuesday": "Shoulders",
    "wednesday": "Legs",
    "thursday": "Back and Biceps",
    "friday": "Core",
    "saturday": "Rest day - take a break",
    "sunday": "Legs"
}

# list of encouragement phrases
encouragements = [
    "Good job showing up today.",
    "You are getting stronger every day.",
    "Stay consistent and keep working.",
    "Push yourself a little more this time.",
    "You are making progress, keep going."
]

workout_count = 0

def get_workout(day):
    # looks up the workout for the given day
    return workout_schedule.get(day.lower(), "That is not a valid day. Try again.")

def get_encouragement():
    # picks a random encouragement from the list
    return random.choice(encouragements)

def main():
    global workout_count
    print("Welcome to your Workout Companion Chatbot!")
    name = input("What is your name? ")
    print("Hello " + name + ". Type 'quit' anytime to stop.")

    while True:
        day = input("What day is it today? ")
        if day.lower() == "quit":
            print("You worked out " + str(workout_count) + " times this week. Goodbye " + name + "!")
            break

        workout = get_workout(day)
        print("Today's workout: " + workout)

        if "Rest" not in workout:
            workout_count += 1
            print(get_encouragement())
        else:
            print("Enjoy your rest day.")

main()
