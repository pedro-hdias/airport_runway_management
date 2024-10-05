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

### Estrutura de Branches

O fluxo de desenvolvimento deste projeto segue uma estrutura de branches bem definida, baseada em `Git Flow`, para garantir a organização e a estabilidade do código. Cada branch tem um propósito claro, e as versões são gerenciadas automaticamente por workflows do GitHub Actions.

#### 1. Branches de Desenvolvimento

Estas branches representam o trabalho em andamento e são criadas pelos desenvolvedores para novas funcionalidades, melhorias e correções de bugs. Elas são integradas na branch `develop` através de Pull Requests (PRs).

* **`fix/*`**: Branches criadas para correções de bugs e pequenos ajustes.
  * **Exemplo**: `fix/corrige-bug-auth`, `fix/ajuste-layout`
  * **Objetivo**: Quando mergeadas em `develop`, incrementam o `patch` na próxima release.

* **`update/*`**: Branches usadas para melhorias e pequenas adições de funcionalidades.
  * *Exemplo**: `update/melhoria-performance`, `update/refatoracao-codigo`
  * **Objetivo**: Quando mergeadas em `develop`, incrementam o `minor` na próxima release.

* **`feature/*`**: Branches usadas para grandes mudanças ou novas funcionalidades, que podem quebrar a compatibilidade com versões anteriores.
  * **Exemplo**: `feature/nova-funcionalidade-api`, `feature/integra-sistema-externo`
  * **Objetivo**: Quando mergeadas em `develop`, incrementam o `major` na próxima release.

#### 2. Branch Principal (Main)

A branch `main` representa a versão de produção do projeto. As versões estáveis e prontas para uso são sempre mergeadas para esta branch a partir das branches de `release`.

* **`main`**: Contém o código em produção, estável e versionado.
  * **Objetivo**: Receber o merge das branches de `release/*` com uma nova tag de versão.

#### 3. Branch de Integração (Develop)

A branch `develop` serve como uma versão de pré-release. Todas as mudanças das branches de desenvolvimento (`fix/*`, `update/*`, `feature/*`) são integradas aqui antes de serem preparadas para produção.

* **`develop`**: Recebe os PRs de todas as branches de desenvolvimento.
  * **Objetivo**: Acumular as mudanças que estão prontas para serem lançadas em uma nova versão.

#### 4. Branches de Release (Release)

As branches `release/*` são criadas a partir da `develop` quando uma nova versão está pronta para ser lançada. Elas permitem ajustes finais, como testes e documentação, antes da versão ser integrada à `main`.

* **`release/vX.X.X`**: Branches criadas a partir de `develop` para preparar uma nova versão.
  * **Objetivo**: Realizar os ajustes finais e preparar a versão para produção.
  * **Exemplo**: `release/v0.1.0`, `release/v1.0.0`

### Fluxo de Trabalho

O fluxo de trabalho é automatizado por **GitHub Actions**, com Pull Requests sendo criados automaticamente para garantir revisão e controle de qualidade antes de qualquer merge.

#### 1. Criação da Branch de Desenvolvimento

* O desenvolvedor cria uma branch seguindo um dos padrões:
  * `fix/*`: Para correções de bugs.
  * `update/*`: Para melhorias ou pequenas funcionalidades.
  * `feature/*`: Para grandes mudanças ou novas funcionalidades.

#### 2. Push na Branch de Desenvolvimento

* Ao fazer push para uma branch `fix/*`, `update/*`, ou `feature/*`, um workflow é acionado e cria automaticamente um Pull Request (PR) para a branch `develop`.

#### 3. Merge para `develop`

* O time revisa o PR, e, após aprovação, o merge é feito manualmente para a branch `develop`.

#### 4. Criação de Branch de Release

* O time revisa o PR, e, após aprovação, o merge é feito manualmente para a branch `release`.

#### 5. Merge para `main` e Criação de Tag

* Após a revisão e aprovação do PR da `release`, o merge é feito para a branch `main`.
* Uma nova tag de versão é criada automaticamente com base na branch `release`.

### Notas sobre Versionamento

O versionamento segue o [Versionamento Semântico (SemVer)](https://semver.org/):

* **`MAJOR`**: Aumentado quando há mudanças incompatíveis com versões anteriores (ex.: `feature/*` branches).
* **`MINOR`**: Aumentado quando há novas funcionalidades ou melhorias compatíveis com versões anteriores (ex.: `update/*` branches).
* **`PATCH`**: Aumentado quando há correções de bugs ou pequenos ajustes (ex.: `fix/*` branches).

### Overrides Manuais

Embora o workflow aplique automaticamente labels aos PRs com base no nome da branch, os desenvolvedores podem **sobrescrever** esse comportamento manualmente, aplicando um label ao PR (`patch`, `minor`, `major`) antes do merge, caso o impacto da mudança seja diferente do esperado.

O override manual é fortemente desencorajado, e deve ser usado apenas em casos excepcionais, já que o fluxo automatizado é parte fundamental do processo de versionamento e o override pode causar inconsistências. Faça isso apenas se tiver certeza do impacto da mudança e com a devida justificativa.

## Licença

Este projeto está licenciado sob a [GNU GENERAL PUBLIC LICENSE](LICENSE).

Para ver uma versão em português, acesse [o site oficial da licença](https://www.gnu.org/licenses/gpl-3.0.pt-br.html).

---

## Contato

Desenvolvido por [pedro-hdias](https://github.com/pedro-hdias). Para dúvidas ou sugestões, entre em contato pelo GitHub!

---