from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

import pickle
import os
import io

# SCOPES = ["https://www.googleapis.com/auth/drive"]
SCOPES = ['https://www.googleapis.com/auth/drive']

def conectar_drive():

    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("drive", "v3", credentials=creds)


def listar_pdfs(service, pasta_id):

    resultado = service.files().list(
        q=f"'{pasta_id}' in parents",
        fields="files(id,name,mimeType)"
    ).execute()

    arquivos = resultado.get("files", [])

    return [
        arquivo
        for arquivo in arquivos
        if arquivo["mimeType"] == "application/pdf"
    ]


def baixar_arquivo(service, file_id, nome_arquivo, pasta_destino):

    os.makedirs(pasta_destino, exist_ok=True)

    caminho = os.path.join(
        pasta_destino,
        nome_arquivo
    )

    request = service.files().get_media(
        fileId=file_id
    )

    arquivo = io.BytesIO()

    downloader = MediaIoBaseDownload(
        arquivo,
        request
    )

    done = False

    while not done:
        status, done = downloader.next_chunk()

    with open(caminho, "wb") as f:
        f.write(arquivo.getvalue())

    return caminho


def mover_arquivo(service, file_id, pasta_destino):

    arquivo = service.files().get(
        fileId=file_id,
        fields="parents"
    ).execute()

    pasta_atual = ",".join(
        arquivo.get("parents")
    )

    service.files().update(
        fileId=file_id,
        addParents=pasta_destino,
        removeParents=pasta_atual,
        fields="id,parents"
    ).execute()