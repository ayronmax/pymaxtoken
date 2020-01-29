from cryptography.fernet import Fernet, InvalidToken

class pymaxtoken(object):
    def __init__(self):
        pass

    def gerar_chave(self): # gera uma chave privada
        chave = Fernet.generate_key().decode("utf-8")

        with open("chave.txt", "w") as f:
            f.write(chave)
        
        return chave

    def cripto(self, chave=None, mensagem=None): # criptografa uma mensagem gerando um token
        return Fernet(chave.encode("utf-8")).encrypt(mensagem.encode("utf-8")).decode("utf-8")
    
    def decripto(self, chave=None, token=None, validade=None): # decriptografa um token / validade = número de segundos para uma mensagem ser válida
        return Fernet(chave.encode("utf-8")).decrypt(token.encode("utf-8"), validade).decode("utf-8")