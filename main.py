import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "source"))

from documento_email import criar_documento, enviar_email
from extracao import extrair_dados  

def main():
    # Extrai os dados
    print("Extraindo os dados...")
    dados_extraidos = extrair_dados()  
    print("Dados extraídos com sucesso!")

    # Gera o documento
    print("Criando o documento...")
    arquivo = criar_documento()  
    print(f"Documento '{arquivo}' criado com sucesso!")

    # Envia o e-mail
    print("Enviando o e-mail...")
    destinatario = "vieirakarol302@gmail.com"  
    enviar_email(destinatario, arquivo)
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()