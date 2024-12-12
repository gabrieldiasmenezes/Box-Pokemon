"""
INTEGRANTES:
RM:555019
NOME:Gabriel Dias Menezes

RM:554609
NOME:Júlia Soares Farias dos Santos

RM:558841
NOME:Hellen Marinho Cordeiro
"""
import os
os.system('cls')
import requests
import oracledb
from listaPkm import pokemons
def conexao():
    try:
        conn=oracledb.connect('RM555019/120306@oracle.fiap.com.br:1521/ORCL')
        print('Conectado')
        return conn
    except Exception as e:
        print(f'Error: {e}')
def inserir(n:str,h1:str,h2:str,h3:str,v1:str,v2:str):
    conn=conexao()
    cursor=conn.cursor()
    sql=f"Insert INTO box_pokemon(id,nome,habilidade1,habilidade2,habilidade3,tipo1,tipo2)VALUES(seq_box_pokemon.nextval,'{n}','{h1}','{h2}','{h3}','{v1}','{v2}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
def listar_box():
    conn=conexao();
    cursor=conn.cursor()
    sql="SELECT * FROM box_pokemon ORDER BY id ASC"
    cursor.execute(sql)
    for linha in cursor:
        for i in linha:
            print(i)
    cursor.close()
    conn.close()
def deletar_pkm(id:str):
    conn=conexao()
    cursor=conn.cursor()
    sql=f"DELETE FROM box_pokemon WHERE id={id}"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
def menu():
    print("""
        Bem vindo a sua box de pokemon!!
          É aqui onde você irá guardar os seus pokemons capturados
          Escolha a opção que deseja fazer na sua box:
          0-SAIR
          1-Adicionar Pokemon
          2-Excluir Pokemon
          3-Listar Pokemons
    """)
def inserir_pokemon():
    pokemon=input("Digite o nome do pokemon:")
    pkm=pokemon.lower()
    url=f'https://pokeapi.co/api/v2/pokemon/{pkm}'
    resposta=requests.get(url)
    info=resposta.json()
    if pkm not in pokemons:
        print("Pokemon não encontrado, tente novamente!!")
    else:
        hab=[]
        for h in info['abilities']:
            hab.append(h['ability']['name'])
        h1=hab[0]
        h2=hab[1]
        h3=hab[2] if len(hab)>2 else "None"
        tipo=[]
        for t in info['types']:
            tipo.append(t['type']['name'])
        t1=tipo[0]
        t2=tipo[1] if len(tipo)>1 else "None"
        inserir(pkm,h1,h2,h3,t1,t2)
        print(f"{pkm} agora esta na sua box")
"""
Para deixar mais claro, 
cada pokemon tem duas ou tres habilidades,caso digite um pokemon com tres habilidades(h1,h2,h3),sera registrado e mostrado tres habilidades,caso tenha só duas,a terceira variavel sera armazenada nula,o mesmo vale com os tipo,um pokeom pode ter um ou dois tipos(t1,t2),caso tenha dois tipos,sera armazenado os dois tipos,caso tenha apenas um,a variavel do segundo tipo sera armazenada como nula!
"""

while True:
    menu()
    opcao = input("Escolha a opção que deseja fazer na sua box: ")
    if opcao == "0":
        print("Saindo da sua box de pokemons...")
        break
    elif opcao == "1":
        inserir_pokemon()
    elif opcao=='2':
        while True:
            id=input("Fale o id do pokemon que deseja excluir: ")
            if not id.isnumeric():
                print("Id invalido, tente novamente!!")
            else:
                deletar_pkm(id)
                print("Pokemon excluido com sucesso")
                break
    elif opcao=='3':
        listar_box()




