import json
import os

class AnswerGenerator():
    def __init__(self, section_name):
        self.name = section_name
        self.answers = {}
        
    def add_answer(self, question, *answers):
        self.answers[question] = answers
        
    def save(self):
        json_object = json.dumps(self.answers, indent=1)
 
        # Writing to sample.json
        with open(f'{self.name}.json', "w+") as f:
            f.write(json_object)
            
if __name__ == '__main__':
    s1 = AnswerGenerator('Section 1')
    s1.add_answer('Q1 - short answer', 
                  'short answer')
    s1.add_answer('Q2 - short answer (required)', 
                  'short answer')
    s1.add_answer('Q3 - paragraph',
                  'looooooooooooooooooooooooooooooooooooooooooooooooong answer')
    s1.add_answer('Q4 - paragraph (required)', 
                  'looooooooooooooooooooooooooooooooooooooooooooooooong answer')
    s1.add_answer('Q5 - Multiple choice', 
                  'Option 1')
    s1.add_answer('Q6 - Multiple choice (required)', 
                  'Option 2')
    s1.add_answer('Q7 - checkboxes',
                  'Option 1', 'Option 2')
    s1.add_answer('Q8 - checkboxes (with a response validation)',
                  'Option 1', 'Option 2', 'Option 3')
    s1.add_answer('Q9 - checkboxes (required)', 
                  'Option 2', 'Option 3')
    s1.add_answer('Q10 - Drop-down',  
                  'Option 1')
    s1.add_answer('Q11 - Drop-down (required)',  
                  'Option 2')
    s1.add_answer('Q12 - Linear scale',  
                  '4')
    s1.add_answer('Q13 - Linear scale (required)',
                  '5')
    s1.add_answer('Q14 - Multiple-choice grid', 
                  ('Row 1', 'Column 1'), ('Row 2', 'Column 1'))
    s1.add_answer('Q15 - Multiple-choice grid (with a limit)',  
                  ('Row 1', 'Column 2'), ('Row 2', 'Column 1'))
    s1.add_answer('Q16 -  Multiple-choice grid (required)',  
                  ('Row 1', 'Column 1'), ('Row 2', 'Column 2'), ('Row 3', 'Column 1'))
    s1.add_answer('Q17 - Tick box grid',  
                  ('Row 1', 'Column 1'), ('Row 1', 'Column 2'))
    s1.add_answer('Q18 - Tick box grid (with a limit)',
                  ('Row 1', 'Column 1'), ('Row 2', 'Column 2'), ('Row 3', 'Column 3'))
    s1.add_answer('Q19 - Tick box grid (required)',
                  ('Row 1', 'Column 1'), ('Row 2', 'Column 2'), ('Row 3', 'Column 4'))
    s1.add_answer('Q24 - Time' ,  
                  '10:10')
    s1.add_answer('Q25 - Time (Duration)',  
                  '10:10:10')
    s1.add_answer('Q26 - Time (required)', 
                  '10:10')
    s1.save()
    
    s2 = AnswerGenerator('Section 2')
    s2.add_answer('Q1', 
                  'Option 1')
    s2.add_answer('Q2',
                  'Option 2', 'Option 3')
    s2.add_answer('Q3', 
                  'Option 1')
    s2.add_answer('Rate that doggo',
                  '10')
    s2.add_answer('Cats vs Dogs',
                  'Dogs')
    s2.save()
    
    s3 =  AnswerGenerator('Section 3')
    s3.add_answer('Lobby',
                  'Go to section 4')
    s3.save()
