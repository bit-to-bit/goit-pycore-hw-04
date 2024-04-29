'''Task 1 - total_salary()'''
from pathlib import Path

def total_salary(path: str) -> tuple:
    '''Total_salary'''

    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as fh:
            salary_list = [float(el.strip().split(",")[1]) for el in fh.readlines()]
    else:
        raise FileNotFoundError("Invalid file path specified")

    if salary_list:
        sum_salary = 0
        counter = len(salary_list)

        for salary in salary_list:
            sum_salary += salary

        avg_salary = sum_salary / counter

        print(salary_list)

    else:
        sum_salary, avg_salary =  None, None

    return (sum_salary, avg_salary)
