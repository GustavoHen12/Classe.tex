import sys
import os
import random

class Files:
    def __init__(self):
        self.questionsFiles = {}
        self.tags = {}

        self.loadFiles()
    
    def loadFiles(self):
        folder = os.path.dirname(os.path.abspath(__file__)) + '/questions'
        #get questions files
        questions = {}
        tags = {}
        for dirpath, dirnames, fileNames in os.walk(folder):
            for fileName in fileNames:
                if (os.path.splitext(fileName)[-1].lower() == '.tex'):
                    #get tags
                    file = open(os.path.join(dirpath, fileName), 'r')
                    tagLine = file.readline()
                    #process tags
                    if(tagLine.find('%<tags>') >= 0 and tagLine.find('</tags>%') >= 0):
                        tagStr = tagLine[tagLine.find('%<tags>') + 7:tagLine.find('</tags>%')]
                        tagList = []
                        for tag in tagStr.split(','):
                            if(len(tag) > 0):
                                #for dictionary by questions
                                tagList.append(tag.strip())
                                
                                #for dictionary by tags
                                fileList = []
                                if tag.strip() in tags:
                                    fileList = tags[tag.strip()]
                                #fileList.append(os.path.join(dirpath, fileName))
                                fileList.append(os.path.join(fileName))
                                tags[tag.strip()] = fileList

                        #questions[os.path.join(dirpath, fileName)] = tagList
                        questions[fileName] = tagList
        self.questionsFiles = questions
        self.tags = tags
        
        return (questions, tags)

    #get random question from tag list
    def getQuestionFromTag(self, tags):
        questionFilesList = self.getListQuestions(tags)
        if(len(questionFilesList) == 0):
            return None
        return random.choice(questionFilesList)

    #get list of all questions with tags
    def getListQuestions(self, tags):
        allFilesList = []
        fileList = []
        for tag in tags:
            if tag.strip() in self.tags:
                allFilesList.append(self.tags[tag.strip()])

        if(len(allFilesList) == 1):
            return(allFilesList[0])
        else:
            if(len(allFilesList) > 1):
                fileList = set(allFilesList[0]).intersection(*allFilesList[1:])
        
        return list(fileList)