'''
Functions to setup the exam questions and candidate list for the exam.
'''
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step).
    2. You'll need to convert the possible answers (if any) to a list of tuples (see 
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    result = []
    content = fobj.read()
    content = content.strip().split("\n\n")
    i = 0
    while i < len(content):
        q = content[i]
        chunks = q.split("\n")
        t = chunks[0].split(" ")[-1].lower()
        exp_ans = chunks[-2].split(": ")[-1]
        marks = chunks[-1].split(": ")[-1]
        des = None
        ans_opt = []
        
        
        if t == "short":
            des = "\n".join(chunks[1:-2])
        else:
            idx = 1
            while idx < len(chunks) and "Possible Answer" not in chunks[idx]:
                idx += 1
            
            des = "\n".join(chunks[1:idx])
            
            
            idx += 1
            while idx < len(chunks) - 2:
                ans_opt.append((chunks[idx], False))
                idx += 1

        ques = question.Question(t)
        ques.set_marks(int(marks))
        ques.set_description(des)
        ques.set_correct_answer(exp_ans)
        if t == "single" or t == "multiple":
            ques.set_answer_options(ans_opt)
        result.append(ques)
        i += 1
    result.append(question.Question("end"))
    return result






def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.

    Sample usage:
    >>> to_sort = [(1.50, "orange"), (1.02, "apples"), (10.40, "strawberries")]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: [(1.5, 'orange'), (1.02, 'apples'), (10.4, 'strawberries')]
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: [(1.02, 'apples'), (1.5, 'orange'), (10.4, 'strawberries')]
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: [(10.4, 'strawberries'), (1.5, 'orange'), (1.02, 'apples')]
    >>> to_sort = [ "oranges", "apples", "strawberries"]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: ['oranges', 'apples', 'strawberries']
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: ['apples', 'oranges', 'strawberries']
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: ['strawberries', 'oranges', 'apples']
    """
    if order == 0:
        return to_sort.copy()
    elif order == 1:
        new = []
        while to_sort != []:
            min_index = find_min(to_sort)
            new.append(to_sort[min_index])
            to_sort.pop(min_index)
        return new
    elif order == 2:
        new = []
        while to_sort:
            max_index = find_max(to_sort)
            new.append(to_sort[max_index])
            to_sort.pop(max_index)
        return new
    
    else:
        return to_sort.copy()
    
def find_min(to_sort):
    min_item = to_sort[0]
    min_index = 0
    i = 1
    while i < len(to_sort):
        if cmp_item(to_sort[i], min_item) < 0:
            min_item = to_sort[i]
            min_index = i
        i += 1
    return min_index
def find_max(to_sort):
    max_item = to_sort[0]
    max_index = 0
    i = 1
    while i < len(to_sort):
        if cmp_item(to_sort[i], max_item) > 0:
            max_item = to_sort[i]
            max_index = i
        i += 1
    return max_index

def cmp_item (item1,item2):
    if type(item1) == tuple or type(item1) == list:
        if item1[0] < item2[0]:
            return -1
        if item1[0] == item2[0]:
            return 0 
        if item1[0] > item2[0]:
            return 1
    else:
        if item1 < item2:
            return -1
        if item1 == item2:
            return 0 
        if item1 > item2:
            return 1
        


def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    if fobj is None:
        return[]
    contents = fobj.readlines()[1:]
    result = []
    i = 0
    while i < len(contents):
        sid,name,time = contents[i].strip("\n").split(",")
        if time == "":
            time = 0
        else:
            time = int(time)

        result.append ((sid,name,time))
        i += 1
    result = sort(result, 1)
    result2 = []
    i = 0
    while i < len(result):
        sid,name,time = result[i]
        cand = candidate.Candidate(sid,name,time)
        result2.append(cand)
        i += 1
    return result2

