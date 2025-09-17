# 🌱 ESG App - Painel Interativo em Streamlit 

![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)

## 📌 Sobre o Projeto
Este projeto foi desenvolvido pela liga de investimento Wolf Finance para a **SEPEX (Semana de Extensão, Pesquisa e Ensino)**, com o objetivo de **apresentar de forma interativa o conceito de ESG (Environmental, Social and Governance)** e demonstrar como esses fatores podem influenciar o mercado financeiro.

O sistema permite ao usuário:
- 📈 **Montar uma carteira ESG personalizada** com até 6 ações.
- 💹 **Comparar a performance da carteira** com benchmarks.
- 🏭 **Explorar informações sobre empresas ESG** e entender porque são consideradas sustentáveis.
- 🌍 **Aprender o que é ESG** em uma página educativa, com resumo histórico e vídeo explicativo.

---

## 🖼️ Demonstração
<img width="1916" height="784" alt="image" src="https://github.com/user-attachments/assets/795fd97b-841f-439e-a7dd-4941261ceca1" />
<img width="1896" height="889" alt="image" src="https://github.com/user-attachments/assets/7c495845-3de0-4dfc-a4c6-71847bfe17b1" />
<img width="1878" height="897" alt="image" src="https://github.com/user-attachments/assets/877348cb-9390-4e13-8aae-f217d7025871" />
<img width="1900" height="677" alt="image" src="https://github.com/user-attachments/assets/9d2bad02-e918-4dd9-a730-3d0fd14d0160" />
<img width="1899" height="871" alt="image" src="https://github.com/user-attachments/assets/aaea5c30-cd2d-43fc-a08c-1dde34e4f991" />
<img width="1903" height="900" alt="image" src="https://github.com/user-attachments/assets/7fad4490-7341-4786-947b-7b52a3caf5ce" />


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
│   └── 3_ESG.py
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
<img width="350" height="350" alt="Logo_Tradicional_Completa" src="https://github.com/user-attachments/assets/aade90b3-1a32-40e9-ac80-10fd0d445d40" />

## 📜 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
