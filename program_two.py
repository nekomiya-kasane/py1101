'''
Interface of the exam
'''

import setup
import program_one
import sys
import exam

def assign_exam(exam):
    path = exam.path_to_dir + "/students.csv"
    fobj = open(path, "r")
    candidates = setup.extract_students(fobj)
    if candidates == []:
        print("No candidates found in the file")
        return None
    print("Assigning exam to candidates...")

    index = 0
    num_candidates = len(candidates)
    while index < num_candidates:
        candidate = candidates[index]
        if exam.shuffle:
            candidate.exam = exam.copy_exam()
        else:
            candidate.exam = exam
        index += 1

    print("Complete. Exam allocated to {} candidates.".format(len(candidates)))
    return candidates 


def copy_question(self):
    new_question = Question(self.qtype)
    if self.qtype == "end":
        return new_question

    new_question.description = self.description
    new_question.set_answer_options(self.answer_options)
    new_question.set_correct_answer(self.correct_answer)
    new_question.marks = self.marks
    new_question.shuffle_answers()
    return new_question

def main(argv):
    exam_obj = program_one.main(argv)
    candidates = assign_exam(exam_obj)
    
    while True:
        action = input("Enter SID to preview student's exam (-q to quit): ")

       
        if action == "-q":
            break
        
        
        elif action == "-a":
            for candidate in candidates:
                print(candidate.do_exam())

        
        elif action.isdigit() and len(action) == 9:
            matched_candidate = None
            for candidate in candidates:
                if candidate.sid == action:
                    matched_candidate = candidate
                    break

            if matched_candidate:
                print(matched_candidate.do_exam())
            else:
                print("SID not found in list of candidates.")
        
        else:
            print("SID is invalid.")


if __name__ == "__main__":
    main(sys.argv)


