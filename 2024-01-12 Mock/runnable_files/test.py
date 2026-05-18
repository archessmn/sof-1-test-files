from test_question_1 import Question1Test
from test_question_2 import Question2Test
from test_question_3 import Question3Test
from test_question_4 import Question4iTest, Question4iiTest, Question4iiiTest, Question4ivTest


q1test = Question1Test()

q1test.testExtractText()
q1test.testEmptyText()
q1test.testNoMatchingCharacters()


q2test = Question2Test()

q2test.testUnionNoOverlaping()
q2test.testUnionWithOverlaps()
q2test.testUnionWithOverlapsFromBothObjects()

q3test = Question3Test()

q3test.testFileWithComments()
q3test.testFileWithoutComments()
q3test.testFileWithScaledValues()
q3test.testFileWithDuplicatePlayers()
q3test.testFileWithInvalidFormat()

q4itest = Question4iTest()

q4itest.testInit()
q4itest.testInitInvalidPuzzle()

q4iitest = Question4iiTest()

q4iitest.testMatchPattern()
q4iitest.testPatternDontMatch()

q4iiitest = Question4iiiTest()

q4iiitest.testMoves()
q4iiitest.testInvalidMoves()

q4ivtest = Question4ivTest()

q4ivtest.testSolvable()
