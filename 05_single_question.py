# هدف الكود: بناء أول وحدة تفاعلية (سؤال وإجابة)

# 1. إنشاء قاموس يحتوي على السؤال وإجابته
quiz_data = {
    "question": "Which animal says 'Meow'?",
    "correct_answer": "cat"
}

print("--- Welcome to the Interaction Level ---")

# 2. عرض السؤال على الطفل
print(quiz_data["question"])
child_answer = input("Your answer: ").lower().strip() # تحويل النص لصغير وحذف المسافات لضمان الدقة

# 3. مخ البرنامج يقارن الإجابة
if child_answer == quiz_data["correct_answer"]:
    print("🌟 Brilliant! Correct Answer.")
    score = 10
else:
    print(f"Oops! The correct answer was: {quiz_data['correct_answer']}")
    score = 0

print(f"Score for this task: {score}")
