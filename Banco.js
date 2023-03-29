let Banco = {
    conta: "12345",
    saldo: 1000,
    tipoConta: "Corrente",
    agencia: "001",
    
    buscarSaldo: function() {
      return this.saldo;
    },
    
    deposito: function(valor) {
      this.saldo += valor;
      return "Depósito realizado com sucesso. Novo saldo: R$" + this.saldo;
    },
    
    saque: function(valor) {
      if (valor > this.saldo) {
        return "Saldo insuficiente para realizar o saque.";
      } else {
        this.saldo -= valor;
        return "Saque realizado com sucesso. Novo saldo: R$" + this.saldo;
      }
    },
    
    numeroConta: function() {
      return this.conta;
    }
  };
  
  console.log(Banco.buscarSaldo());
  console.log(Banco.deposito(500));
  console.log(Banco.saque(200));
  console.log(Banco.numeroConta());
  