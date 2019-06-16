"""
##  @File: ReadAllocationData.py
#   @Title: ReadAllocationData
#   @Author: Harshil Modi
#   @Date:January 17th 2019
"""
'''
Format of line of readstdnts testfile:
    macid fname lname gender gpa choice1 choice2 choice3
    eg. modih3 harshil2 modi male 7.0 civil electrical chemical
    
Format of line of readFreeChoice textfile:
    macid
    eg. modih1

format of line of readDeptCapacity textfile:
    department_name department_capacity
    eg. civil 10

'''

##  @brief This function takes a string corresponding to a filename and returns a list of dictionary of student information
#   which includes: macid, first_name, last_name, gender, GPA, department_choices.
#   Assumptions: 1) The file must be in the format specified above,
#                2) GPA must be a non-negative float or int.
#   @param S type (String): A filename with student information
#   @return A list of dictionaries of student information

def readStdnts(s):
  
    mac_student = []   
    file = open(s, "r")
    
    for each_line in file:        
        dictionary = {}        
        student = each_line.split(" ")        
        dictionary['macid'] = student[0]
        dictionary['fname'] = student[1]
        dictionary['lname'] = student[2]
        dictionary['gender'] = student[3]
        dictionary['gpa'] = float(student[4])
        dictionary['choice'] = [student[5], student[6], student[7].strip()]        
        mac_student.append(dictionary)
    
    file.close()
    return mac_student

##  @brief This function takes a filename and returns a list of students with free choice.
#   Assumptions: 1) The file must be in the format specified above.
#   @param S type (String): A filename with macid of students with free choice 
#   @return A list student's macid with free choice

def readFreeChoice(s):
    
    free_choice = []    
    file = open(s, "r")
    
    for each_line in file:        
        free_choice.append(each_line.strip())    
    file.close()    
    return free_choice

##  @brief takes a filename and returns a dictionary of departments and their max capacity. 
#   @details Within the dictionary the keys are the department names and their corressponding values are
#   the max department capacity.
#   Assumptions 
#               1) The file must be in the format specified above.
#   @param s type (String): A filename with department names and corressponding max capacities
#   @return A dictionary of department names with their corressponding max capacities
    
def readDeptCapacity(s):
    
    department_capacity = {}    
    file = open(s, "r")
    
    for each_line in file:        
        department = each_line.split(" ")        
        department_capacity[department[0]] = int(department[1])
        
    file.close    
    return department_capacity
        
