import streamlit as st

st.set_page_config(page_title="Painel ESG", page_icon="🌱", layout="wide")

# ===== LOGO NO TOPO DA SIDEBAR =====
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

# ===== HOME CONTENT =====
st.title("🌱 Painel ESG - Central")
st.write("""
Bem-vindo ao **Painel Interativo de Ações ESG** 🎉  

Aqui você poderá:
- 📈 Montar sua **carteira ESG personalizada** e comparar com benchmarks (S&P500 e Ibovespa).  
- 📖 Explorar as **empresas ESG** e entender por que elas são relevantes.  
- 🌍 Aprender o que significa **ESG (Environmental, Social, Governance)** e seu impacto no mercado financeiro.  

Use o **menu lateral** para navegar entre as páginas.
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


