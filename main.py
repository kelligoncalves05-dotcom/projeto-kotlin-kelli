import uuid
usuarios = {}
def cadastrar():
    nome = input("Nome: ")
    email = input("E-mail: ").lower()
    for u in usuarios.values():
        if u['email'] == email:
            print("❌ E-mail já cadastrado!")
            return
    senha = input("Senha (min 6): ")
    if len(senha) < 6:
        print("❌ Senha curta!")
        return
    id_user = str(uuid.uuid4())[:8]
    usuarios[id_user] = {"nome": nome, "email": email, "senha": senha}
    print(f"✅ Cadastrado! ID: {id_user}")
def listar():
    for id_user, d in usuarios.items():
        print(f"ID: {id_user} | {d['nome']} - {d['email']}")
while True:
    print("\n1-Cadastrar 2-Listar 3-Sair")
    op = input("Op: ")
    if op == "1": cadastrar()
    elif op == "2": listar()
    elif op == "3": break