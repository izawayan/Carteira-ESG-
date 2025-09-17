# 🌱 ESG App - Painel Interativo em Streamlit

![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)

## 📌 Sobre o Projeto
Este projeto foi desenvolvido para a **SEPEX (Semana de Extensão, Pesquisa e Ensino)**, com o objetivo de **apresentar de forma interativa o conceito de ESG (Environmental, Social and Governance)** e demonstrar como esses fatores podem influenciar o mercado financeiro.

O sistema permite ao usuário:
- 📈 **Montar uma carteira ESG personalizada** com até 6 ações.
- 💹 **Comparar a performance da carteira** com benchmarks como **S&P500** e **Ibovespa**.
- 🏭 **Explorar informações sobre empresas ESG** e entender porque são consideradas sustentáveis.
- 🌍 **Aprender o que é ESG** em uma página educativa, com resumo histórico e vídeo explicativo.

---

## 🖼️ Demonstração
*(adicione prints do app rodando, ex.: página da carteira, página "O que é ESG")*

---

## 🛠️ Tecnologias Utilizadas
- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [yFinance](https://pypi.org/project/yfinance/) → para buscar dados de mercado
- [Plotly](https://plotly.com/python/) → gráficos interativos
- [Pandas](https://pandas.pydata.org/) → manipulação de dados

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/esg_app.git
cd esg_app
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```
Ative o ambiente:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Rode o Streamlit
```bash
streamlit run app.py
```

O app ficará disponível em: **http://localhost:8501**

---

## 📂 Estrutura do Projeto
```
esg_app/
│── app.py                  # Página inicial (hub central)
│── requirements.txt        # Dependências
│── assets/                 # Logo e imagens
│── src/                    # Código modular (fetcher, charts, utils)
│── pages/                  # Páginas do app
│   ├── 1_Carteira_ESG.py
│   ├── 2_Sobre_Empresas.py
│   └── 3_O_que_e_ESG.py
```

---

## 🎯 Objetivo na SEPEX
Este projeto tem como **objetivo educativo e demonstrativo**:
- Mostrar de forma acessível o **conceito de ESG**.
- Demonstrar que é possível **combinar tecnologia (Python + Streamlit)** com **finanças sustentáveis**.
- Engajar o público com uma ferramenta **interativa e visual** durante a feira.

---

## 📽️ Vídeo Explicativo
Acesse o vídeo introdutório sobre ESG:  
👉 [O que é ESG (YouTube)](https://www.youtube.com/watch?v=JPdwEmghBUg)

---

## 📜 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
