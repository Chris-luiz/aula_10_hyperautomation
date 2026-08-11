from googleapiclient.discovery import build


def conectar_sheets(creds):
    return build("sheets", "v4", credentials=creds)


def criar_planilha(service_sheets, titulo):
    """Cria uma planilha nova (fica na raiz do Drive) e devolve o ID dela."""

    corpo = {
        "properties": {"title": titulo}
    }

    planilha = service_sheets.spreadsheets().create(
        body=corpo,
        fields="spreadsheetId"
    ).execute()

    return planilha["spreadsheetId"]


def escrever_dados(service_sheets, planilha_id, dados, aba="Página1"):
    """
    Preenche a planilha com os dados extraídos do PDF.
    'dados' é uma lista de dicts, cada um com as chaves Nome, CPF e Telefone.
    """

    valores = [["Nome", "CPF", "Telefone"]]

    for registro in dados:
        valores.append([
            registro.get("Nome", ""),
            registro.get("CPF", ""),
            registro.get("Telefone", ""),
        ])

    corpo = {"values": valores}

    service_sheets.spreadsheets().values().update(
        spreadsheetId=planilha_id,
        range=f"{aba}!A1",
        valueInputOption="RAW",
        body=corpo
    ).execute()
