from datetime import datetime, timedelta

def get_all_classes(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    classes = []

    # Adjust the starting date to the first class (April 11, 2024)
    current_date = start_date

    # Generate the class dates
    while len(classes) < 32:  # Adjust the number of classes needed
        if current_date.weekday() in [0, 3]:  # Monday (0) or Thursday (3)
            classes.append(current_date)
        current_date += timedelta(days=1)

    return classes

def print_classes(classes):
    for i, class_date in enumerate(classes, start=1):
        print(f"Lecture {i:2}: {class_date.strftime('%d %b %Y')} 19:15")

# Define the start date
start_date_str = "2024-04-11"

# Get all class dates
classes = get_all_classes(start_date_str)

# Print all class dates
print_classes(classes)
