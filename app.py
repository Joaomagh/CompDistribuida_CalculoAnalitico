import streamlit as st
import numpy as np
from math import comb  # comb é mais eficiente para calcular combinações "n escolhe k"

def calcular_disponibilidade(n, k, p):
    """
    Calcula a disponibilidade de um serviço com n servidores,
    necessitando de k servidores disponíveis, onde cada um tem
    probabilidade p de estar online.
    
    A(n, k, p) = Σ [de i=k até n] (n escolhe i) * p^i * (1-p)^(n-i)
    """
    if not (0 < k <= n):
        return 0.0
    if not (0 <= p <= 1):
        return 0.0

    disponibilidade_total = 0.0
    for i in range(k, n + 1):
        # Usamos math.comb para (n escolhe i)
        termo = comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        disponibilidade_total += termo
        
    return disponibilidade_total

st.set_page_config(layout="wide")

st.title("Calculadora de Disponibilidade de Sistemas Distribuídos")
st.markdown("Esta ferramenta implementa os exercícios 1.1 e 1.2 da disciplina de Computação Distribuída.")

st.sidebar.header("Parâmetros de Entrada")
st.sidebar.markdown("Use os controles abaixo para simular um cenário.")

n = st.sidebar.slider(
    label="Número total de servidores (n)",
    min_value=1,
    max_value=50,
    value=5,
    step=1,
    help="O número total de réplicas do serviço."
)

k = st.sidebar.slider(
    label="Quorum mínimo de servidores (k)",
    min_value=1,
    max_value=n,  # O valor máximo de k depende de n
    value=3,
    step=1,
    help="O número mínimo de servidores que precisam estar online para o serviço funcionar."
)

p = st.sidebar.slider(
    label="Probabilidade de um servidor estar disponível (p)",
    min_value=0.0,
    max_value=1.0,
    value=0.95,
    step=0.01,
    help="A confiabilidade individual de cada servidor. Ex: 0.99 para 99% de uptime."
)



st.header(f"Análise para n={n}, k={k}, p={p}")

disponibilidade_calculada = calcular_disponibilidade(n, k, p)


st.subheader("Disponibilidade Calculada")
st.metric(
    label=f"Probabilidade de pelo menos {k} de {n} servidores estarem online",
    value=f"{disponibilidade_calculada:.6%}" 
)

st.info(f"A fórmula geral calcula a soma das probabilidades de ter exatamente k, k+1, ..., até n servidores online.", icon="ℹ️")