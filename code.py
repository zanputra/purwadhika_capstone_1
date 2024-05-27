# Fauzan Harlyanto Putra
# JCDSOL-14B

#Capstone Module 1
#-------------------------------------------------------------------------------------- INITIAL DATA AREA ------------------------------------------------------------------------------------------------

all_StudentData = [ 
    {
        'ID': 'AA001', 
        'NAME': 'Aaliyah Mossad', 
        'GENDER': 'Female',
        'CLASS':'Alpha', 
        'STATISTICS': 100, 
        'OOP': 99,
        'BIOLOGY': 98,
        'EMAIL':'a.mossad@aamail.ac.id'
    },
    {   
        'ID': 'AA002', 
        'NAME': 'Bukhari Bennett', 
        'GENDER': 'Male',
        'CLASS': 'Sigma', 
        'STATISTICS': 95, 
        'OOP': 85,
        'BIOLOGY': 75,
        'EMAIL': 'b.bennet@aamail.ac.id'
    },
    {
        'ID': 'AA003', 
        'NAME': 'Maria Stojanova', 
        'GENDER': 'Female',
        'CLASS': 'Alpha', 
        'STATISTICS': 90, 
        'OOP': 88,
        'BIOLOGY': 86,
        'EMAIL': 'm.stojanova@aamail.ac.id'
        
    },
    {   
        'ID': 'AA004', 
        'NAME': 'Mohammed Avdol', 
        'GENDER': 'Male',
        'CLASS' : 'Sigma',
        'STATISTICS': 85, 
        'OOP': 85,
        'BIOLOGY': 85,
        'EMAIL':'m.avdol@aamail.ad.id'
    },
]
#-------------------------------------------------------------------------------------- END INITIAL DATA AREA ------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------- ESSENTIALS FUNCTION AREA ------------------------------------------------------------------------------------------------


# Region Get Student ID
StudentID = ''
def get_id():
    while True:
        global StudentID
        temp_StudentID = input('\nEnter Student ID : ')
        if temp_StudentID[:2] == 'AA' and temp_StudentID[2:].isnumeric():
            StudentID = temp_StudentID
            break
        else:
            e_false_input
    return StudentID
# End Region Get Student ID

#Region printing student data
column_names = [nilai for nilai in all_StudentData[0].keys()]

def calculate_columnWidths(data, column_names):
    column_widths = []
    for column_name in column_names:
        max_length = max(len(str(row[column_name])) for row in data)
        column_widths.append(max_length)
    return column_widths

def get_studentScore(data,column_names):
    result = calculate_columnWidths(data, column_names)

    init_max_result = []
    for column_name, width in zip(column_names, result):
        max_result = max(len(column_name), width)
        init_max_result.append(max_result)


    print('+'+'+'.join(['-' * (width + 2) for width in init_max_result]) + '+')
    print('|' + '|'.join([' ' + column_name.center(width) + " " for column_name, width in zip(column_names, init_max_result)]) + "|")
    print('+'+'+'.join(['-' * (width + 2) for width in init_max_result]) + '+')

    for iterExam in data:
        row = [str(iterExam[vals]) for vals in column_names]
        print("|" + "|".join([" " + value.ljust(width) + " " for value, width in zip(row, init_max_result)]) + "|")
    print("+" + "+".join(["-" * (width + 2) for width in init_max_result]) + "+")

#End Region

#Region Alter Student Data
def alter_studentData(param_id, param_choice, altrdData):
    single_StudentData = [iterExamList for iterExamList in all_StudentData if iterExamList['ID']==param_id]
    single_StudentData[0][param_choice] = altrdData

#End Region

#Region New Student Mail
def get_studentMail(param_name):
    mail = param_name.lower()
    if len(param_name.split()) == 1:
        mail = mail + '@aamail.ac.id'     
    elif len(param_name.split()) == 2:
        mail2 = "".join(mail.split()[1])
        mail = mail[0] + '.' + mail2 + '@aamail.ac.id'
    elif len(param_name.split()) > 2:
        mail2 = "".join(mail.split()[1:-1])
        mail = mail[0] + '.' + mail2 + '@aamail.ac.id'
    return mail
#End Region       

#Region Delete Student Data
def del_studentData(param_id, data):
    
    data_toDel = [i for i, iterExamList in enumerate(all_StudentData)if iterExamList['ID']==param_id]
    int_result = int(''.join(map(str, data_toDel)))
    del data[int_result]

#-------------------------------------------------------------------------------------- END ESSENTIAL FUNCTION AREA ------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------- MISC PRINT AREA ------------------------------------------------------------------------------------------------

#Region Press Any Key
def i_pressAnyKey():
    input('\nPress Any Key to Continue...')
#end Region

#Region Zero Data
def e_zero_data():
    print('\nERROR: No data is found!')
#End Region

#Region False Input
def e_false_input():
    print('\nERROR: Input is not recognised!')
#end Region

#Region Student ID Already Exists
def e_student_exists(param_StudentID):
    print('\nERROR: Student ID is already exists!')
#end Region

#Region Saved Data
def info_saved():
    print('\nData Successfully Saved')
#end Region

#Region Deleted Data
def info_deleted():
    print('\nData Successfully Deleted')
#end Region

#Region Updated Data
def info_updated():
    print('\nData Successfully Updated')
#end Region
#-------------------------------------------------------------------------------------- END MISC PRINT AREA ------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------- GUI AREA ------------------------------------------------------------------------------------------------

#Region main menu function
def main_menu():
    while True:
        print('''
Welcome to Alpha Arbutin School Exam Result Data Vault

1. Display Exam Results of The Students 
2. Insert Exam Results of The Students 
3. Alter Exam Results of The Students 
4. Delete Exam Results of The Students 
5. Quit Program
        ''')

        mainChoice = input('Choose [1 - 5] : ')
        
        if mainChoice == '1':
            read_data()
        elif mainChoice == '2':
            insert_data()
        elif mainChoice == '3':
            alter_data()
        elif mainChoice == '4':
            pop_data()
        elif mainChoice  == '5':
            quit()
        else:
            e_false_input()
            i_pressAnyKey()

#End Region main menu function

# Region Read Function

def read_data():
    isReading = 1
    while isReading == 1:
        
        print('''
Display Exam Score of Students in AlphaArbutin High

1. Display Exam Score of All Students
2. Display Exam Score of Certain Students
3. Back
        ''')
        
        subChoice = input('\nChoose [1 - 3] : ')
        
        #Region Read All Data (checked aman)
        if subChoice == '1':
            #Check Null Data
            if len(all_StudentData) == 0:
                e_zero_data()
                i_pressAnyKey()
            else:
                print('\nExam Score of All Students:')
                get_studentScore(all_StudentData, column_names)
                i_pressAnyKey()
                # isReading = 0
                # main_menu()
        #End Region
        
        #Region Read Segmented Data (checked aman)
        elif subChoice == '2':
            if len(all_StudentData) == 0:
                e_zero_data()
                i_pressAnyKey()
            else:
                isSubChoice2 = 1
                while isSubChoice2 == 1:
                    print('''
Display Exam Score of Students in AlphaArbutin High

1. Display Based on Student ID
2. Display Based on Gender
3. Display Based on Class
4. Back
            ''')    
                    super_SubChoice = input('\nChoose [1 - 4] : ')
                    if super_SubChoice == '1':
                        lookUp = 'id'
                        loop_Sub = 1
                        while loop_Sub == 1:
                            print('\nExam Score of Student Based on Student ID:')
                            
                            get_id()
                            
                            if StudentID not in [iterExamList['ID'] for iterExamList in all_StudentData]:
                                e_zero_data()
                                i_pressAnyKey()
                            elif StudentID in [iterExamList['ID'] for iterExamList in all_StudentData]:
                                    print(f"\nHere are data of Student with Student ID : {StudentID}")
                                    single_StudentData = [iterExamList for iterExamList in all_StudentData if iterExamList[lookUp.upper()]==StudentID]
                                    get_studentScore(single_StudentData, column_names)
                                    i_pressAnyKey()
                                    loop_Sub = 0
                                    isSubChoice2 = 0
                                    # isReading = 0
                                    # main_menu()
                    
                    elif super_SubChoice == '2':
                        lookUp = 'gender'
                        isLookingUp_val = 1
                        while isLookingUp_val == 1:
                            lookUp_value = input('Which Gender? [Male / Female] : ').upper()
                            if lookUp_value != 'MALE' and lookUp_value != 'FEMALE':
                                e_false_input()
                                i_pressAnyKey()
                            else:
                                print(f"\nHere are data of Student(s) of {lookUp.capitalize()} : {lookUp_value}")
                                single_StudentData = [iterExamList for iterExamList in all_StudentData if iterExamList[lookUp.upper()]==lookUp_value.capitalize()]
                                get_studentScore(single_StudentData, column_names)
                                i_pressAnyKey()
                                isLookingUp_val = 0
                                isSubChoice2 = 0
                                # isReading = 0
                                # main_menu()
                                
                    elif super_SubChoice == '3':
                        lookUp = 'class'
                        isLookingUp_val = 1
                        while isLookingUp_val == 1:
                            lookUp_value = input('Which Class? [Alpha / Sigma] : ').upper()
                            if lookUp_value != 'ALPHA' and lookUp_value != 'SIGMA':
                                e_false_input()
                                i_pressAnyKey()
                            else:
                                print(f"\nHere are data of Student(s) of {lookUp.capitalize()} : {lookUp_value}")
                                single_StudentData = [iterExamList for iterExamList in all_StudentData if iterExamList[lookUp.upper()]==lookUp_value.capitalize()]
                                get_studentScore(single_StudentData, column_names)
                                i_pressAnyKey()
                                isLookingUp_val = 0
                                isSubChoice2 = 0
                                # isReading = 0
                                # main_menu()
                    elif super_SubChoice == '4':
                        isSubChoice2 = 0
                        i_pressAnyKey()
                    else:
                        e_false_input()
                        i_pressAnyKey()
        #End Region
        
        #Back To Menu
        elif subChoice == '3':
            isReading = 0
            main_menu()
        
        #Escape choice if input is invalid
        else:
            e_false_input()

#End Region Read Function
    
#Region Insert New Data
def insert_data():
    isInserting = 1
    while isInserting == 1:   
        print('''
Insert New Exam Score of Students in AlphaArbutin High

1. Insert New Exam Score of Students in Alpha Arbutin High
2. Back
        ''')
    
        subChoice = input('\nChoose [1 - 2] : ')

        #Region Insert new data
        if subChoice == '1':
            #Get Student ID
            get_id()

            #validate studentID
            if StudentID in [iterExamList['ID'] for iterExamList in all_StudentData]:
                e_student_exists(StudentID)
                i_pressAnyKey()
                
            #if student id fulfills validaton, then proceed to insert new data       
            else:
                newID = StudentID
                #Get and validate Student Name
                isGettingName = 1
                while isGettingName == 1:
                    newName = input('Input New Student\'s Name: ')
                    if len(newName) == 0 or newName.isnumeric():
                        e_false_input()
                        # i_pressAnyKey()
                    else:
                        newName = newName.title()
                        isGettingName = 0

                #Get Student Gender
                isGettingGender = 1
                while isGettingGender == 1:
                    newGender = input('Input New Student\'s Gender [Male / Female] : ').upper()
                    if newGender != 'MALE' and newGender != 'FEMALE':
                        e_false_input()
                    else:
                        newGender = newGender.capitalize()
                        isGettingGender = 0
                
                #Get Student Class
                isGettingClass = 1
                while isGettingClass == 1:
                    newClass = input('Input New Student\'s Class [Alpha / Sigma] : ').upper()
                    if newClass != 'ALPHA' and newClass != 'SIGMA':
                        e_false_input()
                    else:
                        newClass = newClass.capitalize()
                        isGettingClass = 0
                
                #Get Student Email
                newMail = get_studentMail(newName)
                print('E-mail is autogenerated!')
                  
                #Region append new nilai pour chaque metier
                temp_NewExam = {"STATISTICS": 0, "OOP": 0, "BIOLOGY": 0}
                for metier in temp_NewExam:
                    isGettingMetier = 1
                    while isGettingMetier == 1:
                        temp_NewExam[metier] = input(f'Insert Score of {metier} (0-100): ')
                        if (temp_NewExam[metier].isdigit() == False) or (int(temp_NewExam[metier]) > 100 or int(temp_NewExam[metier]) < 0):
                            e_false_input
                        else:
                            temp_NewExam[metier] = int(temp_NewExam[metier])
                            isGettingMetier = 0
                
                #Region Saving Inserted Data
                isSaving = 1
                while isSaving == 1:
                    save = input('\nAre You Sure to Save the Data? [Yes / No]: ').upper()

                    if save == 'YES':
                        all_StudentData.append(
                        {
                            'ID': newID, 
                            'NAME': newName, 
                            'GENDER': newGender,
                            'CLASS':newClass, 
                            'STATISTICS': temp_NewExam["STATISTICS"], 
                            'OOP': temp_NewExam["OOP"],
                            'BIOLOGY': temp_NewExam["BIOLOGY"],
                            'EMAIL' : newMail
                        }
                        )
                        info_saved()
                        i_pressAnyKey()
                        isSaving = 0
                        # isInserting = 0
                        # main_menu()
                    elif save == 'NO':
                        isSaving = 0
                    else:
                        e_false_input()
        
        #End Region Insert New Data
        
        #Back to Menu
        elif subChoice == '2':
            isInserting = 0
            main_menu()
        #Escape choice if input is invalid
        else:
            e_false_input()

# End Region Insert Data

#Region Alter Data

def alter_data():
    isAltering = 1
    while isAltering == 1:
        print('''
Alter Alpha Arbutin High Student's Exam Score Data

1. Alter Data
2. Back
        ''')
        
        subChoice = input('Choose [1 - 2] : ')
        
        if subChoice == '1':
            print('\nExam Score of Single Student:')
            get_id()
                
            if len(all_StudentData) == 0 or StudentID not in [iterExamList['ID'] for iterExamList in all_StudentData]:
                e_zero_data()
                i_pressAnyKey()
            
            elif StudentID in [iterExamList['ID'] for iterExamList in all_StudentData]:
                    print(f"\nHere are data of Student with Student ID : {StudentID}")
                    single_StudentData = [iterExamList for iterExamList in all_StudentData if iterExamList["ID"]==StudentID]
                    get_studentScore(single_StudentData, column_names)
                    
                    alterFlag = 'DOWN'
                    isChoosing = 1
                    #Loop Start: Choose Data to Alter (Data vs Score)
                    while isChoosing == 1:
                        choice_ToAlter = input('\n\n Which Data to Alter [Student Data / Student Score]: ').upper()
                        
                        #Region Alter STUDENT DATA
                        if choice_ToAlter == 'STUDENT DATA':
                            is_alteringStudData = 1
                            while is_alteringStudData == 1:
                                print('''
Which student data do you wish to be alter

1. Student ID
2. Student Name
3. Student Gender
4. Student Class
5. Back
''')
                                choice_ToAlterData = input('Choose Which Data Do You Wish to be Altered [1 - 5] : ')
                                
                                if choice_ToAlterData == '1':
                                    isIDing = 1
                                    while isIDing == 1:
                                        get_id()
                                        if StudentID in [iterExamList['ID'] for iterExamList in all_StudentData]:
                                            e_student_exists(StudentID)
                                            i_pressAnyKey()
                                        else:
                                            altrdData = StudentID
                                            isIDing = 0
                                            is_alteringStudData = 0
                                            isChoosing = 0
                            
                                #if input equals to name
                                elif choice_ToAlterData == '2':
                                    print('CAUTION: NOTICE THAT CHANGING NAME ALSO CHANGES EMAIL')
                                    isNaming = 1
                                    while isNaming == 1:
                                        altrdData = input('Input New Student\'s Name : ')
                                        if len(altrdData) == 0 or altrdData.isnumeric():
                                            e_false_input()
                                            i_pressAnyKey()
                                        else:
                                            altrdData = altrdData.title()
                                            altrdMail = get_studentMail(altrdData)
                                            choice = 'NAME'
                                            alterFlag = 'UP'
                                            isNaming = 0
                                            is_alteringStudData = 0
                                            isChoosing = 0
                                
                                #if input equals to gender
                                elif choice_ToAlterData == '3':
                                    isGendering = 1
                                    while isGendering == 1:
                                        altrdData = input('Input New Student\'s Gender [Male / Female] : ').upper()
    
                                        if altrdData != 'MALE' and altrdData != 'FEMALE':
                                            e_false_input()
                                            i_pressAnyKey()
                                        else:
                                            altrdData = altrdData.title()
                                            choice = 'GENDER'
                                            alterFlag = 'UP'
                                            isGendering = 0
                                            is_alteringStudData = 0
                                            isChoosing = 0
                                
                                #if input equals to class
                                elif choice_ToAlterData == '4':
                                    isClassing = 1
                                    while isClassing == 1:
                                        altrdData = input('Input New Student\'s Class [Alpha / Sigma] : ').upper()
    
                                        if altrdData != 'ALPHA' and altrdData != 'SIGMA':
                                            e_false_input()
                                            i_pressAnyKey()
                                        else:
                                            altrdData = altrdData.title()
                                            choice = 'CLASS'
                                            alterFlag = 'UP'
                                            isClassing = 0
                                            is_alteringStudData = 0
                                            isChoosing = 0
                                
                                elif choice_ToAlter == '5':
                                    is_alteringStudData = 0
                                    isChoosing = 0
                        #End Region Alter Student Data
                        
                        # Region Alter Student Score    
                        elif choice_ToAlter == 'STUDENT SCORE':
                            is_alteringStudScore = 1
                            while is_alteringStudScore == 1:
                                print('''
Which student data do you wish to be alter

1. Statistics Score
2. OOP Score
3. Biology Score
4. Back
''')
                                choice_ToAlterScore = input('Which Subject Score Do You Wish to Alter? [1 - 4] : ')
                                flag = 'RED'
                                metier = ''
                                if choice_ToAlterScore == '1':
                                    metier = 'STATISTICS'
                                    flag = 'GREEN'
                                elif choice_ToAlterScore == '2':
                                    metier = 'OOP'
                                    flag = 'GREEN'
                                elif choice_ToAlterScore == '3':
                                    metier = 'BIOLOGY'
                                    flag = 'GREEN'
                                elif choice_ToAlterScore == '4':
                                    is_alteringStudScore = 0
                                    isChoosing = 0
                                    flag = 'RED'
                                else:
                                    e_false_input()
                                
                                if flag == 'GREEN':
                                    isMetiering = 1
                                    while isMetiering == 1:
                                        altrdData = input(f'Insert New {metier} Score [0 - 100]: ')
                                        
                                        if (altrdData.isdigit() == False) or (int(altrdData) > 100 or int(altrdData) < 0):
                                            e_false_input()
                                            i_pressAnyKey()
                                        else:
                                            altrdData = int(altrdData)
                                            choice = metier
                                            alterFlag = 'UP'
                                            isMetiering = 0
                                            is_alteringStudScore = 0
                                            isChoosing = 0
                            #End Region Alter Student Score
                    
                    
                        if alterFlag == 'UP':
                            isUpdating = 1
                            while isUpdating == 1:
                                update = input('\nDo You Wish to Alter This Data? [YES / NO]: ').upper()
                                if update == 'YES':
                                    if choice == 'NAME':
                                        alter_studentData(StudentID, choice, altrdData)
                                        alter_studentData(StudentID, 'EMAIL', altrdMail)
                                    else:
                                        alter_studentData(StudentID, choice, altrdData)
                                    info_saved()
                                    i_pressAnyKey()
                                    isUpdating = 0
                                    isChoosing = 0
                                    # isAltering = 0
                                elif update == 'NO':
                                    i_pressAnyKey()
                                    isUpdating = 0
                                    isChoosing = 0
                                else:
                                    e_false_input()
                                    i_pressAnyKey()
                    #Boundary loop data vs score (isChoosing)
                        
        #Back to menu            
        elif subChoice == '2':
            isAltering = 0
            main_menu()
        #Escape condition if input is invalid
        else:
            e_false_input()

# Region Pop Data

def pop_data():
    isPopping = 1
    while isPopping == 1:
        print('''
Delete Student's Exam Data

1. Delete Student Data
2. Back
''')
        
        subChoice = input('Choose [1 - 2]: ')
        
        if subChoice == '1':
            get_id()
            if StudentID not in [iterExamList['ID'] for iterExamList in all_StudentData]:
                e_zero_data()
                i_pressAnyKey()
            elif StudentID in [iterExamList['ID'] for iterExamList in all_StudentData]:
                    print(f"\nHere are Data of Student with Student ID : {StudentID}")
                    single_StudentData = [iterExamList for iterExamList in all_StudentData if iterExamList['ID']==StudentID]
                    get_studentScore(single_StudentData, column_names)
                    
                    isSubChoice1 = 1
                    while isSubChoice1 == 1:
                        subChoice_opt = input('Do You Wish to Delete This Data? [YES / NO] : ').upper()
                        
                        if subChoice_opt == 'YES':
                            del_studentData(StudentID, all_StudentData)
                            info_deleted()
                            i_pressAnyKey()
                            isSubChoice1 = 0
                            isPopping = 0
                        elif subChoice_opt == 'NO':
                            isSubChoice1 = 0
                            isPopping = 0
                        else:
                            e_false_input()
                            i_pressAnyKey()
                    
        elif subChoice == '2':
            isPopping = 0
            main_menu()
        else:
            e_false_input
#End Region

#-------------------------------------------------------------------------------------- END GUI AREA ------------------------------------------------------------------------------------------------
    
#Start The Program
main_menu()
