import unittest                
from python.funciones_auxiliares import calculariva             
class tests_iva(unittest.TestCase):          
    def test_iva(self):
        self.assertEqual(calculariva(100),21)                 
        self.assertEqual(calculariva(0.2),0.042)
        self.assertEqual(calculariva(200000),42000)
if __name__ == '__main__':
    unittest.main()
