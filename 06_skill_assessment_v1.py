# هدف الكود: إدارة مجموعة أسئلة وحساب النتيجة الإجمالية تلقائياً

# 1. بنك الأسئلة (قائمة من القواميس)
questions_bank = [
    {"question": "What is the color of the sky?", "answer": "blue"},
    {"question": "How many legs does a cat have?", "answer": "4"},
    {"question": "Is the sun hot or cold?", "answer": "hot"}
]

final_score = 0

print("--- Starting Child Skill Assessment ---")

# 2. استخدام Loop للمرور على كل سؤال في البنك
for item in questions_bank:
    print(f"\nQuestion: {item['question']}")
    user_input = input("Answer: ").lower().strip()

    # 3. التحقق من الإجابة
    if user_input == item['answer']:
        print("✅ Correct!")
        final_score += 10  # إضافة 10 درجات لكل إجابة صحيحة
    else:
        print(f"❌ Incorrect. The right answer is {item['answer']}")

# 4. النتيجة النهائية
print("\n" + "="*40)
print(f"Assessment Finished!")
print(f"Total Score: {final_score} / {len(questions_bank) * 10}")
print("="*40)
