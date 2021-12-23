
import re

enderecoIp = [];

##Adicionando os enderecos IP na lista
while True:
    ipLista = str(input("Adicione um ip na lista:"));
    enderecoIp.append(ipLista);
    x = str(input("Digite '.' se deseja adicionar mais endereços: "));

    if x != '.':
        print("Encerrando aplicação");
        break;

print("Enderecos IPs digitados: ");
print(enderecoIp);

##Verificando se os enderecos sao validos ou nao##
enderecosValidos  : str;
enderecosValidos = [];
enderecosInvalidos : str;
enderecosInvalidos = [];

##Funcao regex para verificar a estrutura do ipv4, se e verdadeiro ou nao##
def verificarIp(ipTeste):

    flag = 0

    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
    match = re.match(pattern, ipTeste)
    if (match):
        field = ipTeste.split(".")
        for i in range(0, len(field)):
            if (int(field[i]) < 256):
                flag += 1
            else:
                flag = 0
    if (flag == 4):
        enderecosValidos.append(ipTeste);
    else:
        enderecosInvalidos.append(ipTeste);

##Percorrendo todos os itens da lista e atribuindo os validos e invalidos chamando a funcao##
for i in range(0, len(enderecoIp)):
    verificarIp(enderecoIp[i]); 


##Imprimindo os enderecos validos e invalidos, os ipv4 validos possuem 4 subdominios e por consequencia 3 pontos de separacao e vao de 0 ate 255 por familia##
print("Enderecos validos: ", enderecosValidos);
print("Enderecos invalidos: ", enderecosInvalidos);
