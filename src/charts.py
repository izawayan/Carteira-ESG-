import plotly.express as px
import pandas as pd

def plot_price(df_hist, empresa):
    return px.line(df_hist, x=df_hist.index, y="Close", title=f"Histórico de {empresa}")

def plot_esg_scores(empresa):
    esg_data = {
        "Categoria": ["Environmental", "Social", "Governance"],
        "Score": [80, 75, 85]  # Simulados
    }
    df = pd.DataFrame(esg_data)
    return px.bar(df, x="Categoria", y="Score", title=f"ESG Scores - {empresa}",
                  color="Categoria", text="Score")
