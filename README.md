# 💳 Análise Financeira Nubank | ETL | Power BI + DAX

Projeto de Business Intelligence focado em **análise comportamental de gastos**, combinando pipeline de dados moderno com geração de insights automáticos.

---

## 💭 O Problema

Faturas de cartão chegam todo mês e geram preocupações sobre o controle dos gastos
A maioria das pessoas sabe quanto gastou — mas não sabe **por que**,
**quando** e **em que padrão** os gastos acontecem.

Este projeto nasceu dessa necessidade real: transformar dados brutos
de fatura em inteligência financeira automatizada.

---

## 🎯 Objetivo

A maioria das análises financeiras responde:
> "Quanto foi gasto?"

Este projeto responde:
> **"Por que o gasto mudou e o que isso revela sobre o comportamento financeiro?"**

---

## 🏗️ Arquitetura de Dados (Medallion)

O pipeline de dados foi estruturado seguindo a arquitetura **Medallion**, garantindo qualidade, rastreabilidade e escalabilidade.

```
Fonte → Bronze → Silver → Gold → Power BI → Insights
```

### 🥉 Bronze (Raw)
- Dados brutos de transações financeiras
- Sem tratamento
- Fonte original preservada

### 🥈 Silver (Tratamento)
- Limpeza e padronização de dados
- Tratamento de datas e categorias
- Remoção de inconsistências

### 🥇 Gold (Analytics)
- Dados modelados para análise
- Criação de métricas e agregações
- Base pronta para consumo no Power BI

---

## 🧠 Principais Features

### 🔹 Top Drivers de Gasto
Identificação automática dos principais fatores que impactaram a variação mensal.

**Exemplo:**
> Supermercado (+R$469 | 52%), Delivery (+R$116 | 13%)

---

### 🔹 Insight Automático (Estilo Fintech)
Geração de explicações dinâmicas:
- "Seus gastos aumentaram principalmente por…"
- "Seus gastos diminuíram principalmente por…"

---

### 🔹 Análise de Frequência (Comportamento)
Classificação de gastos com base em recorrência:
- 🔁 Recorrente
- 📊 Frequente
- 🟡 Ocasional
- ⚪ Esporádico

---

### 🔹 Detecção de Padrões
Identificação automática de comportamento financeiro:
- ⚠️ Gasto recorrente em crescimento
- 📈 Gasto pontual em alta
- 🔁 Padrão estável

---

## ⚙️ Técnicas Utilizadas

- DAX avançado (`ADDCOLUMNS`, `TOPN`, `CONCATENATEX`)
- Tabelas virtuais e contexto de filtro
- Time Intelligence (Month over Month)
- Modelagem dimensional (tabela calendário)
- Arquitetura Medallion (Bronze, Silver, Gold)

---

## 💡 Insights Reais que os Dados Revelaram

**S3 e S4 concentram 88% dos gastos** — R$ 8,6 mil dos R$ 9,7 mil totais
> Seus maiores desembolsos acontecem consistentemente na segunda metade do mês

**Supermercado Guanabara representa 53% do total** — R$ 5,2 mil
> Um único estabelecimento domina mais da metade dos gastos

**MoM de +8,08%**
> Gastos crescendo mês a mês — sinal de atenção para o orçamento

**IOF de atraso e Juros de atraso detectados**
> Custo do crédito aparecendo — oportunidade imediata de economia

**Amazon Prime Canais — R$ 113,60/mês**
> Assinatura recorrente que pode estar passando despercebida

Contribuindo para: Consciência financeira • Identificação de padrões • Apoio à tomada de decisão

---

## 📊 Tecnologias

- Python — tratamento e orquestração dos dados
- Power BI — visualização e dashboards
- DAX — métricas e cálculos avançados
- Power Query + Linguagem M — ETL e transformação

---

## 🚀 Próximos Passos

- [ ] MVP com Streamlit — upload de fatura e dashboard automático
- [ ] API de insights financeiros
- [ ] Score comportamental do usuário
- [ ] Sistema de alertas inteligentes
- [ ] Chat com LLM para perguntas em linguagem natural

---

## 👀 Preview

*Dashboard — Página 1: Perfil Comportamental*

<img width="1152" height="648" alt="perfil-comportamental" src="https://github.com/user-attachments/assets/faf3bc66-df0b-4fbf-a725-bf7d861d406e" />

---

## 📌 Autor

**Hugo Alves da Costa**
Graduando em Física — UERJ | Analista de Dados

[LinkedIn](https://www.linkedin.com/in/hugo-costa22) • [GitHub](https://github.com/hugodevelopment)