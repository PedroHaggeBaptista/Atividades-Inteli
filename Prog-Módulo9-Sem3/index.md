
# Relatório sobre Sistema de Conta Bancária e Testes Unitários em C#

## Introdução

Este relatório apresenta um sistema simples de conta bancária implementado na linguagem de programação C#, acompanhado de uma série de testes unitários. O propósito é ilustrar os conceitos fundamentais de programação orientada a objetos (POO), evidenciar a importância dos testes unitários no processo de desenvolvimento de software e demonstrar sua implementação em C#.

## Tecnologia e Ferramentas

- **C#**: Uma linguagem de programação moderna e orientada a objetos, desenvolvida pela Microsoft, que é parte integral do .NET Framework. É utilizada extensivamente para criar aplicações web, desktop e jogos.

## Conceitos Relacionados a Atividade

### Programação Orientada a Objetos (POO)

- **Classes e Objetos**: A classe `BankAccount` simboliza uma conta bancária, possuindo propriedades como `m_customerName` (nome do cliente) e `m_balance` (saldo). As instâncias desta classe representam contas bancárias individuais.
- **Encapsulamento**: Detalhes de implementação da conta bancária são encapsulados, com o saldo sendo acessível somente por meio dos métodos `Credit` e `Debit`, protegendo-o contra acessos e modificações indevidos.
- **Construtores**: Empregados para inicializar novas instâncias da classe `BankAccount`, estabelecendo o nome do cliente e o saldo inicial.

### Testes Unitários

- **Importância dos Testes Unitários**: Os testes unitários asseguram a execução do código conforme o esperado e facilitam a identificação de problemas no início do ciclo de desenvolvimento.
- **Framework NUnit**: Empregado para definir e executar testes unitários. A anotação `[Test]` sinaliza que o método subsequente é um teste unitário.
- **Asserts**: Afirmações que verificam se o comportamento do código atende ao esperado. Por exemplo, `Assert.AreEqual` confirma se dois valores são equivalentes. Por exemplo: `Assert.AreEqual(expected, actual, 0.001, "Account not debited correctly");`

## Sistema de Conta Bancária

A classe `BankAccount` fornece funcionalidades essenciais de uma conta bancária, permitindo operações de crédito e débito. Salvaguarda contra operações inválidas por meio de verificações, lançando exceções quando apropriado.

### Métodos Principais

- **Credit(double amount)**: Incrementa o saldo da conta com uma quantia, desde que esta seja positiva.
- **Debit(double amount)**: Reduz o saldo da conta por uma quantia, garantindo que o valor é menor que o saldo e não negativo.

## Testes Unitários Implementados

Foram elaborados três testes para validar o comportamento do método `Debit`:

1. **Debit_WithValidAmount_UpdatesBalance**: Confirma se, ao debitar uma quantia válida, o saldo é atualizado corretamente.
2. **Debit_WhenAmountIsLessThanZero_ShouldThrowArgumentOutOfRange**: Assegura que uma exceção é lançada ao tentar debitar um valor negativo.
3. **Debit_WhenAmountIsMoreThanBalance_ShouldThrowArgumentOutOfRange**: Garante que uma exceção é lançada ao debitar um valor superior ao saldo.

## Execução dos Testes
![Execução dos testes](https://imgur.com/EmPEUe7.png)
![Execução dos testes](https://imgur.com/kqdPquO.png)

## Conclusão

A implementação de um sistema de conta bancária simples em C#, juntamente com testes unitários utilizando NUnit, oferece um entendimento prático dos princípios de POO, como encapsulamento, e destaca a importância dos testes unitários no desenvolvimento de software. A adoção do framework NUnit facilita a criação, execução e manutenção de testes unitários, contribuindo para a qualidade e robustez do software desenvolvido.