from drive import (
    conectar_drive,
    listar_pdfs,
    baixar_arquivo,
    mover_arquivo
)

from config import (
    PASTA_PENDENTES,
    PASTA_OK,
    PASTA_DOWNLOADS  # Corrigido o nome da variável
)


def main():

    service = conectar_drive()

    pdfs = listar_pdfs(
        service,
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

        caminho = baixar_arquivo(
            service,
            pdf["id"],
            pdf["name"],
            PASTA_DOWNLOADS  # Corrigido o nome da variável
        )

        print(
            f"Baixado em: {caminho}"
        )

        # Aqui entra a lógica da atividade
        # extrair_dados(caminho)

        mover_arquivo(
            service,
            pdf["id"],
            PASTA_OK
        )

        print(
            "Movido para Documentos_OK"
        )


if __name__ == "__main__":
    main()