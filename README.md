# 🔐 Crypto Wallet (Python)

Implementação de uma carteira de criptomoedas com foco em criptografia, assinatura digital e segurança de dados, incluindo sistema automatizado de backup.

## 🚀 Objetivo

Demonstrar na prática conceitos fundamentais de criptografia aplicados a carteiras digitais, incluindo geração de chaves, assinatura de transações e proteção de dados.

## 🛠️ Stack

* Python
* Criptografia assimétrica (chaves pública/privada)
* File system (armazenamento de backups)
* Scheduler para automação

## 🔑 Funcionalidades

### ✔️ Gestão de Carteira

* Geração de par de chaves (pública e privada)
* Criação de endereço de carteira

### ✔️ Assinatura Digital

* Assinatura de transações
* Verificação de autenticidade via chave pública

### ✔️ Backup Automatizado

* Criação automática de backups da carteira
* Retenção configurável (ex: 7 dias)
* Restauração de backups

### ✔️ Automação

* Scheduler para execução periódica de backups

### ✔️ Interface CLI

* Menu interativo no terminal
* Operações simples e diretas

---

## ▶️ Como executar

```bash
git clone https://github.com/schindlerfx/wallet_crypto.git
cd wallet-crypto
python main.py
```

---

## 🧪 Exemplo de uso

```
1. Criar transação
2. Verificar assinatura
3. Restaurar backup
4. Sair
```

---

## 🔒 Segurança

⚠️ Este projeto é educacional.

* A chave privada **não deve ser exposta**
* Não utilizar em ambiente real sem camadas adicionais de segurança
* Não integrado com blockchain real

---

## 📈 Possíveis melhorias

* Criptografia do armazenamento local
* Integração com blockchain real
* Interface gráfica
* API REST
* Suporte a múltiplas carteiras

---

## 📌 Diferencial

Projeto demonstra conhecimento prático em:

* Criptografia aplicada
* Assinatura digital
* Automação de processos
* Organização modular de código

---

Projeto desenvolvido para fins educacionais e exploração de segurança em aplicações financeiras.
