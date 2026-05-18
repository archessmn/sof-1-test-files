from test_class import TestCase, number

from question_2 import union


class Question2Test(TestCase):

    # @weight(3)
    @number("2.1")
    def testUnionNoOverlaping(self):
        """
        Question 2: Test results when the union keeps all the spheres from both objects. That is when the objects are not overlapping.
        """
        object1 = {(1, 1, 1, 2), (3, 0, 0, 3)}
        object2 = {(0, 0, 0, 2), (-1, 0, 0, 2), (0, -1, 0, 2)}
        result = {(1, 1, 1, 2), (3, 0, 0, 3), (0, 0, 0, 2),
                  (-1, 0, 0, 2), (0, -1, 0, 2)}
        self.assertEqual(union(object1, object2), result)

    # @weight(6)
    @number("2.2")
    def testUnionWithOverlaps(self):
        """
        Question 2: Test that the union removes inscribed spheres from one of the object when only one object contains inscribed spheres.
        """
        object1 = {(1, 1, 1, 2), (3, 0, 0, 3)}
        object2 = {(1, 1, 1, 2), (0, 0, 0, 2), (-1, 0, 0, 2), (0, -1, 0, 2)}
        result = {(1, 1, 1, 2), (3, 0, 0, 3), (0, 0, 0, 2),
                  (-1, 0, 0, 2), (0, -1, 0, 2)}
        self.assertEqual(union(object1, object2), result)
        object2 = {(1.1, 1.1, 1.2, 1), (0, 0, 0, 2),
                   (-1, 0, 0, 2), (0, -1, 0, 2)}
        self.assertEqual(union(object1, object2), result)

    # @weight(6)
    @number("2.3")
    def testUnionWithOverlapsFromBothObjects(self):
        """
        Question 2: Test that the union removes inscribed spheres from both objects when both objects have inscribed spheres.
        """
        object1 = {(1, 1, 1, 2), (3, 0, 0, 3),
                   (10, 10, 10, 2), (-10, -10, -9, 1)}
        object2 = {(1.1, 1.1, 1.2, 3), (5, 0, 0, 1), (-1, 0, 0, 2),
                   (0, -1, 0, 2), (10, 10, 9, 1), (-10, -10, -10, 2)}
        result = {(1.1, 1.1, 1.2, 3), (3, 0, 0, 3), (-1, 0, 0, 2),
                  (0, -1, 0, 2), (-10, -10, -10, 2), (10, 10, 10, 2)}
        self.assertEqual(union(object1, object2), result)
