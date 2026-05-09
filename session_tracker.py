#برنامج لحساب مدة الجلسة التدريبيه للطفل
#هذا البرنامج يطبق مفاهيم المدخلات والمخرجات والعمليات الحسابية
print("---------Autism Session Duration Tracker---------")


# input the data from the user
child_name=input("Enter the Child Name: ")
start_time=int(input("Enter the Start Time: "))
end_time=int(input("Enter the End Time: "))

# the operation
duration = end_time-start_time

# output
print(f"Summary for: {child_name}")
print(f"Total session duration: {duration} minutes.")
