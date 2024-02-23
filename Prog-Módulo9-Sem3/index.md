# Relatório sobre Sistema de Conta Bancária e Testes Unitários em C#

## Introdução

Este relatório descreve um sistema simples de conta bancária implementado na linguagem de programação C# e uma série de testes unitários associados, utilizando o framework de testes NUnit. O objetivo é demonstrar os conceitos básicos de programação orientada a objetos (POO), a importância dos testes unitários no desenvolvimento de software e como implementá-los em C#.

## Conceitos Aprendidos

### Programação Orientada a Objetos (POO)

- **Classes e Objetos**: A classe `BankAccount` representa uma conta bancária com propriedades como `m_customerName` (nome do cliente) e `m_balance` (saldo). Instâncias dessa classe representam contas bancárias individuais.
- **Encapsulamento**: Os detalhes de implementação da conta bancária são encapsulados. O saldo, por exemplo, é acessível apenas através dos métodos `Credit` e `Debit`, protegendo-o de acessos e modificações indevidas.
- **Construtores**: Utilizados para inicializar novas instâncias da classe `BankAccount`, configurando o nome do cliente e o saldo inicial.

### Testes Unitários

- **Importância dos Testes Unitários**: Os testes unitários garantem que o código execute conforme esperado e ajudam a identificar problemas precocemente no ciclo de desenvolvimento.
- **Framework NUnit**: Utilizado para definir e executar testes unitários. A anotação `[Test]` indica que o método subsequente é um teste unitário.
- **Asserts**: São afirmações que verificam se o comportamento do código está conforme o esperado. Por exemplo, `Assert.AreEqual` verifica se dois valores são iguais.

## Sistema de Conta Bancária

A classe `BankAccount` oferece funcionalidades básicas de uma conta bancária, permitindo operações de crédito e débito. Protege contra operações inválidas através de verificações, lançando exceções quando necessário.

### Métodos Principais

- **Credit(double amount)**: Adiciona uma quantia ao saldo da conta, desde que seja positiva.
- **Debit(double amount)**: Deduz uma quantia do saldo da conta, verificando se o valor é menor que o saldo e se não é negativo.

## Testes Unitários Implementados

Três testes foram criados para validar o comportamento do método `Debit`:

1. **Debit_WithValidAmount_UpdatesBalance**: Verifica se, ao debitar um valor válido, o saldo é atualizado corretamente.
2. **Debit_WhenAmountIsLessThanZero_ShouldThrowArgumentOutOfRange**: Garante que uma exceção é lançada ao tentar debitar um valor negativo.
3. **Debit_WhenAmountIsMoreThanBalance_ShouldThrowArgumentOutOfRange**: Assegura que uma exceção é lançada ao tentar debitar um valor maior que o saldo.

## Execução dos Testes
![Execução dos testes](https://imgur.com/EmPEUe7.png)
![Execução dos testes](https://imgur.com/kqdPquO.png)

## Conclusão

A implementação de um sistema de conta bancária simples e seus testes unitários associados em C# proporcionam um entendimento prático dos conceitos de POO, como encapsulamento, e a importância dos testes unitários no desenvolvimento de software. O uso do framework NUnit facilita a criação, execução e manutenção desses testes, contribuindo para a qualidade e robustez do software desenvolvido.