import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# ========= CONFIG =========
st.set_page_config(page_title="Carteira ESG", page_icon="🌱", layout="wide")

st.title("🌱 Carteira ESG")
st.write("""
    Monte sua carteira escolhendo **até 6 ações ESG** e veja gráficos e indicadores.

    **O que é ESG?**  
    ESG significa *Environmental, Social and Governance*.  
    São critérios usados para avaliar empresas em sustentabilidade, impacto social e boas práticas de governança.  
    """)

# ========= LISTA DE AÇÕES ESG =========
acoes_esg = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Tesla (TSLA)": "TSLA",
    "Nvidia (NVDA)": "NVDA",
    "Alphabet (GOOGL)": "GOOGL",
    "Amazon (AMZN)": "AMZN",
    "Meta (META)": "META",
    "Johnson & Johnson (JNJ)": "JNJ",
    "Procter & Gamble (PG)": "PG",
    "Coca-Cola (KO)": "KO",
    "PepsiCo (PEP)": "PEP",
    "Visa (V)": "V",
    "Mastercard (MA)": "MA",
    "Nike (NKE)": "NKE",
    "Unilever (UL)": "UL",
    "Nestlé (NESN.SW)": "NESN.SW",
    "Roche (ROG.SW)": "ROG.SW",
    "Novartis (NOVN.SW)": "NOVN.SW",
    "Siemens (SIE.DE)": "SIE.DE",
    "L'Oréal (OR.PA)": "OR.PA",
    "Natura (NTCO3.SA)": "NTCO3.SA",
    "Banco do Brasil (BBAS3.SA)": "BBAS3.SA",
    "Itaú Unibanco (ITUB4.SA)": "ITUB4.SA",
    "Ambev (ABEV3.SA)": "ABEV3.SA",
    "Vale (VALE3.SA)": "VALE3.SA",
    "Petrobras (PETR4.SA)": "PETR4.SA",
    "Magazine Luiza (MGLU3.SA)": "MGLU3.SA",
    "WEG (WEGE3.SA)": "WEGE3.SA",
    "Suzano (SUZB3.SA)": "SUZB3.SA",
    "BRF (BRFS3.SA)": "BRFS3.SA"
}

# ========= ESCOLHA DAS AÇÕES =========
selecionadas = st.multiselect(
    "Escolha até 6 ações ESG:",
    list(acoes_esg.keys()),
    max_selections=6
)

if selecionadas:
    tickers = [acoes_esg[a] for a in selecionadas]

    # ========= BAIXAR DADOS =========
    dados = yf.download(tickers, period="1y")["Close"]

    # ========= RENTABILIDADE NORMALIZADA =========
    dados_norm = dados / dados.iloc[0] * 100  # normalizado
    carteira_media = dados_norm.mean(axis=1)
    dados_norm["Carteira ESG"] = carteira_media

    # Benchmarks
    bench = yf.download(["^BVSP", "^GSPC"], period="1y")["Close"]
    bench_norm = bench / bench.iloc[0] * 100
    dados_norm["Ibovespa (^BVSP)"] = bench_norm["^BVSP"]
    dados_norm["S&P500 (^GSPC)"] = bench_norm["^GSPC"]

    # ========= GRÁFICO DE RENTABILIDADE =========
    st.subheader("📈 Rentabilidade Acumulada")
    fig_rent = px.line(dados_norm, x=dados_norm.index, y=dados_norm.columns,
                       title="Rentabilidade Acumulada da Carteira vs Benchmarks")
    st.plotly_chart(fig_rent, use_container_width=True)

    # ========= COMPOSIÇÃO DA CARTEIRA =========
    st.subheader("📊 Composição da Carteira (baseada no último preço)")
    ultimo_preco = dados.iloc[-1]
    carteira = pd.DataFrame({
        "Ação": selecionadas,
        "Ticker": tickers,
        "Preço Atual": ultimo_preco.values
    })

    fig_pizza = px.pie(carteira, names="Ação", values="Preço Atual",
                       title="Distribuição da Carteira (simulada)")
    st.plotly_chart(fig_pizza, use_container_width=True)

    # ========= MÉTRICAS =========
    st.subheader("📌 Indicadores das Empresas")
    colunas = st.columns(len(selecionadas))

    for i, acao in enumerate(selecionadas):
        ticker = acoes_esg[acao]
        info = yf.Ticker(ticker).info
        with colunas[i]:
            st.markdown(f"**{acao}**")
            st.metric("Preço Atual", f"${info.get('currentPrice', 0)}")
            st.metric("P/L", round(info.get("trailingPE", 0), 2) if info.get("trailingPE") else "N/A")
            st.metric("Valor Mercado", f"${round(info.get('marketCap', 0)/1e9, 2)} Bi")

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] li:first-child {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

import base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = get_base64_of_bin_file("assets/logo.png")
st.markdown(
    f"""
    <style>
        [data-testid="stSidebarNav"]::before {{
            content: "";
            display: block;
            margin: 0 auto 20px auto;
            background-image: url("data:image/png;base64,{logo_base64}");
            background-size: contain;
            background-repeat: no-repeat;
            height: 200px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)