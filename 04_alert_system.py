# هدف الكود: فحص قائمة الدرجات تلقائياً وتنبيهنا للأيام الضعيفة

weekly_scores = [8, 9, 4, 7, 3, 10, 5]

print("Starting Weekly Check...")

# هنا يبدأ التكرار (Loop)
for score in weekly_scores:
    if score < 5:
        print(f"⚠️ Alert: A low score of ({score}) was detected! Needs attention.")
    else:
        print(f"✅ Score ({score}) is acceptable.")

print("Weekly Check Completed.")
