'''Test module for Task 1'''
import salary

WRONG_PATH = "non-existent-file.txt"
TEST_PATH = ["storage/task-01-test-01.txt",
             "storage/task-01-test-02.txt",
             "storage/task-01-test-03.txt"
            ]

for salary_file in TEST_PATH:
    total, average = salary.total_salary(salary_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# total, average = salary.total_salary(WRONG_PATH)
