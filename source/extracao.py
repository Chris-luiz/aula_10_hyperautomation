from pathlib import Path
from playwright.sync_api import sync_playwright

def extrair_dados():
    with sync_playwright() as p:
        navigator = p.chromium.launch(headless=False)
        page = navigator.new_page()

        file = Path("portal_fake/index.html").resolve()

        page.goto(f"file://{file}")
        page.click('#btnNovo')

        page.wait_for_timeout(1000)

        dados = {
            "Nome":         page.locator("#f_nome").input_value(),
            "Sobrenome":    page.locator("#f_sobrenome").input_value(),
            "CPF":          page.locator("#f_cpf").input_value(),
            "E-mail":       page.locator("#f_email").input_value(),
            "Telefone":     page.locator("#f_telefone").input_value(),
            "Nascimento":   page.locator("#f_nascimento").input_value(),
            "Endereço":     page.locator("#f_endereco").input_value(),
        }

        print("Dados Extraídos: ")

        for campo, valor in dados.items():
            print(f"{campo}: {valor}")

        navigator.close()

if __name__ == '__main__':
    extrair_dados()