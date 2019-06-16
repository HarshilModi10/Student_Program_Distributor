"""
##  @File: testCalc.py
#   @Title: testCalc
#   @Author: Harshil Modi
#   @Date:January 17th 2019
"""

import CalcModule
import ReadAllocationData

#Test case to check if the sort function can sort large datasets
def test_sort():
    S = ReadAllocationData.readStdnts("textfile.txt")
    sort = CalcModule.sort(S)
    assert sort == [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih23', 'fname': 'harshil22', 'lname': 'modi', 'gender': 'male', 'gpa': 11.5, 'choice': ['software', 'electrical', 'chemical']}, 
                     {'macid': 'modih18', 'fname': 'harshil17', 'lname': 'modi1', 'gender': 'female', 'gpa': 11.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih17', 'fname': 'harshil16', 'lname': 'modi', 'gender': 'male', 'gpa': 10.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih21', 'fname': 'harshil20', 'lname': 'modi', 'gender': 'male', 'gpa': 9.3, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih9', 'fname': 'harshil8', 'lname': 'modi', 'gender': 'male', 'gpa': 9.2, 'choice': ['chemical', 'engphys', 'software']}, 
                     {'macid': 'modih16', 'fname': 'harshil15', 'lname': 'modi', 'gender': 'female', 'gpa': 9.0, 'choice': ['chemical', 'engphys', 'software']}, 
                     {'macid': 'modih5', 'fname': 'harshil4', 'lname': 'modi', 'gender': 'male', 'gpa': 8.5, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih22', 'fname': 'harshil21', 'lname': 'modi1', 'gender': 'female', 'gpa': 8.2, 'choice': ['electrical', 'software', 'mechanical']}, 
                     {'macid': 'modih15', 'fname': 'harshil14', 'lname': 'modi', 'gender': 'male', 'gpa': 8.0, 'choice': ['civil', 'electrical', 'chemical']}, 
                     {'macid': 'modih20', 'fname': 'harshil19', 'lname': 'modi', 'gender': 'male', 'gpa': 7.9, 'choice': ['engphys', 'electrical', 'mechanical']}, 
                     {'macid': 'modih6', 'fname': 'harshil5', 'lname': 'modi1', 'gender': 'female', 'gpa': 7.5, 'choice': ['electrical', 'sofware', 'mechanical']}, 
                     {'macid': 'modih19', 'fname': 'harshil18', 'lname': 'modi', 'gender': 'female', 'gpa': 7.4, 'choice': ['civil', 'electrical', 'chemical']}, 
                     {'macid': 'modih3', 'fname': 'harshil2', 'lname': 'modi', 'gender': 'male', 'gpa': 7.0, 'choice': ['civil', 'electrical', 'chemical']}, 
                     {'macid': 'modih12', 'fname': 'harshil11', 'lname': 'modi', 'gender': 'female', 'gpa': 7.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih10', 'fname': 'harshil9', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.8, 'choice': ['electrical', 'software', 'mechanical']}, 
                     {'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}, 
                     {'macid': 'modih7', 'fname': 'harshil6', 'lname': 'modi', 'gender': 'male', 'gpa': 5.3, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih4', 'fname': 'harshil3', 'lname': 'modi', 'gender': 'male', 'gpa': 5.0, 'choice': ['chemical', 'engphys', 'software']}, 
                     {'macid': 'modih8', 'fname': 'harshil7', 'lname': 'modi', 'gender': 'male', 'gpa': 5.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih24', 'fname': 'harshil23', 'lname': 'modi', 'gender': 'female', 'gpa': 5.0, 'choice': ['chemical', 'engphys', 'software']}, 
                     {'macid': 'modih14', 'fname': 'harshil13', 'lname': 'modi1', 'gender': 'female', 'gpa': 4.0, 'choice': ['electrical', 'software', 'mechanical']}, 
                     {'macid': 'modih11', 'fname': 'harshil10', 'lname': 'modi', 'gender': 'male', 'gpa': 3.9, 'choice': ['civil', 'electrical', 'mechanical']}, 
                     {'macid': 'modih13', 'fname': 'harshil12', 'lname': 'modi', 'gender': 'male', 'gpa': 2.0, 'choice': ['software', 'engphys', 'software']}]
    

#Test case to check if the sort function can handle empty file    
def test_sort_1():
    S = ReadAllocationData.readStdnts("textfile1.txt")
    sort = CalcModule.sort(S)
    assert sort == []

#Test case to check if it can handle GPA of 0 while sorting       
def test_sort_2():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    sort = CalcModule.sort(S)
    assert sort == [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}, 
                     {'macid': 'modih3', 'fname': 'harshil2', 'lname': 'modi', 'gender': 'male', 'gpa': 0.0, 'choice': ['civil', 'electrical', 'chemical']}]

#Test case to check if it can sort all files with same GPA
def test_sort_3():
    S = ReadAllocationData.readStdnts("textfile4.txt")
    sort = CalcModule.sort(S)
    assert sort == [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 1.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                     {'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'male', 'gpa': 1.0, 'choice': ['electrical', 'software', 'mechanical']}, 
                     {'macid': 'modih3', 'fname': 'harshil2', 'lname': 'modi', 'gender': 'male', 'gpa': 1.0, 'choice': ['software', 'electrical', 'chemical']}]

#test case to check if average can handle large dataset for female
def test_average():
    S = ReadAllocationData.readStdnts("textfile.txt")
    average = CalcModule.average(S, "female")
    assert average == 7.19

#test case to check if average can handle large dataset for male    
def test_average1():
    S = ReadAllocationData.readStdnts("textfile.txt")
    average = CalcModule.average(S, "male")
    assert average == 7.47

#test case to check if average can handle no data for female     
def test_average3():
    S = ReadAllocationData.readStdnts("textfile1.txt")
    average = CalcModule.average(S, "female")
    assert average == 0.0
 
#test case to check if average can handle no data for male       
def test_average4():
    S = ReadAllocationData.readStdnts("textfile1.txt")
    average = CalcModule.average(S, "male")
    assert average == 0.0

#test case to check if average can handle same GPA for all
def test_average5():
    S = ReadAllocationData.readStdnts("textfile4.txt")
    average = CalcModule.average(S, "male")
    assert average == 1.0
    
#test case when free choice file contains names but file is empty
def test_allocate():
    S = ReadAllocationData.readStdnts("textfile1.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice.txt")
    C = ReadAllocationData.readDeptCapacity("department.txt")   
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [], 'mechanical': [], 'software': [], 'materials': [], 'engphys': []}
    assert department == department1

#test case to check when a person has a GPA of zero (<4.0)   
def test_allocate1():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice.txt")
    C = ReadAllocationData.readDeptCapacity("department.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [{'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 
                   'choice': ['electrical', 'software', 'mechanical']}], 'mechanical': [], 'software': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 
                             'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}], 'materials': [], 'engphys': []}
    assert department == department1

# test case to check if allocate can handle large data with a few free choice students and full first and second choices
def test_allocate2():
    S = ReadAllocationData.readStdnts("textfile.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice.txt")
    C = ReadAllocationData.readDeptCapacity("department.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [{'macid': 'modih15', 'fname': 'harshil14', 'lname': 'modi', 'gender': 'male', 'gpa': 8.0, 'choice': ['civil', 'electrical', 'chemical']}, 
                              {'macid': 'modih19', 'fname': 'harshil18', 'lname': 'modi', 'gender': 'female', 'gpa': 7.4, 'choice': ['civil', 'electrical', 'chemical']}, 
                              {'macid': 'modih3', 'fname': 'harshil2', 'lname': 'modi', 'gender': 'male', 'gpa': 7.0, 'choice': ['civil', 'electrical', 'chemical']}], 'chemical': [{'macid': 'modih16', 'fname': 'harshil15', 'lname': 'modi', 'gender': 'female', 'gpa': 9.0, 'choice': ['chemical', 'engphys', 'software']}, 
                              {'macid': 'modih9', 'fname': 'harshil8', 'lname': 'modi', 'gender': 'male', 'gpa': 9.2, 'choice': ['chemical', 'engphys', 'software']}, 
                              {'macid': 'modih4', 'fname': 'harshil3', 'lname': 'modi', 'gender': 'male', 'gpa': 5.0, 'choice': ['chemical', 'engphys', 'software']}, 
                              {'macid': 'modih24', 'fname': 'harshil23', 'lname': 'modi', 'gender': 'female', 'gpa': 5.0, 'choice': ['chemical', 'engphys', 'software']}], 'electrical': [{'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}, 
                              {'macid': 'modih22', 'fname': 'harshil21', 'lname': 'modi1', 'gender': 'female', 'gpa': 8.2, 'choice': ['electrical', 'software', 'mechanical']}, 
                              {'macid': 'modih5', 'fname': 'harshil4', 'lname': 'modi', 'gender': 'male', 'gpa': 8.5, 'choice': ['software', 'electrical', 'mechanical']}, 
                              {'macid': 'modih6', 'fname': 'harshil5', 'lname': 'modi1', 'gender': 'female', 'gpa': 7.5, 'choice': ['electrical', 'sofware', 'mechanical']}, 
                              {'macid': 'modih10', 'fname': 'harshil9', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.8, 'choice': ['electrical', 'software', 'mechanical']}, 
                              {'macid': 'modih7', 'fname': 'harshil6', 'lname': 'modi', 'gender': 'male', 'gpa': 5.3, 'choice': ['software', 'electrical', 'mechanical']}], 'mechanical': [], 'software': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                              {'macid': 'modih8', 'fname': 'harshil7', 'lname': 'modi', 'gender': 'male', 'gpa': 5.0, 'choice': ['software', 'electrical', 'mechanical']}, {'macid': 'modih12', 'fname': 'harshil11', 'lname': 'modi', 'gender': 'female', 'gpa': 7.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                              {'macid': 'modih21', 'fname': 'harshil20', 'lname': 'modi', 'gender': 'male', 'gpa': 9.3, 'choice': ['software', 'electrical', 'mechanical']}, {'macid': 'modih23', 'fname': 'harshil22', 'lname': 'modi', 'gender': 'male', 'gpa': 11.5, 'choice': ['software', 'electrical', 'chemical']}, 
                              {'macid': 'modih18', 'fname': 'harshil17', 'lname': 'modi1', 'gender': 'female', 'gpa': 11.0, 'choice': ['software', 'electrical', 'mechanical']}, {'macid': 'modih17', 'fname': 'harshil16', 'lname': 'modi', 'gender': 'male', 'gpa': 10.0, 'choice': ['software', 'electrical', 'mechanical']}], 'materials': [], 'engphys': [{'macid': 'modih20', 'fname': 'harshil19', 'lname': 'modi', 'gender': 'male', 'gpa': 7.9, 'choice': ['engphys', 'electrical', 'mechanical']}]}
    assert department == department1

#test case to check when a person has a GPA of zero (<4.0) but also free choice  
def test_allocate3():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice1.txt")
    C = ReadAllocationData.readDeptCapacity("department.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [{'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 
                   'choice': ['electrical', 'software', 'mechanical']}], 'mechanical': [], 'software': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 
                             'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}], 'materials': [], 'engphys': []}
    assert department == department1

#test case to check when the first choice is full for a person without free choice      
def test_allocate4():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice1.txt")
    C = ReadAllocationData.readDeptCapacity("department1.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                             {'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}], 'mechanical': [], 'software': [], 'materials': [], 'engphys': []}
    assert department == department1
    
#test case to check when the first choice is full and second choice is full for a person without free choice      
def test_allocate5():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice1.txt")
    C = ReadAllocationData.readDeptCapacity("department2.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [], 'mechanical': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                             {'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}], 'software': [], 'materials': [], 'engphys': []}
    assert department == department1

#test to see when all 3 of the choices are full for someone without free choice    
def test_allocate6():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice1.txt")
    C = ReadAllocationData.readDeptCapacity("department3.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [], 'mechanical': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}, 
                             {'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}], 'software': [], 'materials': [], 'engphys': []}
    assert department == department1

#test case to check when the first choice is full for a person with freechoice
def test_allocate7():
    S = ReadAllocationData.readStdnts("textfile2.txt")
    F = ReadAllocationData.readFreeChoice("freeChoice2.txt")
    C = ReadAllocationData.readDeptCapacity("department3.txt")
    department = CalcModule.allocate(S, F, C)
    department1 = {'civil': [], 'chemical': [], 'electrical': [{'macid': 'modih2', 'fname': 'harshil1', 'lname': 'modi1', 'gender': 'female', 'gpa': 6.0, 'choice': ['electrical', 'software', 'mechanical']}],
                   'mechanical': [{'macid': 'modih1', 'fname': 'harshil', 'lname': 'modi', 'gender': 'male', 'gpa': 12.0, 'choice': ['software', 'electrical', 'mechanical']}], 'software': [], 'materials': [], 'engphys': []}
    assert department == department1