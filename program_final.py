'''
Interface of the exam
'''

import setup
import program_two

def main(argv):
    candidates = program_two.main(argv)
    sid_attempts = 0
    name_attempts = 0

    while sid_attempts < 3:
        sid = input("Enter your student identification number (SID) to start exam: ")
        
        if not sid.isdigit() or len(sid) != 9:
            print("Invalid SID.")
            sid_attempts += 1
            if sid_attempts == 3:
                print("Contact exam administrator.")
                return

        else:
            cand = find_one(candidates, sid)
            if cand is None:
                print("Candidate number not found for exam.")
                sid_attempts += 1

                while True:
                    action = input("Do you want to try again [Y|N]?")
                    if action.lower() == "y":
                        break
                    elif action.lower() == "n":
                        return
                    else:
                        print("Response must be [Y|N].")
            else:
                print("Verify candidate details...")
                while name_attempts < 3:
                    name = input("Enter your full name as given during registration of exam: ")
                    if name.lower() != cand.name.lower():
                        print("Name does not match records.")
                        name_attempts += 1
                        if name_attempts == 3:
                            return
                    else:
                        print("Start exam...")
                        cand.do_exam(False) 
                        return



