import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Calculadoras de Saúde",
    page_icon="💪",
    layout="centered"
)

# ==========================================
# TEMA ESCURO PERSONALIZADO
# ==========================================
st.markdown("""
<style>
    /* Fundo principal */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #161B22;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    h1 {
        text-align: center;
        color: #00C853 !important;
    }

    /* Textos */
    p, label, .stMarkdown {
        color: #E6EDF3 !important;
    }

    /* Campos de entrada */
    .stNumberInput input {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 1px solid #30363D !important;
    }

    /* Abas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #0E1117;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #161B22;
        color: #FFFFFF;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #00C853 !important;
        color: #FFFFFF !important;
    }

    /* Botões */
    .stButton > button {
        width: 100%;
        background-color: #00C853;
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #00A844;
        color: #FFFFFF;
    }

    /* Resultado */
    [data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 12px;
    }

    /* Divisórias */
    hr {
        border-color: #30363D;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# TÍTULO
# ==========================================
st.title("💪 Calculadoras de Saúde")

st.markdown(
    "<p style='text-align:center;'>"
    "Calcule seu IMC e sua sugestão de consumo diário de água."
    "</p>",
    unsafe_allow_html=True
)


# ==========================================
# ABAS
# ==========================================
aba_imc, aba_agua = st.tabs([
    "⚖️ Calculadora de IMC",
    "💧 Consumo de Água"
])


# ==========================================
# CALCULADORA DE IMC
# ==========================================
with aba_imc:

    st.header("⚖️ Calculadora de IMC")

    peso = st.number_input(
        "Peso (kg)",
        min_value=1.0,
        max_value=500.0,
        value=70.0,
        step=0.1
    )

    altura = st.number_input(
        "Altura (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.70,
        step=0.01
    )

    if st.button("Calcular IMC", key="calcular_imc"):

        imc = peso / (altura ** 2)

        st.metric(
            "Seu IMC",
            f"{imc:.2f}"
        )

        # Classificação
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            st.warning(f"⚠️ Classificação: **{classificacao}**")

        elif imc < 25:
            classificacao = "Peso normal"
            st.success(f"✅ Classificação: **{classificacao}**")

        elif imc < 30:
            classificacao = "Sobrepeso"
            st.warning(f"⚠️ Classificação: **{classificacao}**")

        else:
            classificacao = "Obesidade"
            st.error(f"🔴 Classificação: **{classificacao}**")

        st.info(
            "O IMC é uma referência geral e não substitui "
            "uma avaliação profissional."
        )


# ==========================================
# CALCULADORA DE ÁGUA
# ==========================================
with aba_agua:

    st.header("💧 Calculadora de Consumo de Água Diário")

    peso_agua = st.number_input(
        "Peso corporal (kg)",
        min_value=1.0,
        max_value=500.0,
        value=70.0,
        step=0.1,
        key="peso_agua"
    )

    if st.button(
        "Calcular consumo de água",
        key="calcular_agua"
    ):

        # Fórmula: peso × 35 ml
        agua_ml = peso_agua * 35
        agua_litros = agua_ml / 1000

        st.metric(
            "Meta diária sugerida",
            f"{agua_litros:.2f} L"
        )

        st.write(
            f"💧 Aproximadamente **{agua_ml:.0f} ml de água por dia**."
        )

        st.info(
            "Essa sugestão utiliza a fórmula de 35 ml por kg de peso. "
            "A necessidade individual pode variar."
        )


# ==========================================
# RODAPÉ
# ==========================================
st.divider()

st.caption(
    "💡 Ferramentas para fins informativos."
)
