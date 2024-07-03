# sum of the marks and average
def calculate_sum_and_average():
    subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]
    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100")
            except ValueError:
                print("Invalid input. Please enter a numeric value")
    total_marks = sum(marks)
    average_marks = total_marks / len(subjects)
    print(f"\nTotal Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")
calculate_sum_and_average()