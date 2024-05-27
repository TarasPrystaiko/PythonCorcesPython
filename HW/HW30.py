from datetime import datetime, timedelta

def get_all_classes(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    classes = []

    current_date = start_date

    while len(classes) < 32:  #
        if current_date.weekday() in [0, 3]:
            classes.append(current_date)
        current_date += timedelta(days=1)

    return classes

def print_classes(classes):
    for i, class_date in enumerate(classes, start=1):
        print(f"Lecture {i:2}: {class_date.strftime('%d %b %Y')} 19:15")

start_date_str = "2024-04-11"

classes = get_all_classes(start_date_str)

print_classes(classes)
