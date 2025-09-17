import streamlit as st

st.set_page_config(page_title="O que é ESG", page_icon="🌍")

st.title("🌍 O que é ESG?")

st.markdown("""
**ESG** significa **Ambiental, Social e Governança** (*Environmental, Social and Governance*).  
É um conjunto de critérios usados para avaliar empresas quanto ao seu impacto **ambiental**, sua atuação **social** e suas práticas de **governança corporativa**.  

Esse conceito cresceu nas últimas décadas e hoje influencia bilhões de dólares em investimentos no mundo todo.
""")

# Inserindo vídeo explicativo
st.subheader("🎥 Vídeo Explicativo")
st.video("https://www.youtube.com/watch?v=JPdwEmghBUg")

# =====================
st.header("📖 Origem e História")
st.markdown("""
O termo ESG ganhou destaque em **2004** no relatório *“Who Cares Wins”*, apoiado pela ONU.  
Ele consolidou a ideia de que empresas que cuidam do meio ambiente, da sociedade e da governança tendem a ser mais sustentáveis e lucrativas no longo prazo.  

Na história, exemplos como o desinvestimento contra o apartheid na África do Sul (anos 1970–80) mostraram como escolhas éticas podem moldar mercados.  
""")

# =====================
st.header("💡 Por que o ESG é importante?")
st.markdown("""
- 🌱 **Ambiental**: combate às mudanças climáticas, energia renovável, redução de poluentes.  
- 🤝 **Social**: diversidade, inclusão, respeito aos direitos humanos e condições de trabalho.  
- 🏛️ **Governança**: transparência, ética nos negócios e boas práticas administrativas.  

Investidores e consumidores têm dado cada vez mais peso a esses fatores.  
Hoje, **mais de US$ 30 trilhões** em ativos globais são geridos com critérios ESG.
""")

# =====================
st.header("⚖️ Críticas e Desafios")
st.markdown("""
Apesar da popularidade, o ESG também recebe **críticas**:  
- **Falta de padronização** nos indicadores.  
- **Greenwashing** (empresas exagerando práticas sustentáveis para marketing).  
- **Diferenças regionais**: Europa lidera, enquanto outros mercados ainda resistem.  
- Debate sobre se o ESG seria uma forma indireta de **regulação privada** feita por grandes gestoras.  
""")

# =====================
st.header("📊 ESG Hoje")
st.markdown("""
- O mercado de fundos ESG movimenta **mais de US$ 18 trilhões** (2021).  
- A Europa concentra **84%** desses ativos, sendo o maior mercado do mundo.  
- Novas gerações (Millennials e Gen Z) têm maior tendência a escolher investimentos sustentáveis.  
- Empresas de diversos setores estão se adaptando para não ficarem de fora dessa onda.  
""")

# =====================
st.header("✅ Conclusão")
st.markdown("""
O ESG não é apenas uma tendência de moda ou filantropia:  
é uma **abordagem prática para alinhar negócios com sustentabilidade, ética e responsabilidade social**.  

Seja para **investidores**, **empresas** ou **sociedade**, o ESG molda o futuro do mercado financeiro e do planeta.
""")



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