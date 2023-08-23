squared = {data: data**2 for data in range (1, 13) }
print(squared)  #  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

student_list = [("name", "jon"), ("age", 25), ("address", "KTM")]
student = {key: value for key, value in student_list}
print(student)