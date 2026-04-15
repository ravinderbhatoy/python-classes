# Stores values in key value pair

# syntax

# {
#   key: value,
#   key1: value1,
# }


student = {
    "name": "Prabh",
    "roll_no": 89,
    "marks": {
        "semester": {
            1: {
                "Aos": 89,
                "OOPS": 78,
                "DSA": 67
            }
        }
    },
    "isMale": True
}

student['pass'] = True

subject = "DSA"
semester = 1

print("Your marks of", subject)
print(student["marks"]["semester"][semester][subject])

print(student.keys())
print(student["marks"].keys())
print(student["marks"]["semester"].keys())

print(student.values())
