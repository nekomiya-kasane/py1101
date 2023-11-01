class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        if self.exam:
            return self.exam.duration + self.extra_time
        return 0
            
    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        if isinstance(sid, str) and len(sid) == 9 and int(sid) > 0:
            self.sid = sid
        

    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        if type(t) == int and t >= 0:
            self.extra_time = t

    
    def set_confirm_details(self, sid, name):
        '''
        Update attribute confim_details
        '''
        if sid == self.sid and name.lower() == self.name.lower():
            self.confirm_details = True
            return True
        return False

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        file = "{}.txt".format(self.sid)
        fobj = open(file, "w")
        fobj.write(data)
        fobj.close()
    
    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details:
            if len(ls) == len(self.exam.questions) - 1:  
                self.results = ls

    def do_exam(self, preview=True):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''
        
        print(f"Candidate: {self.name}({self.sid})")
        t = self.get_duration()
        print(f"Exam duration: {t} minutes")
        print(f"You have {t} minutes to complete the exam.")

        if self.exam is None:
            print("No exam assigned.")
            return

        for i, question in enumerate(self.exam.questions, start=1):
            question_type = question.qtype  
            marks = question.marks  
            description = question.description  
            answer_options = question.answer_options  

            
            print(f"Question {i} - {question_type.capitalize()} Answer[{marks}]")
            print(description)
            if answer_options: 
                print(f"[Optional] {answer_options}")

            if not preview:
                response = input(f"Response for Question {i}: ")
                
        print("-End-")




    def __str__(self):
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t}minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out






