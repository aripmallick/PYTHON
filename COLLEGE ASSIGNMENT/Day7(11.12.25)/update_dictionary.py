employees = {
    1: {'name': 'Arip', 'age': 20, 'salary': 10000},
    2: {'name': 'Simi', 'age': 20, 'salary': 20000},
    3: {'name': 'Fahim', 'age': 22, 'salary': 30000}
}

def give_hike(emp):
    for k in emp:
        emp[k]['salary'] += emp[k]['salary'] * 0.10
    return emp

updated = give_hike(employees)
print(updated)
