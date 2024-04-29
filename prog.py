import pickle #IMPORT THE MODULE THAT CAN WRITE A LIST INTO BINARY
#LIST OF STUDENTS AND THEIR GWA, GWA MUST BE WRITTEN FIRST
students_list = [(1.50, 'Laron'), (1.50, 'Pedro'), (1.75, 'Jirald'), (1.75, 'Karding'), (1.25, 'James'), 
                 (1.08, 'Grego'), (1.15, 'Charles'), (1.03, 'Juswa'), (2.50, 'Justin'), (2.75, 'Clark'), 
                 (3.00, 'Clint'), (2.30, 'Michael'), (1.50, 'Juan'), (3.00, 'Ricar'), (2.50, 'Anna'), 
                 (1.12, 'Jiro'), (2.30, 'Quince'), (1.15, 'Kin'), (1.60, 'Prince'), (1.50, 'Gan')]
with open("binary.txt", "wb") as file: #OPEN FUNCTION THAT CLOSES ITSELF, WRITES THE LIST AS BINARY INTO THE FILE
    pickle.dump(students_list, file)
with open("binary.txt", "rb") as file: #OPENING THE FILE IN READING BINARY MODE TO CONVERT BINARY INTO LIST 
    new_students = pickle.load(file)
student = min(new_students) #GETTING THE LOWEST VALUE FOR THE HIGHEST GWA
print(f"The student who got the highest grade is {student[1]}, with a {student[0]} GWA")
 
