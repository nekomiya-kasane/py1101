class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)
        
    def copy_exam(self):
        """
        Returns a deep copy of the current Exam object.
        """
        
        copied_exam = Exam(self.duration, self.path_to_dir, self.shuffle)
        copied_exam.exam_status = self.exam_status
        copied_exam.questions = [q.copy_question() for q in self.questions]  # Assuming each question has a copy_question() method
        return copied_exam

    def set_name(self, path):
        """
        Sets the name of the exam. 
        """
        new_str = ""
        contents = path.split("/")
        name = contents[-1]
        i = 0
        while i < len(name):
            if name[i] == " ":
                new_str += "_"
            else:
                new_str += name[i]
            i += 1
        self.name = new_str

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        return self.name.replace("_", " ").upper()

    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if self.questions != []:
            self.exam_status = True
        
    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if isinstance(t, int) and t > 0:  
            self.duration = t        

    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''

        if type(ls) != list:
            return False

    
        end_q = ls[-1]
        if (end_q.qtype != "end" or end_q.description != None or end_q.answer_options != [] or end_q.correct_answer != None or end_q.marks != None):
            print("End marker missing or invalid")
            return False

    
        is_complete = True
        i = 0
        while i < len(ls) - 1: 
            ques = ls[i]
            if not self.check_complete(ques):
                is_complete = False
                break
            i += 1
        if is_complete:
            self.questions = ls

        return is_complete     



    def check_complete(self, question):
        if not question.description or not question.correct_answer:
            print("Description or correct answer missing")
            return False

        if question.qtype == "single" or question.qtype == "multiple":
            if not question.answer_options or len(question.answer_options) != 4:
                print("Answer options incorrect quantity")
                return False

        elif question.qtype == "short" and question.answer_options:
            print("Answer options should not exist")
            return False
        return True
    
    def preview_exam(self):
        '''
        Returns a formatted string.
        '''
        result = ""
        i = 0
        while i < len(self.questions):
            if i == 0:
                result += self.get_name()+"\n"
            if i > 0:
                result += "\n"
            
            result += self.questions[i].preview_question(i+1)
            result += "\n"
            if i == len(self.questions)-1:
                result += "\n"
            i += 1
        return result


        
    def __str__(self):
        Pass

