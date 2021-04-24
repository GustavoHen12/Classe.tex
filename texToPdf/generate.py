import sys
import os
import random

from texToPdf.files import Files

def generateTex (size):
    files = Files()

    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
    folderTemp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    #define tags

    #create temp file
    template = open(os.path.join(folder, 'template.tex'), 'r')
    temp = open(os.path.join(folderTemp, 'temp.tex'), 'w')

    for line in template.readlines():
        if(line.find('%<content/>%') == -1):
            temp.write(line)
        else:
            for index in range(size):
                question = files.getQuestionFromTag(['easy'])
                temp.write('\question \import{'+folder+'/}{'+question+'}\n')
    temp.close()


# exam = sys.argv[1]
# folder = sys.argv[2]

# questions = []
# for bank, number in zip(sys.argv[3::2], map(int, sys.argv[4::2])):
#     qfiles = [
#         os.path.join(dirpath, fname) 
#         for dirpath, dirnames, filenames in os.walk(os.path.join(folder, bank)) 
#         for fname in filenames 
#         if os.path.splitext(fname)[-1].lower() == '.tex'
#         ]
#     for qfile in random.sample(qfiles, number):
#         with open(qfile, 'r') as qfh:
#             questions.append(qfh.read())

# with open(exam, 'w') as efh:
#     for question in questions:
#         print(question, file=efh)