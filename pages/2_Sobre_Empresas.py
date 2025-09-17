import streamlit as st
import yfinance as yf

st.title("📖 Sobre as Empresas ESG")

st.write("Aqui você encontra uma breve descrição sobre a empresa selecionada e sua relevância em ESG.")

# Lista resumida de razões ESG (personalizar conforme sua pesquisa)
esg_reasons = {
    "Apple (AAPL)": "Investimentos em energia limpa e cadeia de suprimentos sustentável.",
    "Microsoft (MSFT)": "Meta de zerar emissões até 2030 e foco em inclusão digital.",
    "Tesla (TSLA)": "Veículos elétricos e soluções de energia renovável.",
    "Nvidia (NVDA)": "Eficiência energética em GPUs e suporte a tecnologias de IA aplicadas à sustentabilidade.",
    "Alphabet (GOOGL)": "Uso intensivo de energias renováveis em data centers e iniciativas de inclusão digital.",
    "Amazon (AMZN)": "Programa Climate Pledge com meta de carbono zero até 2040.",
    "Meta (META)": "Investimentos em energias renováveis e políticas de inclusão em sua força de trabalho.",
    "Johnson & Johnson (JNJ)": "Foco em saúde pública global e práticas éticas na cadeia de suprimentos.",
    "Procter & Gamble (PG)": "Uso de embalagens recicláveis e metas de redução de emissões.",
    "Coca-Cola (KO)": "Projetos de economia circular e redução do consumo de água.",
    "PepsiCo (PEP)": "Planos para agricultura sustentável e neutralidade de carbono até 2040.",
    "Visa (V)": "Operações globais movidas por energia 100% renovável desde 2020.",
    "Mastercard (MA)": "Parcerias em inclusão financeira e neutralidade de carbono.",
    "Nike (NKE)": "Iniciativas de economia circular e uso de materiais reciclados.",
    "Unilever (UL)": "Produtos de consumo com foco em redução de plástico e responsabilidade social.",
    "Nestlé (NESN.SW)": "Compromisso com agricultura sustentável e embalagens 100% recicláveis.",
    "Roche (ROG.SW)": "Investimentos em pesquisa de saúde sustentável e acessível.",
    "Novartis (NOVN.SW)": "Projetos para acesso a medicamentos em países em desenvolvimento.",
    "Siemens (SIE.DE)": "Líder em soluções industriais para energia limpa e cidades inteligentes.",
    "L'Oréal (OR.PA)": "Programas de diversidade e embalagens com menor impacto ambiental.",
    "Natura (NTCO3.SA)": "Reconhecida globalmente em sustentabilidade e impacto social.",
    "Banco do Brasil (BBAS3.SA)": "Crédito rural sustentável e programas de inclusão financeira.",
    "Itaú Unibanco (ITUB4.SA)": "Investimentos em energia limpa e incentivo a práticas ESG no mercado financeiro.",
    "Ambev (ABEV3.SA)": "Uso de energia renovável e programas de eficiência hídrica.",
    "Vale (VALE3.SA)": "Metas de descarbonização e recuperação ambiental após desastres.",
    "Petrobras (PETR4.SA)": "Investimentos crescentes em biocombustíveis e energia renovável.",
    "Magazine Luiza (MGLU3.SA)": "Programas de diversidade e inclusão no varejo brasileiro.",
    "WEG (WEGE3.SA)": "Produção de motores elétricos eficientes e soluções em energia renovável.",
    "Suzano (SUZB3.SA)": "Líder em papel e celulose sustentável, com foco em reflorestamento.",
    "BRF (BRFS3.SA)": "Práticas de bem-estar animal e eficiência energética na produção de alimentos."
}


acao = st.selectbox("Escolha uma empresa para saber mais:", list(esg_reasons.keys()))

if acao:
    ticker = acao.split("(")[-1].replace(")", "")
    info = yf.Ticker(ticker).info
    st.subheader(acao)
    st.write(f"**O que a empresa faz:** {info.get('longBusinessSummary', 'Resumo não disponível.')}")
    st.write(f"**Por que é considerada ESG:** {esg_reasons.get(acao, 'Não disponível, pesquise mais para enriquecer!')}")

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