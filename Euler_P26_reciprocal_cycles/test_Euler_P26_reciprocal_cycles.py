import unittest
from Euler_P26_reciprocal_cycles import (
    create_factor_list,
    gcd,
    coprime_test,
    create_prime_list,
    create_prime_factors_list,
    create_totient_list,
    prime_factorization,
    do_mod_multiplication,
    check_terminating_denominators,
    remove_terminating_denominators,
    
)

class TestMathFunctions(unittest.TestCase):

    def test_create_factor_list(self):
        self.assertEqual(create_factor_list(16), [1,2,4,8,16])
        self.assertEqual(create_factor_list(12), [1,2,3,4,6,12])
        self.assertRaises(ValueError, create_factor_list, -4)
        self.assertRaises(ValueError, create_factor_list, 0)
        self.assertRaises(ValueError, create_factor_list, 0.5)
        
    def test_gcd(self):
        self.assertEqual(gcd(60,42), 6)
        self.assertEqual(gcd(100,81), 1)
        self.assertRaises(ValueError, gcd, -1, 1)
        self.assertRaises(ValueError, gcd, 0.5, 1)
        self.assertRaises(ValueError, gcd, 1, -1)
        self.assertRaises(ValueError, gcd, 1, 1.5)
    
    def test_coprime_test(self):
        self.assertEqual(coprime_test(20, 9), True)
        self.assertEqual(coprime_test(20, 4), False)
        pass

    def test_create_prime_list(self):
        self.assertEqual(create_prime_list(29), [2,3,5,7,11,13,17,19,23,29])
        self.assertEqual(create_prime_list(30), [2,3,5,7,11,13,17,19,23,29])
        
    def test_create_prime_factors_list(self):
        self.assertEqual(create_prime_factors_list(10), [2,5])
        self.assertEqual(create_prime_factors_list(17), [17])
        self.assertEqual(create_prime_factors_list(20), [2,5])
        self.assertEqual(create_prime_factors_list(30), [2,3,5])
        self.assertEqual(create_prime_factors_list(90), [2,3,5])
        self.assertEqual(create_prime_factors_list(2), [2])
        self.assertEqual(create_prime_factors_list(1), [])
        
    def test_create_totient_list(self):
        self.assertEqual(create_totient_list(9), [1,2,4,5,7,8])
        self.assertEqual(create_totient_list(1), [1])

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(10), [2,5])
        self.assertEqual(prime_factorization(17), [17])
        self.assertEqual(prime_factorization(20), [2,2,5])
        self.assertEqual(prime_factorization(30), [2,3,5])
        self.assertEqual(prime_factorization(90), [2,3,3,5])

    def test_do_mod_multiplication(self):
        self.assertEqual(do_mod_multiplication(5,117,19), 1)
        self.assertEqual(do_mod_multiplication(10,6,7), 1)
        self.assertEqual(do_mod_multiplication(10,2,11), 1)
        self.assertEqual(do_mod_multiplication(10,21,129), 1)

    def test_check_terminating_denominators(self):
        self.assertEqual(check_terminating_denominators(2), True)
        self.assertEqual(check_terminating_denominators(5), True)
        self.assertEqual(check_terminating_denominators(10), True)
        self.assertEqual(check_terminating_denominators(15), False)
        self.assertEqual(check_terminating_denominators(100), True)
        self.assertEqual(check_terminating_denominators(21), False)
        self.assertEqual(check_terminating_denominators(6), False)
        self.assertEqual(check_terminating_denominators(1), None)
        
    def test_remove_terminating_denominators(self):
        list_test_remove1=[3,6,7,9,11,12,13,14,15,17,18,19,21,22,23,24]
        test_range1 = list(range(2,26))
        self.assertEqual(remove_terminating_denominators(test_range1), list_test_remove1)  
    
if __name__=='__main__':
    unittest.main()

    


