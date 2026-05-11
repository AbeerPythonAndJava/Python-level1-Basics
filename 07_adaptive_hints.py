# هدف الكود: جعل النظام يتكيف مع تعثر الطفل بإعطائه تلميحاً وفرصة ثانية

# 1. بنك أسئلة مطور يحتوي على مفتاح جديد "hint"
questions_bank = [
    {
        "question": "What animal has a long trunk?",
        "answer": "elephant",
        "hint": "It is a very big grey animal!"
    },
    {
        "question": "What is the color of a banana?",
        "answer": "yellow",
        "hint": "It is the same color as the sun."
    }
]

final_score = 0

print("--- Starting Adaptive Assessment with Hints ---")

for item in questions_bank:
    print(f"\nQuestion: {item['question']}")
    attempt = input("Your answer: ").lower().strip()

    # المحاولة الأولى
    if attempt == item['answer']:
        print("🌟 Excellent! Correct from the first time.")
        final_score += 10
    else:
        # هنا يبدأ النظام التكيفي: إعطاء تلميح وفرصة ثانية
        print(f"💡 Hint: {item['hint']}")
        second_attempt = input("Try again: ").lower().strip()

        if second_attempt == item['answer']:
            print("👏 Good job! You got it after the hint.")
            final_score += 5  # درجة أقل لأنه احتاج مساعدة
        else:
            print(f"❌ Hard luck. The answer was {item['answer']}.")

print(f"\nTotal Score: {final_score}")
