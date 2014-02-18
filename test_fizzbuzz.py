import unittest2
class FizzBuzz:
    def count(self, number):
        output = "Fizz" if number%3==0 else ''
        if number%5==0: output = output + "Buzz"
        else: output=output+''
        
        if output=='': return str(number)
        return output


class FizzBuzzTest(unittest2.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_1_should_return_1(self):
        self.assertEquals(self.fizzbuzz.count(1), '1')

    def test_2_should_return_2(self):
        self.assertEquals(self.fizzbuzz.count(2), '2')

    def test_3_should_return_fizz(self):
        self.assertEquals(self.fizzbuzz.count(3), 'Fizz')

    def test_5_should_return_buzz(self):
        self.assertEquals(self.fizzbuzz.count(5), 'Buzz')
    
    def test_6_should_return_fizz(self):
        self.assertEquals(self.fizzbuzz.count(6), 'Fizz')

    def test_10_should_return_buzz(self):
        self.assertEquals(self.fizzbuzz.count(10), 'Buzz')

    def test_15_should_return_fizzbuzz(self):
        self.assertEquals(self.fizzbuzz.count(15), 'FizzBuzz')

    def test_30_should_return_fizzbuzz(self):
        self.assertEquals(self.fizzbuzz.count(30), 'FizzBuzz')

