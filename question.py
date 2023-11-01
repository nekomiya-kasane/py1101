import random

class Question:
    def __init__(self, qtype):
        if self.set_type(qtype) == False:
            self.qtype = None
        else:
            self.qtype = None
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None
        
        self.set_type(qtype)
    def copy_question(self):
        new_question = Question(self.qtype, self.description, self.answer_options, self.correct_answer, self.marks)
        return new_question

    def set_type(self, qtype):
        if qtype == "single" or qtype == "multiple" or qtype == "short" or qtype == "end":
            self.qtype = qtype
            return True
        return False
    

    def set_description(self, desc):
        if type(desc) == str and desc != "":
            self.description = desc
            return True
        return False
    
    def set_correct_answer(self, ans):
        if self.qtype == "end":
            return False

        if type(ans) != str:
            return False
        else:
            if self.qtype == "single":
                if ans == "A" or ans == "B" or ans == "C" or ans == "D":
                    self.correct_answer = ans
                    return True
                else:
                    return False
        
            if self.qtype == "short":
                self.correct_answer = ans
                return True
        
            if self.qtype == "multiple":
                if ans == "A" or ans == "B" or ans == "C" or ans == "D":
                    self.correct_answer = ans
                    return True
                else:
                    my_list = ans.split(", ")
                    i = 0
                    while i < len(my_list):
                        if my_list[i] != "A" and my_list[i] != "B" and my_list[i] != "C" and my_list[i] != "D":
                            return False
                        i += 1
                    self.correct_answer = ans 
                    return True
            return False

    
    def set_marks(self, num):
        if type(num) == int  and num >= 0 :
            self.marks = num
            return True
        return False

    
    def set_answer_options(self, opts):
        if self.qtype == "short":
            self.answer_options = opts
            return True
            
        i = 0
        while i < len(opts):
            each_tuple = opts[i]
            ans_des = each_tuple[0]
            ft = ans_des[:2]
            if ft != "A." and ft != "B." and ft != "C." and ft != "D.":
                return False
            i += 1
        
        if len(opts) != 4:
            return False
        
        fopt = opts[0][0][0]
        sopt = opts[1][0][0]
        topt = opts[2][0][0]
        fropt = opts[3][0][0]

        if not (fopt == "A" and sopt == "B" and topt == "C" and fropt == "D"):
            return False
        
        if not isinstance(self.correct_answer, str):
            return False

        if self.correct_answer != None:
            new = []
            if self.qtype == "single":
                if len(self.correct_answer) != 1:
                    return False
            if self.qtype == "multiple":
                if len(self.correct_answer.split(", ")) < 1:
                    return False
            i = 0
            while i < len(opts):
                if self.qtype == "single": 
                    new.append((opts[i][0], opts[i][0][0] == self.correct_answer))
                if self.qtype == "multiple":
                    flag = self.correct_answer.split(", ")
                    new.append((opts[i][0], opts[i][0][0] in flag))
                i += 1
            self.answer_options = new
            return True
        return False


    def get_answer_option_descriptions(self):
        if self.qtype == "end" or self.qtype == "short":
            return ""
        
        result = ""
        i = 0
        while i < len(self.answer_options):
            if i == len(self.answer_options)-1:
                result += "{}".format(self.answer_options[i][0])
            else:
                result += "{}\n".format(self.answer_options[i][0])
            i += 1
            
        return result
    
    def mark_response(self, response):
        if self.qtype == "end":
            return None
        total  = 0
        if self.qtype == "multiple":
            correct_ans = self.correct_answer.split(", ")
            mark = self.marks/ len(correct_ans)
            result = response.split(", ")
            index = 0
            while index < len(result):
                if result[index] in correct_ans:
                    total += mark
                index += 1
            return round(total,2)
        elif self.qtype == "short" or self.qtype == "single":
            if response == self.correct_answer:
                return self.marks
            else:
                return 0
        else:
            return None

        


    
    def shuffle_answers(self):
        if self.qtype not in ["single", "multiple"]:
            return

   
        order = Question.generate_order()

    
        old_opt = self.answer_options
        letters = ["A", "B", "C", "D"]
        new_opt = [(letters[i] + old_opt[order[i]][0][1:], old_opt[order[i]][1]) for i in range(4)]
        self.answer_options = new_opt


        if self.qtype == "single":
            old_index = letters.index(self.correct_answer)
            self.correct_answer = letters[order.index(old_index)]
        else:  
            correct_answers = self.correct_answer.split(", ")
            new_correct_answers = [letters[order[letters.index(ans)]] for ans in correct_answers]
            self.correct_answer = ", ".join(new_correct_answers)


    def preview_question(self, i = 0, show = True):
        if self.qtype == "end":
            return "-End-"
        if i == 0:
            i = "X"
        if self.qtype == "multiple":
            ans = "Answers"
        else:
            ans = "Answer"
        result = f"Question {i} - {self.qtype.capitalize()} {ans}[{self.marks}]\n"
        result += f"{self.description}\n"
        result += self.get_answer_option_descriptions()

        if show:
            if self.qtype == "short":
                result += f"Expected Answer: {self.correct_answer}"
            else:
                result += f"\nExpected Answer: {self.correct_answer}"
    
        return result
    
    def generate_order():
        result = []
        while len(result) != 4:
            num = random.randint(0,3)
            if num not in result:
                result.append(num)
        return result

    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''

