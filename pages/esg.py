import streamlit as st
import networkx as nx
import random
from tqdm import tqdm
import pandas as pd
import os
import base64

# ========= CONFIGURAÇÕES INICIAIS E ESTILIZAÇÃO =========
# Configuração de página
st.set_page_config(page_title="Simulador de Carteiras", page_icon="📈", layout="wide")

# CSS personalizado
st.markdown(
    """
    <style>
    /* Fundo da página */
    .stApp {
        background-color: #d1d1d1;
    }

    /* Botões */
    div.stButton > button {
        background-color: #01c1ca;
        color: white;
        height: 3em;
        width: 8em;
        border-radius: 10px;
        border: none;
    }

    /* Títulos */
    h1, h2 {
        color: #01c1ca;
    }
    </style>
    """, unsafe_allow_html=True
)

# Funções para estilização da barra lateral
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

def get_base64_of_bin_file(bin_file):
    if not os.path.exists(bin_file):
        return ""
    with open(bin_file, 'rb') as f:
            data = f.read()
    return base64.b64encode(data).decode()

# Tente carregar o logo. Se não existir, a estilização não será aplicada
try:
    logo_base64 = get_base64_of_bin_file("assets/logo.png")
    if logo_base64:
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
except:
    pass

# DEFINE_SEED = 3
# random.seed(DEFINE_SEED) 

# ==============================
# Integração com o CSV
# ==============================

def carregar_dados_do_csv(nome_arquivo):
    """
    Carrega os dados de Tickers e o Índice Combinado de um arquivo CSV,
    retornando um dicionário com a estrutura esperada pelo programa.
    """
    if not os.path.exists(nome_arquivo):
        st.error(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

    try:
        df = pd.read_csv(nome_arquivo, sep=';', decimal=',')
        df['Indice Combinado'] = pd.to_numeric(df['Indice Combinado'], errors='coerce')
        df.dropna(subset=['Indice Combinado'], inplace=True)
        
        # Converte o DataFrame para o formato de dicionário esperado
        dados_formatados = {
            row['Ticker']: {"indice_combinado": row['Indice Combinado']}
            for index, row in df.iterrows()
        }
        return dados_formatados
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar o arquivo: {e}")
        return None

# Carrega os dados do arquivo no início do script
nome_do_arquivo = 'indice_combinado.csv'
acoes_carregadas = carregar_dados_do_csv(nome_do_arquivo)

if acoes_carregadas is None or not acoes_carregadas:
    st.stop() # Interrompe a execução se os dados não puderem ser carregados

# ==============================
# Funções do programa
# ==============================
def calcular_indice_combinado_carteira(carteira, G):
    """
    Calcula o Índice Combinado ponderado da carteira, usando os dados do grafo (G).
    """
    total_indice = 0
    for acao, porcentagem in carteira.items():
        if acao in G.nodes:
            total_indice += (porcentagem / 100) * G.nodes[acao]['indice_combinado']
    return total_indice

def gerar_carteira(acoes, restricoes_minimas):
    """
    Gera uma carteira aleatória, respeitando as restrições mínimas
    e garantindo que a soma dos pesos seja 100%.
    """
    carteira = {acao: 0 for acao in acoes}
    total_atual = sum(restricoes_minimas.values())

    # 1. Aplica as restrições mínimas
    for acao, min_val in restricoes_minimas.items():
        carteira[acao] = min_val

    restante = 100 - total_atual
    
    # Lista de ações que podem receber o peso restante
    acoes_restantes = [acao for acao in acoes]

    # 2. Distribui o peso restante de forma aleatória em blocos de até 5%
    while restante > 0 and acoes_restantes:
        for acao in acoes_restantes[:]:
            if restante <= 0:
                break
            
            # Incremento aleatório (entre 0 e 5, ou o que restar)
            incremento = random.randint(0, min(5, restante))
            carteira[acao] += incremento
            restante -= incremento
            
            # (Lógica original): Remove a ação se ela atingir um limite
            if carteira[acao] >= 100 - len(acoes_restantes) * 5 and acao in acoes_restantes:
                acoes_restantes.remove(acao)

    # 3. Ajuste final para garantir 100% (corrige possíveis erros de arredondamento)
    diferenca = 100 - sum(carteira.values())
    if diferenca != 0 and carteira:
        primeira_acao = list(carteira.keys())[0]
        carteira[primeira_acao] += diferenca

    return carteira

def obter_melhores_carteiras(acoes, restricoes_minimas, num_tentativas=100000):
    """
    Roda a simulação de força bruta e retorna as 5 carteiras com maior Índice Combinado.
    """
    resultados = []
    
    # Cria o grafo
    G = nx.Graph()
    for acao, dados in acoes.items():
        G.add_node(acao, indice_combinado=dados['indice_combinado'])

    # Loop de simulação
    for _ in tqdm(range(num_tentativas), desc="Gerando carteiras"):
        carteira = gerar_carteira(acoes, restricoes_minimas)
        indice_combinado = calcular_indice_combinado_carteira(carteira, G)
        resultados.append((carteira, indice_combinado))

    # Ordena todos os resultados pelo Índice Combinado (do maior para o menor)
    resultados.sort(key=lambda x: x[1], reverse=True)
    
    # RETORNA APENAS AS 5 MELHORES
    return resultados[:5]

# ==============================
# Streamlit Interface
# ==============================
st.title("Simulador de Carteiras por Índice Combinado")
st.write("Selecione as ações que deseja analisar e defina restrições mínimas de participação.")

# Seleção de ações
tickers_selecionados = st.multiselect(
    "Escolha os tickers:",
    options=list(acoes_carregadas.keys()),
    default=[] # Alterado para não haver pré-seleção
)

# Restrições mínimas
restricoes_minimas = {}
soma_minima = 0
if tickers_selecionados:
    st.write("Defina as porcentagens mínimas para cada ticker (opcional)")
    sliders = {}
    for ticker in tickers_selecionados:
        # Pega o valor do índice combinado para o valor padrão do slider
        valor_padrao = int(acoes_carregadas[ticker]['indice_combinado']) if ticker in acoes_carregadas else 0
        sliders[ticker] = st.slider(f"{ticker} (%)", 0, 100, 0)
    
    soma_minima = sum(sliders.values())
    st.info(f"Soma das porcentagens mínimas: {soma_minima}%")
    
    if soma_minima > 100:
        st.error("A soma das porcentagens mínimas não pode ser maior que 100%.")
    else:
        restricoes_minimas = sliders

# Botão para gerar carteiras
if st.button("Gerar melhores carteiras"):
    if not tickers_selecionados:
        st.warning("Selecione pelo menos um ticker.")
    elif soma_minima > 100:
        st.error("Corrija as porcentagens mínimas antes de continuar.")
    else:
        # Filtra os dados carregados do CSV com base nos tickers selecionados
        acoes = {ticker: acoes_carregadas[ticker] for ticker in tickers_selecionados}
        
        st.write("Gerando carteiras, aguarde...")

        # Definir tamanho da simulação
        melhores = obter_melhores_carteiras(acoes, restricoes_minimas, num_tentativas=100000)

        st.success("Carteiras geradas!")
        for i, (carteira, indice_combinado) in enumerate(melhores, 1):
            soma_pesos = sum(carteira.values())
            st.write(f"**Carteira {i} | Índice Combinado: {indice_combinado:.2f} | Soma: {soma_pesos}%**")
            for ticker, pct in sorted(carteira.items()):
                if pct > 0:
                    st.write(f" - {ticker}: {pct}%")
            st.write("---")