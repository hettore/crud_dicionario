import repositorio

#EXPERIMENTE A FUNÇÃO retornar_produtos(), que retornar um dicionário de dicionários com todos os produtos
print(repositorio.retornar_produtos())

#EXPERIMENTE A FUNÇÃO retornar_produto(id), que recebe um id e retorna um único dicionário contendo os detalhes do produto
print()
print(repositorio.retornar_produto(1))

#EXPERIMENTE A FUNÇÃO remover_produto(id), que recebe um id e remove um produto do dicionário de dicionários
repositorio.remover_produto(1)
print(repositorio.retornar_produtos())
print(repositorio.retornar_produto(1))

#EXPERIMENTE A FUNÇÃO alterar_produto(id, dados_produto), que recebe um id e um dicionário contendo dados do produto para então atualizar o produto no dicionário de dicionários
alterado = {
    'nome': 'Samsung Galaxy S23', 
    'descricao': 'Samsung Galaxy S21, modelo com 5G, na cor preta', 
    'preco': 5500.0, 
    'imagem': 'samsung.jpg'}

repositorio.atualizar_produto(2, alterado)
print(repositorio.retornar_produto(2))

#EXPERIMENTE A FUNÇÃO criar_produto(nome, descricao, preco, imagem), que recebe um nome, uma descricao, um preço e uma imagem e adiciona o produto no dicionário de dicionário com um novo id
repositorio.criar_produto(nome="Teste", descricao="testteeeee", preco=15, imagem="teste.jpg")
print()
print(repositorio.retornar_produtos())


#EXPERIMENTE A FUNÇÃO gerar_id(), que retornar um novo id à partir dos ids já cadastrados no dicionário de dicionários

print(repositorio.gerar_id())