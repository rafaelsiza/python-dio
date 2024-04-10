nome = "Rafael"
idade = 43
profissao = "Developer"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Rafae", "idade": 43}


print ("Nome: %s Idade %d" % (nome, idade))
print ("Nome: {} Idade: {}".format(nome, idade))
print ("Nome: {1} Idade: {0}".format(idade,nome ))
print ("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade,nome))

print ("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))
print ("Nome: {name} Idade: {age}".format(age=idade, name=nome))

print ("Nome: {nome} Idade: {idade}".format(**dados))

print (f'Nome: {nome} Idade: {idade} Saldo: {saldo:4.2f}' )

