import random

# ---------------------------
# Data
# ---------------------------

# Workout schedule for each day
workout_schedule = {
    "monday": "Chest and Triceps",
    "tuesday": "Shoulders",
    "wednesday": "Legs",
    "thursday": "Back and Biceps",
    "friday": "Core",
    "saturday": "Rest day - take a break",
    "sunday": "Legs"
}

# Encouragement messages
encouragements = [
    "Good job showing up today.",
    "You are getting stronger every day.",
    "Stay consistent and keep working.",
    "Push yourself a little more this time.",
    "You are making progress, keep going."
]

# Track workouts per day
workout_log = {
    "monday": 0,
    "tuesday": 0,
    "wednesday": 0,
    "thursday": 0,
    "friday": 0,
    "saturday": 0,
    "sunday": 0
}

# ---------------------------
# Functions
# ---------------------------

def get_workout(day):
    """Return the workout for the given day"""
    return workout_schedule.get(day.lower(), None)

def get_encouragement():
    """Return a random encouragement message"""
    return random.choice(encouragements)

def track_workout(day):
    """Increase workout count for the day if not rest day"""
    if "Rest" not in workout_schedule[day]:
        workout_log[day] += 1
        return True
    return False

def show_summary(name):
    """Print the weekly workout summary"""
    total = sum(workout_log.values())
    print(f"\n{name}, here's your weekly workout summary:")
    for day, count in workout_log.items():
        print(f"{day.title()}: {count} workout(s)")
    print(f"Total workouts this week: {total}")
    print("Keep it up!")

def main():
    """Main chatbot loop"""
    print("Welcome to your Workout Companion Chatbot!")
    name = input("What is your name? ").strip()
    print(f"Hello {name}! Type 'quit' anytime to stop or 'schedule' to see the weekly plan.\n")

    while True:
        day_input = input("What day is it today? ").strip().lower()

        # Quit the chatbot
        if day_input == "quit":
            show_summary(name)
            print(f"Goodbye {name}!")
            break

        # Show full weekly schedule
        if day_input == "schedule":
            print("\nWeekly Workout Schedule:")
            for d, w in workout_schedule.items():
                print(f"{d.title()}: {w}")
            print("")
            continue

        # Validate day input
        if day_input not in workout_schedule:
            print("Invalid day. Try again or type 'schedule' to see all days.\n")
            continue

        # Show today's workout
        workout = get_workout(day_input)
        print(f"Today's workout: {workout}")

        # Track workout and give encouragement
        if track_workout(day_input):
            print(get_encouragement())
        else:
            print("Enjoy your rest day!\n")

# ---------------------------
# Run Chatbot
# ---------------------------
if __name__ == "__main__":
    main()
