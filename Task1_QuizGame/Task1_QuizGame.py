# Task 1: Text-based Quiz Game
# Objective: Implement a simple game using conditional statements.


print("   Welcome to the Ultimate Quiz Game!  ")

print("Answer the following questions by typing A, B, C, or D.\n")


score = 0


print("Question 1: Which programming language is most commonly paired with Selenium for test automation?")
print("A) HTML")
print("B) Python")
print("C) CSS")
print("D) SQL")
answer1 = input("Your answer: ").strip().upper()


if answer1 == 'B':
    print("✅ Correct! Python's simple syntax makes it a favorite for automation.")
    score += 1
else:
    print("❌ Incorrect! The correct answer is B (Python).")

print("\n---------------------------------------")


print("Question 2: In Physics, what is the standard SI unit of Force?")
print("A) Joule")
print("B) Watt")
print("C) Newton")
print("D) Pascal")
answer2 = input("Your answer: ").strip().upper()

if answer2 == 'C':
    print("✅ Correct! Force is measured in Newtons.")
    score += 1
else:
    print("❌ Incorrect! The correct answer is C (Newton).")

print("\n---------------------------------------")


print("Question 3: Which material is commonly applied as a protective layer or edge reinforcement on a cricket bat?")
print("A) Fiber tape")
print("B) Aluminum foil")
print("C) Sandpaper")
print("D) Teflon coating")
answer3 = input("Your answer: ").strip().upper()

if answer3 == 'A':
    print("✅ Correct! Fiber tape is widely used to prevent edge damage and enhance durability.")
    score += 1
else:
    print("❌ Incorrect! The correct answer is A (Fiber tape).")

print("\n=======================================")

print(f"Game Over! Your final score is {score} out of 3.")

if score == 3:
    print("🏆 Excellent work! You got a perfect score!")
elif score == 2:
    print("👍 Good job! Just one mistake.")
elif score == 1:
    print("📚 Not bad, but there's room for improvement.")
else:
    print("😅 Better luck next time! Keep practicing.")