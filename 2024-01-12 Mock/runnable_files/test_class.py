from typing import Callable

from unittest import TestCase as Testy

Testy.assertListEqual


class TestCase:
    def assertEqual(self, first, second):
        print(f"Test {'passed' if first == second else 'failed'}")
        return True if first == second else False

    def assertNotEqual(self, first, second):
        print(f"Test {'passed' if first != second else 'failed'}")
        return True if first != second else False

    def assertTrue(self, check):
        print(f"Test {'passed' if check else 'failed'}")
        return check == True

    def assertFalse(self, check):
        print(f"Test {'passed' if not check else 'failed'}")
        return check == False

    def assertRaises(self, error, toCall, filename):
        try:
            try:
                toCall(filename)
                print("Test failed")

            except error:
                print("Test passed")
                return True
        except:
            print("Test failed")
        return False

    def assertListEqual(self, l1: list, l2: list):
        print(f"Test {'passed' if l1 == l2 else 'failed'}")
        return True if l1 == l2 else False


def number(number: int):
    def decorator(func: Callable[[None], None]):
        def wrapper(*args, **kwargs):
            doc = func.__doc__.replace('\n', '').replace("    ", "")
            print(f"\n\n{number}  {doc}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
