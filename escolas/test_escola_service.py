import unittest
from datetime import datetime
from escola_model import db, escola
from escola_service import (
    create_escola,
    get_escola,
    get_all_escolas,
    update_escola,
    delete_escola
)

class EscolaServiceTest(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.app = create_app()  # Certifique-se de ter uma função create_app() em seu código
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        # Limpeza após os testes
        db.session.remove()
        db.drop_all()

    def test_create_escola(self):
        data = {
            'nome': 'Escola Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '123456789',
            'data_criacao': datetime.now()
        }

        created_escola = create_escola(data)
        self.assertIsNotNone(created_escola.id)

    def test_get_escola(self):
        data = {
            'nome': 'Escola Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '123456789',
            'data_criacao': datetime.now()
        }

        created_escola = create_escola(data)
        retrieved_escola = get_escola(created_escola.id)

        self.assertIsNotNone(retrieved_escola)
        self.assertEqual(retrieved_escola.nome, 'Escola Teste')

    def test_get_all_escolas(self):
        data1 = {
            'nome': 'Escola Teste 1',
            'endereco': 'Rua Teste, 123',
            'telefone': '123456789',
            'data_criacao': datetime.now()
        }
        data2 = {
            'nome': 'Escola Teste 2',
            'endereco': 'Rua Teste, 456',
            'telefone': '987654321',
            'data_criacao': datetime.now()
        }

        create_escola(data1)
        create_escola(data2)

        all_escolas = get_all_escolas()
        self.assertEqual(len(all_escolas), 2)

    def test_update_escola(self):
        data = {
            'nome': 'Escola Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '123456789',
            'data_criacao': datetime.now()
        }

        created_escola = create_escola(data)

        update_data = {'nome': 'Escola Atualizada'}
        updated_escola = update_escola(created_escola.id, update_data)

        self.assertEqual(updated_escola.nome, 'Escola Atualizada')

    def test_delete_escola(self):
        data = {
            'nome': 'Escola Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '123456789',
            'data_criacao': datetime.now()
        }

        created_escola = create_escola(data)
        delete_escola(created_escola.id)
        deleted_escola = get_escola(created_escola.id)

        self.assertIsNone(deleted_escola)

if __name__ == '__main__':
    unittest.main()
