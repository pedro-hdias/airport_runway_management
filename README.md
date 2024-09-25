# Airport Runway Management System

## Descrição

Este projeto é um sistema simples de gerenciamento de pista de decolagem de aeroportos, que permite o controle de voos em uma fila de decolagem. O sistema é desenvolvido em Python e, atualmente, armazena a fila de decolagem em **memória** (sem uso de banco de dados).

O projeto faz parte de um aprendizado contínuo em desenvolvimento de software, e futuras versões irão expandir as funcionalidades, incluindo a integração com banco de dados e o gerenciamento da fila de pouso.

**Nota:** Esta versão inicial **trabalha apenas com a fila de decolagem armazenada em memória**. Futuras versões irão incluir mais funcionalidades.

## Funcionalidades

- Gerenciamento de fila de decolagem de voos.
- Registro e consulta de status de voos.

## Requisitos

- **Python** 3.8 ou superior

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/airport-runway-management.git
cd airport-runway-management
```

2. Instale as dependências Python necessárias usando o arquivo dentro de `app`:

*Sujiro que você use um ambiente virtual para isso. Para criá-lo, faça:

```bash
python -m venv .venv
```

```bash
pip install -r requirements.txt
```

## Uso

1. Após instalar todas as dependências, você pode iniciar o sistema rodando o seguinte comando:

```bash
python main.py
```

2. O sistema vai exibir um menu para você interagir, permitindo adicionar voos à fila de decolagem, visualizar o status dos voos, e outras operações.

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação.
- `models/`: Contém as definições de classes para voos e filas.
- `utils/`: Funções utilitárias e de validação.
- `views/`: Interface de interação com o usuário (CLI).
- `requirements.txt`: Lista de dependências Python do projeto.

## Contribuindo

Contribuições são sempre bem-vindas! Se você quiser contribuir com o projeto, siga os passos:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas mudanças (`git commit -m 'Add alguma feature'`).
4. Faça o push para a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request para a branch `develop`.

## Controle de Versão

Este projeto segue o padrão **Git Flow** para controle de versões. O fluxo padrão é:

- `feature*`: Branches onde novas funcionalidades são desenvolvidas.
- `develop`: Branch principal de integração.
- `release*`: Preparação de novas versões.
- `main`: Código de produção.

## Licença

Este projeto está licenciado sob a [                    GNU GENERAL PUBLIC LICENSE](LICENSE).

---

## Contato

Desenvolvido por [pedro-hdias](https://github.com/pedro-hdias). Para dúvidas ou sugestões, entre em contato pelo GitHub!
;