def employee_print(employee_info):
    info = employee_info.copy()
    name = info.pop("Name", "N/A")
    salary = info.pop ("Salary", "N/A")
    role = info.pop ("Role", "N/A")

    print (f"Name: {name}")
    print (f"Salary: {salary}")
    print (f"Role: {role}")

    if len(info) == 0:
        print ("No other info!")
    else:
        for key, value in info.items():
            print(f"{key}: {value}")
