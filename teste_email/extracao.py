import pdfplumber


def extrair_dados_pdf(caminho_pdf):
    """
    Lê o PDF baixado e extrai a tabela com Nome, CPF e Telefone.
    Funciona com o modelo de PDF que tem uma tabela com essas colunas
    (aceita colunas extras, tipo o '#', sem problema).
    """

    dados = []

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            for tabela in pagina.extract_tables():
                if not tabela or len(tabela) < 2:
                    continue

                cabecalho = [(c or "").strip().lower() for c in tabela[0]]

                # só processa se a tabela realmente tiver essas colunas
                if not {"nome", "cpf"}.issubset(set(cabecalho)):
                    continue

                for linha in tabela[1:]:
                    registro = dict(zip(cabecalho, linha))
                    dados.append({
                        "Nome": (registro.get("nome") or "").strip(),
                        "CPF": (registro.get("cpf") or "").strip(),
                        "Telefone": (registro.get("telefone") or "").strip(),
                    })

    return dados


if __name__ == "__main__":
    import sys
    caminho = sys.argv[1] if len(sys.argv) > 1 else "downloads/dados_teste.pdf"
    for registro in extrair_dados_pdf(caminho):
        print(registro)
