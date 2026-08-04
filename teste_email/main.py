from drive import (
    autenticar,
    conectar_drive,
    listar_pdfs,
    baixar_arquivo,
    mover_arquivo
)

from sheets import (
    conectar_sheets,
    criar_planilha,
    escrever_dados
)

from extracao import extrair_dados_pdf

from config import (
    PASTA_PENDENTES,
    PASTA_OK,
    PASTA_DOWNLOADS,
    PASTA_ARQUIVO_PLANILHAS
)


def main():

    creds = autenticar()
    drive_service = conectar_drive(creds)
    sheets_service = conectar_sheets(creds)

    pdfs = listar_pdfs(
        drive_service,
        PASTA_PENDENTES
    )

    if not pdfs:
        print("Nenhum PDF encontrado.")
        return

    print(
        f"{len(pdfs)} PDF(s) encontrado(s)"
    )

    for pdf in pdfs:

        print(
            f"\nProcessando: {pdf['name']}"
        )

        # 1. Baixa o PDF da pasta de pendentes
        caminho = baixar_arquivo(
            drive_service,
            pdf["id"],
            pdf["name"],
            PASTA_DOWNLOADS
        )
        print(f"Baixado em: {caminho}")

        # 2. Extrai nome, CPF e telefone do PDF
        dados = extrair_dados_pdf(caminho)
        print(f"{len(dados)} registro(s) extraído(s) do PDF")

        if not dados:
            print("Nenhum dado encontrado nesse PDF, pulando para o próximo.")
            continue

        # 3. Cria uma planilha no Google Sheets e preenche com os dados
        titulo_planilha = f"Dados - {pdf['name'].rsplit('.', 1)[0]}"
        planilha_id = criar_planilha(sheets_service, titulo_planilha)
        escrever_dados(sheets_service, planilha_id, dados)
        print(
            f"Planilha criada: https://docs.google.com/spreadsheets/d/{planilha_id}"
        )

        # 4. Move o PDF original para a pasta de processados
        mover_arquivo(
            drive_service,
            pdf["id"],
            PASTA_OK
        )
        print("PDF movido para Documentos_OK")

        # 5. Arquiva a planilha preenchida em outra pasta do Drive
        mover_arquivo(
            drive_service,
            planilha_id,
            PASTA_ARQUIVO_PLANILHAS
        )
        print("Planilha arquivada na pasta de destino")


if __name__ == "__main__":
    main()
