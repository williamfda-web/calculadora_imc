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
# TEMA ESCURO
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    h1 {
        text-align: center;
        color: #00C853 !important;
    }

    p, label, .stMarkdown {
        color: #E6EDF3 !important;
    }

    .stNumberInput input {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 1px solid #30363D !important;
    }

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

    [data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 12px;
    }

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
        value=None,
        placeholder="Digite seu peso",
        step=0.1
    )

    altura = st.number_input(
        "Altura (m)",
        min_value=0.5,
        max_value=2.5,
        value=None,
        placeholder="Digite sua altura. Ex: 1.70",
        step=0.01
    )

    if st.button("Calcular IMC", key="calcular_imc"):

        if peso is None or altura is None:
            st.warning("⚠️ Preencha o peso e a altura.")

        else:
            imc = peso / (altura ** 2)

            st.metric(
                "Seu IMC",
                f"{imc:.2f}"
            )

            # Classificação do IMC
            if imc < 18.5:
                st.warning(
                    "⚠️ Classificação: **Abaixo do peso**"
                )

            elif imc < 25:
                st.success(
                    "✅ Classificação: **Peso normal**"
                )

            elif imc < 30:
                st.warning(
                    "⚠️ Classificação: **Sobrepeso**"
                )

            else:
                st.error(
                    "🔴 Classificação: **Obesidade**"
                )

            st.info(
                "O IMC é uma referência geral e não substitui "
                "uma avaliação realizada por um profissional de saúde."
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
        value=None,
        placeholder="Digite seu peso",
        step=0.1,
        key="peso_agua"
    )

    if st.button(
        "Calcular consumo de água",
        key="calcular_agua"
    ):

        if peso_agua is None:
            st.warning("⚠️ Digite seu peso.")

        else:
            # Fórmula: peso × 35 ml
            agua_ml = peso_agua * 35
            agua_litros = agua_ml / 1000

            st.metric(
                "Meta diária sugerida",
                f"{agua_litros:.2f} L"
            )

            st.write(
                f"💧 Aproximadamente "
                f"**{agua_ml:.0f} ml de água por dia**."
            )

            st.info(
                "Essa sugestão utiliza a fórmula de 35 ml por kg "
                "de peso. A necessidade individual pode variar."
            )


# ==========================================
# RODAPÉ
# ==========================================
st.divider()

st.caption("💡 Ferramentas para fins informativos.")
