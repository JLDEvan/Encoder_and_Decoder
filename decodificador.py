def decodificador_texto(texto_codificado, dicionario_invertido):
    texto_decodificado = ''
    contador = 0
    while contador < len(texto_codificado):
        achou = False
        for chave_atual in dicionario_invertido:
            if texto_codificado[contador:contador+len(chave_atual)] == chave_atual:
                texto_decodificado += dicionario_invertido[chave_atual]
                contador += len(chave_atual)
                achou = True
        if not achou:
            texto_decodificado += texto_codificado[contador]
            contador += 1
    return texto_decodificado

dicionario_invertido = {
'2': '1',
'4': '2',
'5': '3',
'7': '4',
'9': '5',
'8': '6',
'3': '7',
'0': '8',
'1': '9',
'6': '0',
'@#$0': 'A', '@#$': 'a',
'@###0': 'B', '@###': 'b',              
'@##$0': 'C', '@##$': 'c',                     
'$##@0': 'D', '$##@': 'd',
'*@#$0': 'E', '*@#$': 'e',
'*@@!0': 'F', '*@@!': 'f',
'#$$#0': 'G', '#$$#': 'g',
'####0': 'H', '####': 'h',
'###@0': 'I', '###@': 'i',
'##@#0': 'J', '##@#': 'j',
'#@##0': 'K', '#@##': 'k',
'@@@#0': 'L', '@@@#': 'l',
'@@#@0': 'M', '@@#@': 'm',
'@#@@0': 'N', '@#@@': 'n',
'#@@@0': 'O', '#@@@': 'o',
'$$$$0': 'P', '$$$$': 'p',
'$$$@0': 'Q', '$$$@': 'q',
'$$@$0': 'R', '$$@$': 'r',
'$@$$0': 'S', '$@$$': 's',
'@$$$0': 'T', '@$$$': 't',
'!!!!0': 'U', '!!!!': 'u',
'!!!@0': 'V', '!!!@': 'v',
'!!@!0': 'W', '!!@!': 'w',
'!@!!0': 'X', '!@!!': 'x',
'@!!!0': 'Y', '@!!!': 'y',
'**0': 'Z', '**': 'z',
' ': ' '
         
}

arq = open(r'','r') #Inserir o caminho do arquivo

texto_codificado = (arq.read())
texto_decodificado = decodificador_texto(texto_codificado, dicionario_invertido)

print("Texto Decodificado:", texto_decodificado)


