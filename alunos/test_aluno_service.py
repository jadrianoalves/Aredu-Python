# test_aluno_service.py

import unittest
from datetime import date, timedelta, datetime
from aluno_service import validar_cpf, calcular_idade_em_meses, validar_idade, formatar_nome

class TestAlunoService(unittest.TestCase):

    def test_validar_cpf(self):
        self.assertTrue(validar_cpf("12345678909"))  # CPF válido
        self.assertFalse(validar_cpf("12345678901"))  # CPF inválido
        self.assertFalse(validar_cpf("abcde"))  # CPF com caracteres não numéricos
        self.assertFalse(validar_cpf(""))  # CPF vazio
        self.assertTrue(validar_cpf("123.456.789-09"))  # CPF com formatação inválida

    def test_calcular_idade_em_meses(self):
        data_nascimento = date(1990, 1, 15)
        hoje = date.today()
        resultado_esperado = (hoje.year - data_nascimento.year) * 12 + hoje.month - data_nascimento.month
        self.assertEqual(calcular_idade_em_meses(data_nascimento), resultado_esperado)

    def test_validar_idade(self):
        data_nascimento = date(1990, 1, 15)
        meses_desejados = 120  # 10 anos
        self.assertEqual(validar_idade(data_nascimento, meses_desejados), 1)  # Maior
        self.assertEqual(validar_idade(data_nascimento, 800), -1)  # Menor

    def test_formatar_nome(self):
        self.assertEqual(formatar_nome("joão da silva"), "João da Silva")
        self.assertEqual(formatar_nome("MARIA DOS SANTOS"), "Maria dos Santos")
        self.assertEqual(formatar_nome(""), "")  # String vazia
        

if __name__ == '__main__':
    unittest.main()
