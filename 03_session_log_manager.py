# قائمة تحتوي على درجات انتباه الطفل في جلسات سابقة
attention_history = [6, 8, 5, 9, 7]

print(f"Current History: {attention_history}")

# إضافة درجة جديدة (اليوم)
new_score = int(input("Enter today's attention score (1-10): "))
attention_history.append(new_score)

# حساب عدد الجلسات
total_sessions = len(attention_history)

# حساب المتوسط الحسابي (مهم جداً للبحث العلمي)

average_score = sum(attention_history)/ total_sessions

print(f"\nTotal sessions logged: {total_sessions}")
print(f"Updated History: {attention_history}")
print(f"Average Performance: {average_score:.2f}")
