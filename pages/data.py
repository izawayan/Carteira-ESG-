import pandas as pd
from io import StringIO

# Dados da tabela anterior
data = """Ticker;Indice Combinado
VALE3;32.302
SBSP3;11.954
WEGE3;8.921
EQTL3;7.821
BBDC4;7.87
BBAS3;7.764
ITUB4;6.42
SUZB3;6.471
B3SA3;6.372
RAIL3;5.827
RDOR3;5.545
VBBR3;5.426
RADL3;5.447
ITSA4;5.409
UGPA3;5.035
TIMS3;4.852
KLBN11;4.195
LREN3;4.011
MBRF3;3.692
EGIE3;3.661
ALOS3;3.545
PRIO3;3.487
CPLE6;3.396
CMIG4;3.289
SANB11;3.279
ASAI3;3.114
TOTS3;2.905
NEOE3;2.69
PSSA3;2.691
CYRE3;2.635
CPFE3;2.522
NATU3;2.493
FLRY3;2.447
CSAN3;2.389
HYPE3;2.191
COGN3;1.939
AURE3;1.202
MGLU3;1.13
SLCE3;1.108
YDUQ3;1.068
BEEF3;1.004
MRVE3;0.833
HBSA3;0.771
ECOR3;0.746
CEAB3;0.743
PCAR3;0.608
BRKM5;0.564
MDIA3;0.525
VAMO3;0.522
DXCO3;0.518
MOVI3;0.501
OPCT3;0.291
SIMH3;0.291
CBAV3;0.275
GUAR3;0.221
CAML3;0.145
JSLG3;0.107
GRND3;0.107
BHIA3;0.091
AMBP3;0.08
GFSA3;0.023
ALLD3;0.019
AGRO3;0.102"""

# Usa o StringIO para ler a string como se fosse um arquivo
df = pd.read_csv(StringIO(data), sep=';')

# Ordena o DataFrame em ordem decrescente pelo 'Indice Combinado'
df_sorted = df.sort_values(by='Indice Combinado', ascending=False)

# Exporta o DataFrame para um arquivo CSV
output_filename = 'indice_combinado.csv'
df_sorted.to_csv(output_filename, index=False, sep=';', decimal=',')

print(f"O arquivo '{output_filename}' foi criado com sucesso.")
print("\nPrimeiras linhas do arquivo CSV:")
print(df_sorted.head())