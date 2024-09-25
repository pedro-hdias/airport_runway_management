# Registro de alterações

Este arquivo precisa ter todas as alterações que você fez. Por favor, mantenha-o atualizado.

## v0.0.2 - 2024-09-25

### Novas Funcionalidades

- Automação de Workflows: Implementação de uma série de workflows no GitHub Actions para automatizar o processo de integração e versionamento.
  - Feature para Develop: Ao fazer o merge de uma branch feature-* para a branch develop, um PR automático é criado para revisar as alterações.
  - Develop para Release: Após o merge de PRs na branch develop, uma branch release-vX.X.X é criada automaticamente com base na tag mais recente. Um PR é aberto da branch develop para a nova branch de release.
  - Release para Main: Após o merge de PRs da branch release-* para main, um novo PR é criado automaticamente para fazer o merge da release na main.
  - Criação Automática de Tags: Após o merge de PRs da branch release para main, uma nova tag é criada automaticamente, incrementando a versão com base na última tag disponível.

### Funcionalidades da Aplicação

- Gerenciamento de Fila de Decolagem:
  - Adicionar avião à fila de decolagem: Permite que um novo avião seja adicionado à fila de decolagem, capturando as informações de voo e registrando o avião na fila.
  - Permitir a decolagem do próximo avião: Remove o primeiro avião da fila de decolagem e simula sua decolagem.
  - Mostrar o total de aviões na fila: Exibe o número de aviões aguardando na fila de decolagem.
  - Listar todos os aviões na fila: Mostra uma lista detalhada de todos os aviões aguardando para decolar.
  - Exibir detalhes do próximo avião a decolar: Mostra as características e detalhes do avião que está na frente da fila, pronto para decolar.
  - Buscar posição de um avião na fila: Permite buscar a posição de um avião específico na fila de decolagem com base no número do voo.
  - Remover avião específico da fila: Possibilita a remoção de um avião da fila de decolagem com base no número do voo, em caso de reordenação ou cancelamento.

### Melhorias

- Organização do Fluxo de Contribuições: Agora todos os PRs de contribuidores devem ser direcionados para a branch develop, com orientações claras no README para facilitar o processo.
- Geração Automática de Versionamento: Cada nova versão é automaticamente criada após o merge de uma release para main, garantindo rastreabilidade e consistência nas versões do projeto.

### Correções

- Correção no Workflow de Criação de PRs: Ajuste no fluxo de criação de PRs para garantir que a branch de release seja atualizada corretamente antes da criação de PRs para main.
- Correção na Criação de Tags: Correção para garantir que novas tags sejam criadas corretamente após o merge para main.
