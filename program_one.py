'''
Interface of the exam
'''
import setup
import os
import exam  
import sys

def parse_cmd_args(args):
    '''
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam

    >>> parse_cmd_args(['program.py', '/home/info1110/', '60', '-r'])
    ('/home/info1110/', 60, True)

    >>> parse_cmd_args(['program.py', '/home/info1110/', 'ab', '-r'])
    Duration must be an integer

    >>> parse_cmd_args(['program.py', '/home/info1110/'])
    Check command line arguments
    '''
    if len(args) < 3:
        print("Check command line arguments")
        return None
    elif not args[2].isdigit():
        print("Duration must be an integer")
        return None
    else:
        shuffle = False
        if len(args) > 3 and args[3] == "-r": 
            shuffle = True
        return (args[1], int(args[2]), shuffle)
            

def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file 
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
      '''
    path = obj.path_to_dir + "/questions.txt"
    fobj = open(path, "r")
    ques = setup.extract_questions(fobj)
    status = obj.set_questions(ques)
    if status:
        obj.set_exam_status()
    return (obj, status)


def main(args):
    '''
    Implement all stages of exam process.
    '''
    path = args[1]
    students_path = path + "/students.csv"
    question_path = path + "/questions.txt"
    if os.path.exists(students_path) and os.path.exists(question_path):
        try:
            path, duration, shuffle = parse_cmd_args(args)
            exam_obj = exam.Exam(duration, path, shuffle) 
        except:
            return None
        print("Setting up exam...")
    else:
        print("Missing files")
        return

    
    exam_obj.status = setup_exam(exam_obj)[1] 
    
    if exam_obj.status:
        print("Exam is ready...")
        while True:
            action = input("Do you want to preview the exam [Y|N]? ")
            if action.lower() == "y":
                print(exam_obj.preview_exam(), end = "")
            elif action.lower() == "n":
                break
            else:
                print("Invalid command.")
        return exam_obj
    else:
        print("Error setting up exam")
        return None

    

if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)


