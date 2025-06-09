import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime
 
load_dotenv()

# environment parameters
conn_params = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "dbname": os.getenv("DB_NAME")
}

# BD Connection 
conn = psycopg2.connect(**conn_params)

def add_new_client():
    try:
        nome = input('Qual o seu nome e apelido? ')
        email = input('Qual o seu email? ')
        data_registo = datetime.now()
        query = 'INSERT INTO clientes (nome, email, data_registo) VALUES (%s, %s, %s);'
        cur = conn.cursor()
        cur.execute(query, (nome, email, data_registo))
        conn.commit()
        cur.close()
        print('Cliente inscrito com sucesso!')
    except Exception as e:
        print('Não foi possível realizar a inclusão do novo cliente. Tente novamente!')
        print(f'Erro: {e}')
    
def delete_client():
    try:
        id_cliente = input('Indique o ID do cliente a qual gostaria de eliminar a inscrição em nosso banco de dados: ')
        cur = conn.cursor()
        cur.execute('SELECT nome FROM clientes WHERE id = %s', (id_cliente,))
        nome = cur.fetchone()[0]  # retorna o primeiro elemento, o nome.
        
        if not nome:
            print('ID não encontrado! Confirme se o ID é realmente esse e tente novamente...')
            cur.close()
            return
        
        confirmacao = input(f'vamos excluir da base de dados o cliente {nome}. Confirmas? (s/n): ')
        
        if confirmacao.lower() == 's':
            cur.execute('DELETE FROM clientes WHERE id = %s;', (id_cliente,))
            conn.commit()
            cur.close()
            print(f'O cliente {nome} foi excluído da nossa base de dados.')
        elif confirmacao.lower == 'n':
            print('Ok.. vamos voltar para a tela inicial...')
            cur.close()
            return
        else:
            print('Opss... Digite s para Sim ou n para Não. Vamos tentar de novo?')
            cur.close()
            return
    except Exception as e:
        print('Não foi possível eliminar esse cliente de nossa base de dados. Certifique-se que o ID digitado exista e tente novamente mais tarde...')
        print(f'Erro: {e}')

def update_client():
    try:
        id_cliente = input('Indique o ID do cliente inscrito a qual gostaria de alterar o nome ou email em nosso banco de dados: ')
        cur = conn.cursor()
        cur.execute('SELECT nome FROM clientes WHERE id = %s;', (id_cliente,))
        nome = cur.fetchone()[0]
        
        if not nome:
            print('ID não encontrado! Confirme se o ID é realmente esse e tente novamente...')
            cur.close()
            return
        
        confirmacao = input(f'vamos atualizar os dados do cliente {nome}. Tens certeza disso? (s/n): ')
        
        if confirmacao.lower() == 's':
            parametro = input('''
                            Selecione uma das opções para alteração do registo:
                            1. Nome e apelido.
                            2. Email.
                            3. Cancelar.
                            
                            ''')
            if parametro == '1':
                novo_nome = input('Novo nome completo: ')
                cur.execute('UPDATE clientes SET nome = %s WHERE id = %s;', (novo_nome, id_cliente))
                conn.commit()
                print('O nome foi atualizado com sucesso!')
            elif parametro == '2':
                novo_email = input('Novo email: ') 
                cur.execute('UPDATE clientes SET email = %s WHERE id = %s;', (novo_email, id_cliente))
                conn.commit()
                print('Email atualizado com sucesso!')
            elif parametro == '3':
                print('A voltar para o menu inicial...')
            else:
                print('Escolha um número válido no Menu!!')
                cur.close()
                update_client()
            cur.close()
        elif confirmacao.lower() == 'n':
            print('Ok.. vamos voltar para a tela inicial...')
            cur.close()
            return
        else:
            print('Opss... Digite s para Sim ou n para Não. Vamos tentar de novo?')
            cur.close()
            update_client()
    except Exception as e:
        print('Não foi possível alterar os dados em nosso Banco de Dados. Tente novamente mais tarde!')
        print(f'Erro: {e}')
        conn.rollback()  # Para desfazer possiveis alterações parciais antes da quebra.     

def make_search():
    try:
        print('Lista de todos os clientes inscritos:')
        query = 'SELECT * FROM clientes ORDER BY data_registo DESC;'
        cur = conn.cursor()
        cur.execute(query)
        clientes = cur.fetchall()
        print(f'{"ID":<3}  |   {"Nome":<20}  |   {"Email":<30}  |   {"Data do Registo":<15}')
        print('-' * 86)
        for cliente in clientes:
            id, nome, email, data = cliente
            data_formatada = data.strftime('%Y-%m-%d') if hasattr(data, 'strftime') else str(data)
            print(f'{id:<3}  |   {nome:<20}  |   {email:<30}  |   {data_formatada:<15}')
        cur.close()
    except Exception as e:
        print('Não foi possível fazer a pesquisa de clientes em nosso banco de dados. Tente novamente mais tarde!')
        print(f'Erro: {e}')
        
def main_menu():
    menu = True
    while menu:
        option = input('''
                       Escolha uma das opções:
                        1. Adicionar novo cliente.
                        2. Remover cliente.
                        3. Atualizar dados de cliente.
                        4. Ver clientes inscritos.
                        5. Sair
                        
                        ''')
        
        if option == '1':
            add_new_client()
        elif option == '2':
            delete_client()
        elif option == '3':
            update_client()
        elif option == '4':
            make_search()
        elif option == '5':
            print('A sair da aplicação...')
            menu = False
        else:
            print('Selecione um item do menu válido')
            
            
if __name__ == '__main__':
    main_menu()