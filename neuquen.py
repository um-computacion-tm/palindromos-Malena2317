import unittest

def is_palindrome(mystring):
    mystring = mystring.lower().replace(" ", "") # elimina los especios en las palabras
    return mystring == mystring[::-1] # compara la palabra con su reverso 

class TestPalindrome(unittest.TestCase):
    def test_neuquen(self):
        resultado = is_palindrome('n euq uen')
        self.assertEqual(resultado, True)
    
    def test_neunen(self):
        resultado = is_palindrome('neuen') # pali
        self.assertEqual(resultado, True)
    
    def test_quenen  (self):
        resultado = is_palindrome('quenen ') #no es 
        self.assertEqual(resultado, False)
    
    def test_neuqueneu(self):
        resultado = is_palindrome('neuqueneu') #no  es 
        self.assertEqual(resultado, False)

    def test_nen(self):
        resultado = is_palindrome('nen') #si es 
        self.assertEqual(resultado, True) 

    def test_nenqu(self):
        resultado = is_palindrome('nenqu') #no es 
        self.assertEqual(resultado, False)

    def test_neunqe (self):
        resultado = is_palindrome('neunqe ') #no es 
        self.assertEqual(resultado, False)
 
    def test_ueneu (self):
        resultado = is_palindrome('ueneu ') #si es 
        self.assertEqual(resultado, True)

unittest.main()
