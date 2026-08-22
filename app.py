import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadoras de Saúde",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Calculadoras de Saúde - William")
st.write("Calcule seu IMC e veja uma sugestão de consumo diário de água.")

# Criando abas
aba_imc, aba_agua = st.tabs([
    "⚖️ Calculadora de IMC",
    "💧 Consumo de Água"
])

# =========================
# CALCULADORA DE IMC
# =========================
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

    if st.button("Calcular IMC", type="primary"):
        imc = peso / (altura ** 2)

        st.metric("Seu IMC", f"{imc:.2f}")

        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            cor = "warning"
        elif imc < 25:
            classificacao = "Peso normal"
            cor = "success"
        elif imc < 30:
            classificacao = "Sobrepeso"
            cor = "warning"
        else:
            classificacao = "Obesidade"
            cor = "error"

        if cor == "success":
            st.success(f"Classificação: **{classificacao}**")
        elif cor == "warning":
            st.warning(f"Classificação: **{classificacao}**")
        else:
            st.error(f"Classificação: **{classificacao}**")

        st.info(
            "A classificação apresentada é uma referência geral e não substitui "
            "uma avaliação realizada por um profissional de saúde."
        )


# =========================
# CALCULADORA DE ÁGUA
# =========================
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

    if st.button("Calcular consumo de água", type="primary"):
        # Fórmula: peso × 35 ml
        agua_ml = peso_agua * 35
        agua_litros = agua_ml / 1000

        st.metric(
            "Meta diária sugerida",
            f"{agua_litros:.2f} litros"
        )

        st.write(
            f"Isso corresponde a aproximadamente **{agua_ml:.0f} ml de água por dia**."
        )

        st.info(
            "Essa é uma sugestão baseada na fórmula de 35 ml por kg de peso. "
            "A necessidade real de hidratação pode variar conforme clima, "
            "atividade física e outras condições individuais."
        )

# Rodapé
st.divider()
st.caption("💡 Ferramentas para fins informativos.")
