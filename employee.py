def employee_details(name,emp_id,department,salary):
    result=(
        f"Employee Name:{name}\n"
        f"Employee ID:{emp_id}\n"
        f"department:{department}\n"
        f"Employee Salary:{salary}"
    )
    return result

if __name__=="__main__":
    #simple input(you cab change)
    name = "Alice"
    emp_id = "e101"
    department = "IT"
    salary = 55000

    print(employee_details(name, emp_id, department, salary))
    
