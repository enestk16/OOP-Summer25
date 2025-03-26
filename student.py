student1={
    "first_name":"enes talha",
    "last_name":"kanar",
    "index_number":35375,
    "nationality":"turkish",
    "starting_date":"13/09/2024",
    "courses":["basics of marketing"]
}
print(student1["first_name"],student1["last_name"],student1["index_number"],student1["nationality"],student1["starting_date"],student1["courses"])

student2={
    "first_name":"jason",
    "last_name":"jones",
    "index_number":45678,
    "nationality":"american",
    "starting_date":"13/09/2024",
    "courses":["english","pyhsics"]
}
print(student2["first_name"],student2["last_name"],student2["index_number"],student2["nationality"],student2["starting_date"],student2["courses"])

student3={
    "first_name":"mackenzie",
    "last_name":"darla",
    "index_number":45723,
    "nationality":"british",
    "starting_date":"13/09/2024",
    "courses":["basics of chemistry"]
}
print(student3["first_name"],student3["last_name"],student3["index_number"],student3["nationality"],student3["starting_date"],student3["courses"])

def new_students_add(first_name,last_name,index_number,nationality,starting_date,courses):
    student = {'first_name':first_name,'last_name':last_name,'index_number':index_number,'nationality':nationality,'starting_date':starting_date,'courses':courses}
    student.append(student)
    print(first_name + " " + last_name + " " + index_number + " " + nationality + " " + starting_date + " " + courses)