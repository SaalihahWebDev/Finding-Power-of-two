print(" Let's Learn Powers of 2!")
print("Here are the powers of 2 from 0 to 10:\n")

# Step 1: Show powers of 2
for i in range(11):
    print(f"2^{i} = {2 ** i}")

# Step 2: Simple quiz
print("\n🧠 Time for a Quick Quiz!")
answer = int(input("What is 2 to the power of 3? "))

if answer == 2 ** 3:
    print("🎉 Correct! 2^3 = 8")
else:
    print(f"❌ Oops! The correct answer if {2 ** 3}")