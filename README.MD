README.md com as informações abaixo. 

# HyperAutomation - Portal Fake Soluções Digitais

## Descrição
Projeto desenvolvido para demonstrar técnicas de Hyperautomation por meio
da automação do processo de cadastro de clientes da empresa fictícia Portal
Fake Soluções Digitais. A solução integra automação Web, geração
automática de documentos, envio automatizado de e-mails e controle de
versão utilizando Git, GitHub e GitFlow. 

## Funcionalidades
- Extração automática dos dados do formulário de cadastro utilizando
Playwright;
- Geração automática da ficha de cadastro em formato Word (.docx);
- Envio automático da ficha de cadastro por e-mail utilizando SMTP Gmail;
- Proteção das credenciais por meio do arquivo .env;
- Versionamento do projeto utilizando Git, GitHub e GitFlow. 

## Tecnologias Utilizadas
- Python 3.14
- Playwright
- python-docx
- python-dotenv
- smtplib
- Git
- GitHub
- GitFlow

## Estrutura do Projeto
```text
HyperAutomation/
│
├── source/
│   ├── extracao.py
│   └── documento_email.py
│
├── resources/
│
├── Ficha_Cadastro_Portal_Fake.docx
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Segurança
As credenciais utilizadas para o envio de e-mails são armazenadas no
arquivo .env, utilizando as variáveis:
- EMAIL_REMETENTE
- EMAIL_SENHA

O arquivo .env está listado no .gitignore, impedindo que informações sensíveis
sejam enviadas ao repositório GitHub. 

## Controle de Versão
O projeto foi desenvolvido utilizando o fluxo GitFlow, com as seguintes
branches:
- main – versão oficial do projeto;
- develop – integração das funcionalidades;
- feature/extracao – desenvolvimento da extração de dados;
- feature/documento-email – desenvolvimento da geração de documentos
e envio de e-mails;
- release/1.0 – preparação da versão final do projeto. 

## Fluxo GitFlow

1. Criação do repositório Git;
2. Desenvolvimento das funcionalidades em branches feature;
3. Merge das funcionalidades para a branch develop;
4. Criação da branch release/1.0;
5. Realização dos testes finais;
6. Merge da release para a main;
7. Criação da tag v1.0;
8. Publicação do projeto no GitHub. 

## Versão
### Versão atual: v1.0

Primeira versão funcional da automação desenvolvida para o processo de
cadastro da empresa fictícia Portal Fake Soluções Digitais.

## Autor
Nome do aluno: Christian Luiz de Souza Paes 

Turma: AxAcademy 

Disciplina: Hyperautomation

Professor: Moisés Levy