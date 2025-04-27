# Análise Exploratória de Dados (EDA) - Meios de Pagamento (Banco Central do Brasil)

## Sobre o Projeto

Este projeto realiza uma análise exploratória (EDA) das informações sobre meios de pagamento disponibilizados pelo Banco Central do Brasil, armazenadas em um banco de dados SQLite gerado por um processo de ETL.

O foco da análise foi:
- Calcular as médias das variáveis numéricas presentes no conjunto de dados.
- Interpretar os resultados, com destaque especial para a comparação entre diferentes meios de pagamento, excluindo o Pix.

## Objetivo

- Compreender o comportamento médio das transações financeiras por diferentes instrumentos de pagamento no Brasil.
- Identificar padrões de uso e tendências de migração entre os meios tradicionais (DOC, cheque) e os mais modernos (cartão, TED, boleto).

## Como executar

1. Instale as dependências:
   ```bash
   pip install pandas
