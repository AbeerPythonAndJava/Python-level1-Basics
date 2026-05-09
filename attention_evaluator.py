print("---------Attention Evaluator---------")

# input the data from the user
child_name=input("Enter the Child Name: ")
start_time=int(input("Enter the Start Time: "))
end_time=int(input("Enter the End Time: "))
score_child=int(input("Enter the Score: "))

print(f"Summary for: {child_name}")

# the operation
duration = end_time-start_time
print(f"Total session duration: {duration} minutes.")

if duration < 15:
    print("Session too short")
elif 15 <= duration <= 45 :
    print("Ideal session duration")
else:
    print("Warning: Child might be fatigued")


if 1 <=  score_child <= 4:
    print("(Low Attention - Needs sensory break")
elif 5 <= score_child <=7:
    print("Good Attention - Continue activity")
elif 8 < score_child <=10:
    print("Excellent Attention - Introduce new challenge")

