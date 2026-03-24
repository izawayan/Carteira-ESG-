import numpy as np

def obter_melhores_carteiras(acoes, restricoes_minimas, num_tentativas=100000):
    """
    Gera carteiras usando vetorização (NumPy) para máxima performance.
    """
    tickers = list(acoes.keys())
    n_ativos = len(tickers)
    
    # Extrai os índices combinados para um array NumPy
    indices = np.array([acoes[t]['indice_combinado'] for t in tickers])
    
    # Array com os pesos mínimos escolhidos pelo usuário
    pesos_min = np.array([restricoes_minimas.get(t, 0) for t in tickers])
    peso_restante = 100 - np.sum(pesos_min)
    
    # Se o usuário já alocou 100%, só existe uma carteira possível
    if peso_restante <= 0:
        carteira_unica = {tickers[i]: float(pesos_min[i]) for i in range(n_ativos)}
        score = np.sum((pesos_min / 100.0) * indices)
        return [(carteira_unica, score)]

    # 1. Gera pesos aleatórios usando Distribuição de Dirichlet (ideal para proporções que somam 1)
    pesos_aleatorios = np.random.dirichlet(np.ones(n_ativos), size=num_tentativas) * peso_restante
    
    # Arredonda para inteiros (para o painel ficar mais limpo)
    pesos_aleatorios = np.round(pesos_aleatorios)
    
    # Ajusta pequenas diferenças de arredondamento no primeiro ativo para garantir exatos 100%
    diferencas = peso_restante - np.sum(pesos_aleatorios, axis=1)
    pesos_aleatorios[:, 0] += diferencas
    
    # 2. Soma os pesos aleatórios com as restrições mínimas
    matriz_pesos_finais = pesos_aleatorios + pesos_min
    
    # 3. Calcula o Índice Combinado de todas as 100.000 carteiras de uma vez (Produto Escalar)
    scores = np.dot(matriz_pesos_finais / 100.0, indices)
    
    # 4. Encontra os índices das 5 carteiras com as maiores pontuações
    top_5_idx = np.argsort(scores)[-5:][::-1]
    
    # 5. Formata a saída
    resultados = []
    for idx in top_5_idx:
        carteira = {tickers[i]: float(matriz_pesos_finais[idx, i]) for i in range(n_ativos)}
        resultados.append((carteira, float(scores[idx])))
        
    return resultados
