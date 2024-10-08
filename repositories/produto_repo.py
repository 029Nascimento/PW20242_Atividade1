from typing import List, Optional  # Importa List e Optional para definir tipos de retorno
from models.usuario_model import Usuario  # Importa a classe Usuario, que define o modelo de um usuário
from sql.usuario_sql import SQL_CRIAR_TABELA, SQL_INSERIR, SQL_OBTER_TODOS  # Importa as queries SQL
from util import obter_conexao  # Importa uma função para obter a conexão com o banco de dados


# Função para criar a tabela no banco de dados
def criar_tabela():
    # Obtém uma conexão com o banco de dados
    with obter_conexao() as conexao:
        db = conexao.cursor()  # Cria um cursor para executar comandos SQL
        db.execute(SQL_CRIAR_TABELA)  # Executa o SQL para criar a tabela de usuários


# Função para inserir um usuário no banco de dados
# O parâmetro `usuario` é um objeto da classe `Usuario`
# Retorna `Optional[Usuario]`, ou seja, pode retornar o usuário inserido ou None
def inserir(usuario: Usuario) -> Optional[Usuario]:
    # Obtém uma conexão com o banco de dados
    with obter_conexao() as conexao:
        db = conexao.cursor()  # Cria um cursor para executar comandos SQL
        # Executa o SQL de inserção passando os dados do usuário como parâmetros
        db.execute(SQL_INSERIR, (
            usuario.nome,  # Nome do usuário
            usuario.email,  # Email do usuário
            usuario.telefone,  # Telefone do usuário
            usuario.data_nascimento,  # Data de nascimento do usuário
            usuario.senha  # Senha do usuário
        ))


# Função para obter todos os usuários do banco de dados
# Retorna uma lista de objetos `Usuario`
def obter_todos() -> List[Usuario]:
    # Obtém uma conexão com o banco de dados
    with obter_conexao() as conexao:
        db = conexao.cursor()  # Cria um cursor para executar comandos SQL
        tuplas = db.execute(SQL_OBTER_TODOS).fetchall()  # Executa o SQL para obter todos os usuários e pega os resultados
        # Converte cada tupla de dados em um objeto `Usuario`
        usuarios = [Usuario(*t) for t in tuplas]
        return usuarios  # Retorna a lista de usuários
