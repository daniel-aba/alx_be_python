task = input("Enter a task: ") .strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

reminder_message = ""
time_sensitive_phrase = ""

match priority:
    case "high":
        reminder_message = f"'{task}'is a high priority task."
    case "medium":
        reminder_message = f"'{task}' is a medium priority task."
    case "low":
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = f"'{task}' has an unrecognised priority level ({priority})"

if time_bound == "yes":
    time_sensitive_phrase = "That requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    time_sensitive_phrase = ". Consider completing it when you have free time."
else:
    time_sensitive_phrase = "."

print(f"Reminder: {reminder_message}{time_sensitive_phrase}")