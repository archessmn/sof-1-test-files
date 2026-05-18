from test_class import TestCase, number

from question_1 import extractText


class Question1Test(TestCase):

    # @weight(6)
    @number("1.1")
    def testExtractText(self):
        """
        Question 1: Test results when inputs are not empty and return the function returns a non empty string.
        """
        self.assertEqual(extractText('The term conda is not recognised as the name of a', 'theAsORin'),
                         'The is not as the a')
        self.assertEqual(extractText('The term conda is not recognised as the name of a', 'theAsORinmcdgF'),
                         'The term conda is not recognised as the name of a')

    # @weight(2)
    @number("1.2")
    def testEmptyText(self):
        """
        Question 1: Test that an empty string is return if the input text is also empty.
        """
        self.assertEqual(extractText('', 'theAsORin'), '')

    # @weight(2)
    @number("1.3")
    def testNoMatchingCharacters(self):
        """
        Question 1: Test an emtpy string is returned if there are no word matching the keys.
        """
        self.assertEqual(extractText(
            'The term conda is not recognised as the name of a', 'thsORm'), '')
