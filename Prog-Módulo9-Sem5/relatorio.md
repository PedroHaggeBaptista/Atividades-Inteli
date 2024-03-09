# Documentação Cypress

## 1. O que é o Cypress e para que serve?

Cypress é uma ferramenta de teste de front-end de próxima geração, construída para a web moderna. Ela é utilizada para testar aplicações de maneira automatizada, realizando testes de integração, unidade e end-to-end diretamente no navegador. Isso resolve pontos críticos que desenvolvedores e engenheiros de QA enfrentam ao testar aplicações modernas, como problemas de sincronização e inconsistências de testes.

## 2. Vantagens e desvantagens do Cypress

### Vantagens:
- **Execução rápida e consistente**: Devido ao seu design arquitetônico, oferece uma execução de testes mais rápida e confiável.
- **Resistência a flutuações**: Cypress espera automaticamente por comandos e asserções, reduzindo problemas assíncronos.
- **Teste de casos de borda**: Permite simular respostas do servidor, facilitando a verificação de casos extremos.
- **Depurabilidade**: Tira snapshots durante a execução dos testes, permitindo análise detalhada em cada passo.
- **Integração com Dashboard**: Permite visualizar vídeos da execução dos testes através do Cypress Dashboard.

### Desvantagens:
- **Comunidade**: Menor em comparação ao Selenium, mas crescendo rapidamente.
- **Limitação de linguagem**: Cypress está limitado ao JavaScript.
- **Suporte a navegadores**: Não suporta múltiplas abas ou popups, e inicialmente era limitado ao Chrome e Electron, embora versões mais recentes já suportem mais navegadores.
- **Shadow DOM**: Falta suporte a Shadow DOM, uma funcionalidade importante para alguns desenvolvimentos web.
- **Apps nativos móveis**: Não possui suporte a testes de apps nativos móveis.

## 3. Arquitetura do Cypress

A arquitetura do Cypress é inovadora por operar diretamente dentro do navegador, diferentemente de ferramentas como Selenium que operam de fora. Isso permite que Cypress manipule o DOM e altere requisições e respostas de rede em tempo de execução, proporcionando controle total sobre a aplicação.

## 4. Seletores de elementos no Cypress

Cypress usa seletores do DOM para identificar elementos da página para interação e teste. Seletores como `cy.get()` e `cy.find()` são usados frequentemente para capturar elementos com base em seletores CSS ou texto de conteúdo.

## 5. Comandos e asserções no Cypress

Cypress fornece uma variedade de comandos para interagir com elementos, como `click()`, `type()`, `select()`, entre outros. As asserções são utilizadas para verificar se os elementos da página estão no estado esperado, usando comandos como `should()` e `expect()`.

## 6. Descrição das etapas de preparação, execução e verificação no Cypress

### Preparação:
- Configuração do ambiente e instalação do Cypress.
- Estruturação dos arquivos de teste.
- Criação de mocks e stubs para simular o comportamento do servidor.

### Execução:
- Inicialização dos testes através do Test Runner do Cypress.
- Execução dos comandos de teste no navegador.

### Verificação:
- Utilização de asserções para validar o estado da aplicação.
- Análise dos snapshots e vídeos para debugar falhas.

## 7. Como estruturar testes de forma eficiente no Cypress

- **Organize os testes em suites lógicas** usando `describe()` e `context()`.
- **Use `it()` para casos de teste individuais**, proporcionando descrições claras.
- **Aproveite os hooks** `before()`, `beforeEach()`, `after()` e `afterEach()` para configurar e limpar o estado antes e depois dos testes.
- **Evite dependências entre testes** para que possam ser executados isoladamente.
- **Mantenha os testes DRY (Don't Repeat Yourself)** reutilizando comandos e comportamentos através de funções personalizadas ou comandos customizados.
- **Use dados de teste variáveis** para cobrir múltiplos cenários.
- **Faça revisões de código dos testes** para garantir qualidade e legibilidade.
