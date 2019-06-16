"""
##@File: CalcModule.py
#@Title: Calcmodule
#@Author: Harshil Modi
#@Date:January 17th 2019
"""
import ReadAllocationData # importing file ReadAllocationData.py

## @brief This function sorts the students in non ascending GPA. 
#  @Details The function uses a self-made sorting algorithm to sort the dictionary created in readStdnts(s).  
#  @param S A list of dictionaries of student information
#  @return A list of dictionaries of student information in non ascending GPA order

def sort(S):
    
    mac_student = S
    new_list = [] #output list
    
    for student in mac_student:       
        insert = False  #To keep track if the student was inputted
        
        for i in range(len(new_list)):
            new_student = new_list[i]
            
            if new_student['gpa'] < student['gpa']:
                new_list.insert(i,student)
                insert = True
                break
        
        if not insert:
            new_list.append(student)
      
    return new_list

## @brief This function finds the average GPA of females or males.
#  @details If parameter g is 'male' the average GPA of all males is calculated and vice versa.
#  Assumption: 1) parameter g must be either 'male' or 'female'.    
#  @param L: A list of dictionaries of student information created by readFreeChoice(s)
#  @param g type (String): A string representing the gender male or female
#  @return Average GPA of females or males rounded to 2 decimal places

def average(L, g):
    
    sum = 0  #counter to track sum GPA
    count = 0  #number of students counted
    
    for student in L:
        
        if student['gender'] == g:
            sum += student['gpa']
            count +=1
        else:
            continue
    
    if count == 0: #error check for students equals zero
        return 0
    
    return round(sum/count, 2)

## @brief This function allocates students to second-year programs with GPA OVER 4.0
#  @details The function first allocates all the students with free choice to their respected first choice programs.
#   Next the function begins allocating students from highest GPA to lowest GPA to their respected choices. If the
#   students first choice department is full, they will be allocated to their second choice. If that is also full, they
#   will be allocated to their last choice.
#   Assumptions: 1) The number of students with free choice and first choice to a particular department does not exceed the department capacity,
#                2) If the first choice and second choice of a student is full, third choice must not be full,
#                3) students with GPA of 4.0 are not allocated to second-year,
#                4) A case where 2 students having the same gpa and one space left will not be present.       
#  @param S: A list of dictionaries of student information created in readStdnts()
#  @param F: A list of students with free choice created in readFreeChoice(s)
#  @param C: A dictionary of department capacity created in readDeptCapacity(s)
#  @return Dictionary of which students have been allocated to which department

def allocate(S, F, C):
    
    department_dictionary  = {'civil':[], 'chemical':[], 'electrical':[], 'mechanical':[], 'software': [], 'materials': [], 'engphys':[]}
    
    #allocates students with freechoice first   
    for student in S:        
        if student['macid'] in F and student['gpa'] > 4.0:     
            department_students = department_dictionary[student['choices'][0]]
            department_students.append(student)
            department_dictionary[student['choices'][0]] = department_students
    
    S = sort(S) # sorts the students based on GPA
    
    # allocates the students without free choice
    for student in S:        
        if student['macid'] not in F and student['gpa'] > 4.0:
            
            if len(department_dictionary[student['choices'][0]]) < C[student['choices'][0]]:                                
                department_students = department_dictionary[student['choices'][0]]
                department_students.append(student)
                department_dictionary[student['choices'][0]] = department_students
            
            elif len(department_dictionary[student['choices'][1]]) < C[student['choices'][1]]:
                department_students = department_dictionary[student['choices'][1]]
                department_students.append(student)
                department_dictionary[student['choices'][1]] = department_students
            
            else:                
                department_students = department_dictionary[student['choices'][2]]
                department_students.append(student)
                department_dictionary[student['choices'][2]] = department_students
        
        else:
            continue
                           
    return (department_dictionary)
    