from django.test import TestCase
from texToPdf.files import Files

class FileTestCase(TestCase):
    def setUp(self):
        self.fileTest = Files()
    
    def test_load_files(self):
        self.assertEqual(self.fileTest.questionsFiles['ex1.tex'], ['easy', 'math', 'sum'])

        self.assertEqual(self.fileTest.questionsFiles['ex2.tex'], ['medium', 'bio', 'cells'])

    def test_get_files_list(self):
        self.assertSetEqual(set(self.fileTest.getListQuestions(['easy'])), set(['ex1.tex', 'ex3.tex', 'ex5.tex']))

        self.assertSetEqual(set(self.fileTest.getListQuestions(['easy', 'math'])), set(['ex1.tex', 'ex5.tex']))

        self.assertSetEqual(set(self.fileTest.getListQuestions(['easy', 'math', 'cells'])), set([]))

        self.assertSetEqual(set(self.fileTest.getListQuestions(['medium', 'bio', 'cells'])), set(['ex2.tex']))

        self.assertSetEqual(set(self.fileTest.getListQuestions(['easy', 'math', 'alg'])), set(['ex1.tex', 'ex5.tex']))

        self.assertSetEqual(set(self.fileTest.getListQuestions(['hard'])), set([]))

    def test_get_one_files(self):
        self.assertIn(self.fileTest.getQuestionFromTag(['easy']), self.fileTest.getListQuestions(['easy']))

        self.assertIn(self.fileTest.getQuestionFromTag(['easy', 'math']), self.fileTest.getListQuestions(['easy', 'math']))

        self.assertEqual(self.fileTest.getQuestionFromTag(['easy', 'math', 'cells']), None)

        self.assertIn(self.fileTest.getQuestionFromTag(['medium', 'bio', 'cells']), self.fileTest.getListQuestions(['medium', 'bio', 'cells']))

        self.assertIn(self.fileTest.getQuestionFromTag(['easy', 'math', 'alg']), self.fileTest.getListQuestions(['easy', 'math', 'alg']))

        self.assertEqual(self.fileTest.getQuestionFromTag(['hard']), None)
        