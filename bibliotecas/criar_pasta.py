import os
import hashlib
import shutil

def criar_pasta(nome, id, base_dir='./documentos/'):
    # Crie um hash único baseado no ID da entidade
    hash_entidade = hashlib.sha256(str(id).encode()).hexdigest()[:8]

    # Crie o caminho completo para a nova pasta
    pasta_entidade = os.path.join(base_dir, f'{nome}_{hash_entidade}')

    # Crie a pasta se não existir
    os.makedirs(pasta_entidade, exist_ok=True)

    return f'{nome}_{hash_entidade}'


