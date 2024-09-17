# Sistema Bancário com Python

Projeto desenvolvido no bootcamp da NTT DATA - Engenharia de Dados com Python pela [Digital Innovation One](https://www.dio.me/).<br><br>

## Desafio
Criar um sistema bancário com as operações: **depósito**, **saque**, **extrato**, **criar usuário (cliente)**, **criar conta**, **listar usuários** e **listar contas**.

**Depósito:**  
Deve ser possível depositar valores positivos para a conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

**Saque:**  
O sistema deve permitir realizar três saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

**Extrato:**  
Essa operação deve listar, junto com as datas e horas, todos os depósitos e saques realizados na conta. Ao final da listagem, deve ser exibido o saldo atual da conta.

Restrições adicionais:
- Estabelecer um limite de 10 transações diárias.
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.

**Criar Usuário (Cliente):**  
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço deve ser uma string e no CPF deve ser armazenado somente os números. Não poderá cadastrar dois usuários com o mesmo CPF.

**Criar Conta Corrente:**  
O programa deve armazenar as contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.<br><br>


### Ferramentas utilizadas:
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" width="4%">  <img src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png" width="4%">