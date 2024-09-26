# Airport Runway Management System

## Descrição

Este projeto é um sistema simples de gerenciamento de pista de decolagem de aeroportos, que permite o controle de voos em uma fila de decolagem. O sistema é desenvolvido em Python e, atualmente, armazena a fila de decolagem em **memória** (sem uso de banco de dados).

O projeto faz parte de um aprendizado contínuo em desenvolvimento de software, e futuras versões irão expandir as funcionalidades, incluindo a integração com banco de dados e o gerenciamento da fila de pouso.

* **Nota:** Esta versão inicial **trabalha apenas com a fila de decolagem armazenada em memória**. Futuras versões irão incluir mais funcionalidades.

## Funcionalidades

* Gerenciamento de fila de decolagem de voos.
* Registro e consulta de status de voos.

## Requisitos

* **Python** 3.8 ou superior

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/airport-runway-management.git
cd airport-runway-management
```

2. Instale as dependências Python necessárias usando o arquivo dentro de `app`:

* Sujiro que você use um ambiente virtual para isso. Para criá-lo, faça:

```bash
python -m venv .venv
start .venv\scripts\activate
```

```bash
pip install -r apprequirements.txt
```

## Uso

1. Após instalar todas as dependências, você pode iniciar o sistema rodando o seguinte comando:

```bash
python app\src\main.py
```

* O sistema vai exibir um menu para você interagir, permitindo adicionar voos à fila de decolagem, visualizar o status dos voos, e outras operações.

## Estrutura do Projeto

* `.github`: Configurações de workflows do GitHub Actions.
* `.github/workflows`: Workflows de integração contínua.
* `app/`: Pasta base do Código-fonte da aplicação.
* `app/src/`: Código-fonte da aplicação.
* `app/src/controllers/`: Controladores da aplicação.
* `app/src/models/`: Modelos de dados da aplicação.
* `app/src/utils/`: Utilitários da aplicação.
* `app/src/views/`: Interfaces de usuário da aplicação.
* `app/src/main.py`: Ponto de entrada da aplicação.
* `app/tests/`: Testes unitários da aplicação.
* `apprequirements.txt`: Arquivo de dependências Python.
* `.gitignore`: Arquivo de configuração do Git para ignorar arquivos específicos.
* `changelog.md`: Registro de alterações do projeto.
* `LICENSE`: Licença do projeto.
* `README.md`: Documentação do projeto.

## Como Contribuir

1. **Replique o projeto**: Faça o *fork* do projeto.
2. **Crie uma branch de feature**: Ao iniciar uma nova feature ou correção de bug, crie uma branch com o prefixo `feature-*`, onde `*` representa o nome da sua feature.

Exemplo:

`git checkout -b feature-minha-nova-feature`

Onde    `minha-nova-feature` é o nome da sua nova feature.

3. **Seguir o workflow**: Siga todo o workflow do repositório até sua main;

4. **Submeter modificações**: Realize a solicitação pull da sua branch main para a branch develop do repositório.

## Controle de Versão

Este projeto segue o padrão **Git Flow** para controle de versões. O fluxo padrão é:

* `feature*`: Branches onde novas funcionalidades são desenvolvidas.
* `develop`: Branch principal de integração.
* `release*`: Preparação de novas versões.
* `main`: Código de produção.

## Workflows Automatizados

Este repositório utiliza uma série de workflows do GitHub Actions para automatizar os processos de integração e versionamento.

### 1. Feature para Develop

Quando um pull request de uma branch `feature-*` para a branch `develop` é mergeado, um PR é automaticamente criado da `feature` para `develop`. Isso garante que as alterações sejam revisadas e integradas de forma controlada.

### 2. Develop para Release

Após o merge de um pull request na branch `develop`, é criada automaticamente uma branch `release-vX.X.X` com base na tag mais recente. Um pull request é aberto da `develop` para a branch de release, permitindo que as alterações sejam preparadas para a próxima versão.

### 3. Release para Main

Quando um pull request na branch de release (`release-*`) é mergeado, um novo pull request é criado automaticamente da branch `release` para `main`, preparando a versão final para produção.

### 4. Criação de Tag após Merge na Main

Após o merge de um pull request da branch `release` para `main`, uma nova tag é criada automaticamente, incrementando a versão com base na tag anterior. Isso garante que cada release em `main` tenha uma versão única e rastreável.

## Licença

Este projeto está licenciado sob a [GNU GENERAL PUBLIC LICENSE](LICENSE).

Para ver uma versão em português, acesse [o site oficial da licença](https://www.gnu.org/licenses/gpl-3.0.pt-br.html).

---

## Contato

Desenvolvido por [pedro-hdias](https://github.com/pedro-hdias). Para dúvidas ou sugestões, entre em contato pelo GitHub!
