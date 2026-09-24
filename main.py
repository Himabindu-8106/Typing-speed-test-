import time
import random

sentences = [
    "Python is an easy and powerful programming language.",
    "Practice makes you better at typing every day.",
    "Learning Python can help you build amazing projects.",
    "Programming requires patience and regular practice.",
    "Technology is changing the way we live and work."
]

sentence = random.choice(sentences)

print("=" * 50)
print("        TYPING SPEED TEST")
print("=" * 50)

print("\nType the following sentence:")
print("\n" + sentence)

input("\nPress Enter when you are ready...")

print("\nStart typing!")

start_time = time.time()

user_input = input("\nYour typing: ")

end_time = time.time()

# Calculate time
time_taken = end_time - start_time

# Calculate words per minute
words = len(user_input.split())
wpm = (words / time_taken) * 60

# Calculate accuracy
correct_characters = 0

for i in range(min(len(sentence), len(user_input))):
    if sentence[i] == user_input[i]:
        correct_characters += 1

accuracy = (correct_characters / len(sentence)) * 100

# Display results
print("\n" + "=" * 50)
print("              RESULTS")
print("=" * 50)

print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Speed      : {wpm:.2f} WPM")
print(f"Accuracy   : {accuracy:.2f}%")

if accuracy >= 90:
    print("Excellent typing!")
elif accuracy >= 70:
    print("Good job! Keep practicing.")
else:
    print("Keep practicing to improve.")

print("=" * 50)