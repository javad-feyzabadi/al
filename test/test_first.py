from unittest import TestCase
import first
import traceback

class FirstTest(TestCase):
    
    def test_many(self):
        self.assertEqual(first.first(x for x in range(4)),0)

    def test_one(self):
        self.assertEqual(first.first([3]),3)

    def test_default(self):
        self.assertEqual(first.first([],'boo'),'boo')

    def test_empty_stop_iteration(self):
        try:
            first.first([])
        except ValueError:
            formatedd_exec = traceback.format_exc()
            self.assertIn('StopIteration',formatedd_exec)
            self.assertIn('The above exception was the direct cause',formatedd_exec)
        else:
            self.fail()
