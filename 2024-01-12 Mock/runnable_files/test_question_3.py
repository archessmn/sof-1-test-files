from test_class import TestCase, number

from question_3 import getPasserRating


class Question3Test(TestCase):

    # @weight(3)
    @number("3.1")
    def testFileWithComments(self):
        """
        Question 3: Test results when the files contains comments and all entries are valid, that is the file respect the format given in the paper.
        """
        self.assertEqual({'Justin Herbert': 102.2, 'Matt Ryan': 85.0, 'Jalen Hurts': 99.6},
                         getPasserRating('Data/nfl2022WithComments.csv'))

    # @weight(5)
    @number("3.2")
    def testFileWithoutComments(self):
        """
        Question 3: Test results when the files does not contain comments and all entries are valid, that is the file respect the format given in the paper.
        """
        self.assertEqual({'Jared Goff': 99.9, 'Josh Allen': 101.0},
                         getPasserRating('Data/nfl2022WithoutComments.csv'))

    # @weight(2)
    @number("3.3")
    def testFileWithScaledValues(self):
        """
        Question 3: Test results when the files contains players statistics that need to be scaled between 0 and 2.375.
        """
        self.assertEqual({'Lilian Blot': 41.7, 'Nick Pears': 120.4},
                         getPasserRating('Data/nfl2022ScaledStats.csv'))

    # @weight(3)

    @number("3.4")
    def testFileWithDuplicatePlayers(self):
        """
        Question 3: Test that the function raise a KeyError if the files if the file contains more than one data set for a given player, that is two lines or more contain the same player's name.
        """
        self.assertRaises(KeyError, getPasserRating,
                          'Data/nfl2022WithDuplicates.csv')

    # @weight(2)
    @number("3.5")
    def testFileWithInvalidFormat(self):
        """
        Question 3: Test that the function raises a ValueError if the file does not follow the format described in the paper. For example at least one line has not enough entries, or too many of them. Also checks that a ValueError is raised if the numerical entries are not int. 
        """
        self.assertRaises(ValueError, getPasserRating,
                          'Data/nfl2022TooManyEntries.csv')
        self.assertRaises(ValueError, getPasserRating,
                          'Data/nfl2022TooFewEntries.csv')
        self.assertRaises(ValueError, getPasserRating,
                          'Data/nfl2022InvalidNumberFormat.csv')
