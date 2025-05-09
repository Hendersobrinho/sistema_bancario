# Sistema Bancário - Atualização de Versão

## ✨ Sobre a Atualização

Esta versão do **Sistema Bancário** foi **ampliada** e **melhorada** com **novas funcionalidades** e uma **melhor organização** do código, visando **facilitar o uso** e **melhorar a manutenção**.

Agora o programa conta com:

- Cadastro de **Usuários**
- Cadastro de **Contas Bancárias**
- Sistema de **Login** e **Logout**
- Melhorias de **estrutura** usando **funções** e **classes**

---

## 🛠️ Principais Mudanças

### ✅ Novas Funcionalidades Implementadas
- **Cadastro de Usuário**  
  Permite criar um novo cliente, informando CPF, nome, data de nascimento e endereço.
  
- **Cadastro de Conta Bancária**  
  Usuários já cadastrados podem abrir uma conta associada ao seu CPF.
  
- **Login**  
  Usuários agora podem fazer login utilizando seu CPF, para operar suas contas de forma segura.

- **Logout**  
  O sistema permite que o usuário saia da sessão atual para proteger seus dados.

### 🔥 Melhorias Técnicas
- **Código Reestruturado em Classes**:  
  O programa agora utiliza duas classes principais: `Usuario` e `ContaBancaria`, organizando melhor os dados e comportamentos.
  
- **Funções Separadas**:  
  A lógica de operação como login, logout, saque, depósito e extrato foi separada em funções e métodos, tornando o código mais **modular** e **fácil de expandir**.
  
- **Validações de Dados**:  
  Foram adicionadas verificações para CPF válido, limite de saque diário e valor máximo por operação.

---

## 📋 Próximos Passos (Sugestões de Evolução)
- Implementar armazenamento em arquivos ou banco de dados.
- Melhorar controle de saques por dia com base em data/hora reais.
- Adicionar autenticação com senha.
- Desenvolver uma interface gráfica (GUI) para o sistema.

---

## 🚀 Como usar

1. Execute o programa em seu terminal.
2. Use o menu para navegar entre as opções: cadastrar usuário, abrir conta, login/logout, depósitos, saques e extrato.
3. Acompanhe suas operações de forma simples e segura!

---

## 📚 Tecnologias Utilizadas
- Linguagem: **Python 3**
- Biblioteca: **datetime** (nativa do Python).
