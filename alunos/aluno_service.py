from datetime import date, datetime, timedelta
import os
import shutil
import hashlib
from aluno_model import Aluno, db
from sqlalchemy import func

def adicionar_aluno(data):
    
    novo_aluno = Aluno(**data)
    db.session.add(novo_aluno)
    nome_pasta_aluno = criar_pasta_aluno(novo_aluno.id)
    novo_aluno.pasta_id = nome_pasta_aluno
    db.session.commit()
    return novo_aluno

def obter_todos_alunos():
    return Aluno.query.all()

def obter_aluno_por_id(aluno_id):
    return Aluno.query.get(aluno_id)

def atualizar_aluno(aluno, data):
    if 'data_diagnostico' in data and data['data_diagnostico']:
        data['data_diagnostico'] = datetime.strptime(data['data_diagnostico'], "%Y-%m-%d").date()

    for key, value in data.items():
        setattr(aluno, key, value)

    db.session.commit()
    return aluno

def excluir_aluno(aluno):
    db.session.delete(aluno)
    db.session.commit()
    return aluno

def buscar_alunos_por_nome(termo_busca):
    if not termo_busca:
        raise ValueError("O parâmetro 'nome' é obrigatório")

    return Aluno.query.filter(Aluno.nome.ilike(f'%{termo_busca}%')).all()

def atualizar_parcialmente_aluno(aluno, data):
    for key, value in data.items():
        setattr(aluno, key, value)

    db.session.commit()
    return aluno

def obter_filtrado(campos=None, filtro=None):
    try:
        if campos is None:
            campos = ['id', 'nome']  # Definindo campos padrão se não forem fornecidos

        # Construir a query dinamicamente com os campos selecionados
        query = db.session.query(*[getattr(Aluno, campo) for campo in campos])

        # Aplicar filtro se fornecido
        if filtro:
            campo, operador, valor = filtro
            campo_attr = getattr(Aluno, campo)
            if operador == '==':
                query = query.filter(campo_attr == valor)
            elif operador == 'like':
                query = query.filter(campo_attr.ilike(f'%{valor}%'))
            elif operador == '>':
                query = query.filter(campo_attr > valor)
            elif operador == '<':
                query = query.filter(campo_attr < valor)
            else:
                raise ValueError(f"Operador '{operador}' não é suportado.")  # Lançar exceção para operador não suportado

        # Executar a query
        alunos_filtrados = query.all()

        # Serializar os alunos encontrados
        alunos_serializados = []
        for aluno in alunos_filtrados:
            aluno_dict = {}
            for campo in campos:
                valor = getattr(aluno, campo)
                if isinstance(valor, datetime):
                    valor = valor.isoformat() if valor else None
                aluno_dict[campo] = valor
            alunos_serializados.append(aluno_dict)

        return alunos_serializados

    except Exception as e:
        raise ValueError(f"Erro ao filtrar alunos: {str(e)}")  # Lançar exceção com a descrição do erro

def remover_formatacao_cpf(cpf_formatado):
    # Remove caracteres que não são dígitos
    cpf = ''.join(filter(str.isdigit, cpf_formatado))
    return cpf

def validar_cpf(cpf_formatado):
    
   # Remove formatação do CPF
    cpf = remover_formatacao_cpf(cpf_formatado)

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula os dígitos verificadores
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = resto

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = resto

    # Verifica se os dígitos verificadores estão corretos
    if int(cpf[9]) == digito_verificador_1 and int(cpf[10]) == digito_verificador_2:
        return True

    return False

def calcular_idade_em_meses(data_nascimento):
    # Calcula a idade em meses com base na data de nascimento
    hoje = date.today()
    idade_em_meses = (hoje.year - data_nascimento.year) * 12 + hoje.month - data_nascimento.month
    return idade_em_meses

def validar_idade(data_nascimento, meses_desejados):
    hoje = date.today()
    data_futura = data_nascimento + timedelta(days=meses_desejados * 30)  # Aproximação de meses para dias

    if hoje < data_futura:
        return -1  # Menor
    elif hoje == data_futura:
        return 0  # Igual
    else:
        return 1  # Maior

    
def formatar_nome(nome):
    if not nome:
        return ""  # Retorna uma string vazia se a entrada for vazia

    # Converte todas as palavras para minúsculas
    palavras = nome.lower().split()

    # Lista de prefixos a serem tratados
    prefixos = ['da', 'das', 'de', 'do', 'dos']

    # Formata a primeira letra de cada palavra
    palavras_formatadas = [palavra.capitalize() if palavra not in prefixos else palavra for palavra in palavras]

    # Une as palavras formatadas
    nome_formatado = ' '.join(palavras_formatadas)

    return nome_formatado

def criar_pasta_aluno(aluno_id):
    # Crie um hash único baseado no ID do aluno
    hash_aluno = hashlib.sha256(str(aluno_id).encode()).hexdigest()[:8]

    # Diretório onde as pastas dos alunos serão armazenadas
    base_dir = './documentos/'

    # Crie o caminho completo para a nova pasta
    pasta_aluno = os.path.join(base_dir, f'aluno_{hash_aluno}')

    # Crie a pasta se não existir
    os.makedirs(pasta_aluno, exist_ok=True)
    shutil.copy('./assets/p.jpg', os.path.join(pasta_aluno, 'p.jpg'))
    
    return f'aluno_{hash_aluno}'
