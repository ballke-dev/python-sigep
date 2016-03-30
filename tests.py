import unittest
from sigep import *


class MainTest(unittest.TestCase):

    def test_01_consulta_cep(self):
        params = {
            'cep': '89802100',
            'sandbox': True
        }

        obj = ConsultaCEP(**params)
        dados = obj.do()
        self.assertEqual(dados.get('uf'), 'SC')

if __name__ == '__main__':
    unittest.main()