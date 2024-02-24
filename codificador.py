def codificador_texto(texto, dicionario):
    texto_codificado = ''              
    for caractere in texto:                
        if caractere in dicionario:         
            texto_codificado += dicionario[caractere]  
        else:
            texto_codificado += caractere
    return texto_codificado


dicionario = {
    '1': '2',
    '2': '4',
    '3': '5',
    '4': '7',
    '5': '9',
    '6': '8',
    '7': '7',
    '8': '0',
    '9': '1',
    '0': '6',
     'A': '@#$0',  'a': '@#$',                   
    'B': '@###0', 'b': '@###',
    'C': '@##$0', 'c': '@##$',
    'D': '$##@0', 'd': '$##@',
    'E': '*@#$0', 'e': '*@#$',
    'F': '*@@!0', 'f': '*@@!',
    'G': '#$$#0', 'g': '#$$#',
    'H': '####0', 'h': '####',
    'I': '###@0', 'i': '###@',
    'J': '##@#0', 'j': '##@#',
    'K': '#@##0', 'k': '#@##',
    'L': '@@@#0', 'l': '@@@#',
    'M': '@@#@0', 'm': '@@#@',
    'N': '@#@@0', 'n': '@#@@',
    'O': '#@@@0', 'o': '#@@@',
    'P': '$$$$0', 'p': '$$$$',
    'Q': '$$$@0', 'q': '$$$@',
    'R': '$$@$0', 'r': '$$@$',
    'S': '$@$$0', 's': '$@$$',
    'T': '@$$$0', 't': '@$$$',
    'U': '!!!!0', 'u': '!!!!',
    'V': '!!!@0', 'v': '!!!@',
    'W': '!!@!0', 'w': '!!@!',
    'X': '!@!!0', 'x': '!@!!',
    'Y': '@!!!0', 'y': '@!!!',
    'Z': '**0',   'z': '**',
    ' ': ' ',                   
}




texto_que_vai_ser_escrito = input("Digite oque deseja Codificar: ")
texto_codificado = codificador_texto(texto_que_vai_ser_escrito, dicionario)

arq = open(r'','w') #Inserir caminho do arquivo
texto = texto_codificado
arq.write(texto)
arq.close()

print("Texto Codificado:",texto_codificado)