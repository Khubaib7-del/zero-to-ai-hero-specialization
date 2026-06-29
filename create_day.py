import os
import sys

# Mapping of course numbers to folder names
COURSES = {
    1: "Course-1_Foundations of AI Engineering",
    2: "Course-2_Core Machine Learning & Evaluation",
    3: "Course-3_Deep Learning & Modern AI Architecture"
}

SPECIALIZATION_DIR = "AI Engineering Masterclass From Zero to AI Hero"

def print_usage():
    print("\n[Usage]: python create_day.py <course_number> <week_number> <day_number>")
    print("Example: python create_day.py 1 1 1")
    print("This will create directories and template files for Course 1, Week 1, Day 1.\n")

def main():
    # If not enough arguments are passed, prompt interactively
    if len(sys.argv) < 4:
        print("--- Coursera File Organizer ---")
        try:
            print("Select Course:")
            for num, name in COURSES.items():
                print(f"  {num}: {name.split('_')[1]}")
            course_num = int(input("Enter Course Number (1-3): "))
            if course_num not in COURSES:
                print("❌ Invalid course number.")
                return

            week_num = int(input("Enter Week Number (e.g., 1): "))
            day_num = int(input("Enter Day Number (e.g., 1): "))
        except ValueError:
            print("❌ Input must be a valid number.")
            print_usage()
            return
    else:
        try:
            course_num = int(sys.argv[1])
            week_num = int(sys.argv[2])
            day_num = int(sys.argv[3])
        except ValueError:
            print("❌ Arguments must be numbers.")
            print_usage()
            return

    if course_num not in COURSES:
        print(f"❌ Course number {course_num} not found. Must be 1, 2, or 3.")
        return

    course_folder = COURSES[course_num]
    week_folder = f"Week-{week_num}"
    day_folder = f"Day-{day_num}"

    # Construct paths
    target_dir = os.path.join(SPECIALIZATION_DIR, course_folder, week_folder, day_folder)
    
    # Create directories
    os.makedirs(target_dir, exist_ok=True)
    print(f"\n[Dir] Directory created/verified: {target_dir}")

    # Create template Python file
    py_filepath = os.path.join(target_dir, "main.py")
    if not os.path.exists(py_filepath):
        with open(py_filepath, 'w', encoding='utf-8') as f:
            f.write(f'"""\nCoursera Specialization: {SPECIALIZATION_DIR}\nCourse: {course_folder.split("_")[1]}\n{week_folder} | {day_folder}\n"""\n\ndef main():\n    print("Hello from {week_folder}, {day_folder}!")\n\nif __name__ == "__main__":\n    main()\n')
        print(f"[File] Created template Python file: {py_filepath}")
    else:
        print(f"[Info] {py_filepath} already exists. Skipping.")

    print(f"\n[Success] Ready to code! You can also place your notes.docx file inside:")
    print(f"   {target_dir}\n")

if __name__ == "__main__":
    main()
