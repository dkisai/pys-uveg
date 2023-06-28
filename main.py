import streamlit as st
import plotly.express as px
import scipy.stats as stats
import numpy as np

# Streamlit setup
st.title("Distribución de Probabilidad Normal & Teorema de Bayes")
    # Datos del ejemplo 1
col1, col2 = st.columns(2)
with col1:
    # Datos del ejemplo 1
    st.header("Ejemplo 1: Calificación de exámenes")
    st.markdown("""
    Supongamos que las calificaciones de un examen final de matemáticas en una universidad siguen una distribución normal con una media de 75 y una desviación estándar de 10.

    **Pregunta**: ¿Cuál es la probabilidad de que un estudiante elegido al azar haya sacado más de 85 en el examen?
    Usamos la tabla Z o una calculadora de distribución normal. La fórmula para el valor Z es: Z = (X - μ) / σ, donde X es la puntuación, μ es la media y σ es la desviación estándar.
    """)
    media1 = 75
    desviacion_estandar1 = 10
    x1 = 85
    z1 = (x1 - media1) / desviacion_estandar1
    prob1 = (1 - stats.norm.cdf(z1))*100

with col2:
    # Crear gráfica
    x = np.linspace(40, 110, 100)
    y = stats.norm.pdf(x, media1, desviacion_estandar1)
    fig1 = px.line(x=x, y=y, title="Distribución de Calificaciones", labels={'x': 'Calificaciones', 'y': 'Densidad'})
    st.plotly_chart(fig1)
    st.subheader(f"Probabilidad de sacar más de 85: {prob1:.2f}%")

# Datos del ejemplo 2
col1, col2 = st.columns(2)
with col1:
    st.header("Ejemplo 2: Alturas de adultos")
    st.markdown("""
    Supongamos que la altura de los hombres en un país sigue una distribución normal con una media de 177 cm y una desviación estándar de 8 cm.
    **Pregunta**: ¿Cuál es la probabilidad de que un hombre elegido al azar tenga una altura entre 165 cm y 190 cm?
    """)
    media2 = 170
    desviacion_estandar2 = 8
    x2 = 180
    z2 = (x2 - media2) / desviacion_estandar2
    prob2 = (1 - stats.norm.cdf(z2))*100
with col2:
    # Crear gráfica
    x = np.linspace(150, 190, 100)
    y = stats.norm.pdf(x, media2, desviacion_estandar2)
    fig2 = px.line(x=x, y=y, title="Distribución de Alturas", labels={'x': 'Alturas (cm)', 'y': 'Densidad'})
    st.plotly_chart(fig2)
    st.subheader(f"Probabilidad de medir más de 180 cm: {prob2:.2f}%")

# Datos del ejemplo 3
col1, col2 = st.columns(2)
with col1:
    st.header("Ejemplo 3: Pesos de paquetes")
    st.markdown("""
    Supongamos que los pesos de los paquetes en una fábrica de envío siguen una distribución normal con una media de 2 kg y una desviación estándar de 0.1 kg.
    **Pregunta**: ¿Cuál es la probabilidad de que un paquete seleccionado al azar pese menos de 1.9 kg?
    """)
    media3 = 500
    desviacion_estandar3 = 50
    x3 = 550
    z3 = (x3 - media3) / desviacion_estandar3
    prob3 = (1 - stats.norm.cdf(z3))*100
with col2:
    # Crear gráfica
    x = np.linspace(400, 600, 100)
    y = stats.norm.pdf(x, media3, desviacion_estandar3)
    fig3 = px.line(x=x, y=y, title="Distribución de Pesos", labels={'x': 'Pesos (g)', 'y': 'Densidad'})
    st.plotly_chart(fig3)
    st.subheader(f"Probabilidad de que un paquete pese más de 550 g: {prob3:.2f}%")


# Teorema de Bayes
st.header("Teorema de Bayes en la industria")
col1, col2 = st.columns(2)
with col1:
    # Ejemplo 1 (dos eventos)
    st.subheader("Ejemplo 1: Prueba de calidad en fabricación")
    st.markdown("""
    Supongamos que en una fábrica se producen piezas de metal y que el 5% de estas piezas son defectuosas. Si hay una prueba de calidad que detecta las piezas defectuosas con una precisión del 98%, pero que también identifica erróneamente piezas no defectuosas como defectuosas en un 3% de los casos.

    Pregunta: Si una pieza es identificada como defectuosa por la prueba, ¿cuál es la probabilidad de que realmente sea defectuosa?
    """)
    prob_defectuosa = 0.05
    prob_prueba_correcta = 0.98
    prob_falso_positivo = 0.03

    # Teorema de Bayes
    numerador = prob_prueba_correcta * prob_defectuosa
    denominador = (prob_prueba_correcta * prob_defectuosa) + (prob_falso_positivo * (1 - prob_defectuosa))
    prob_posterior = (numerador / denominador)*100
    st.write(f"Probabilidad de que realmente sea defectuosa: {prob_posterior:.2f}%")
with col2:
    # Crear gráfico para el Teorema de Bayes Ejemplo 1
    fig4 = px.bar(x=['Defectuoso y detectado', 'No defectuoso pero detectado'], y=[prob_posterior, 1-prob_posterior], title="Probabilidad de detección de elementos defectuosos", labels={'x': 'Casos', 'y': 'Probabilidad'})
    st.plotly_chart(fig4)

col1, col2 = st.columns(2)

col1, col2 = st.columns(2)
with col1:
# Ejemplo 2 (tres eventos)
    st.subheader("Ejemplo 2: Diagnóstico de enfermedades en una clínica")
    st.markdown("""
    Supongamos que en una clínica se realizan pruebas para detectar tres tipos de enfermedades (A, B y C) en los pacientes. La probabilidad de que un paciente tenga la enfermedad A es del 0.2, la enfermedad B es del 0.3 y la enfermedad C es del 0.1. Además, la prueba detecta correctamente la enfermedad A en un 90% de los casos, la enfermedad B en un 85% de los casos, y la enfermedad C en un 95% de los casos.
    Pregunta: Si un paciente da positivo en la prueba, ¿cuál es la probabilidad de que tenga cada una de las enfermedades (A, B, o C)?
    """)
    prob_A = 0.2
    prob_B = 0.3
    prob_C = 0.1
    prob_pos_A = 0.9
    prob_pos_B = 0.85
    prob_pos_C = 0.95

    # Teorema de Bayes para cada enfermedad
    prob_total_pos = (prob_pos_A * prob_A) + (prob_pos_B * prob_B) + (prob_pos_C * prob_C)
    prob_posterior_A = ((prob_pos_A * prob_A) / prob_total_pos)*100
    prob_posterior_B = ((prob_pos_B * prob_B) / prob_total_pos)*100
    prob_posterior_C = ((prob_pos_C * prob_C) / prob_total_pos)*100
    st.write(f"Probabilidad de tener enfermedad A: {prob_posterior_A:.2f}%")
    st.write(f"Probabilidad de tener enfermedad B: {prob_posterior_B:.2f}%")
    st.write(f"Probabilidad de tener enfermedad C: {prob_posterior_C:.2f}%")
# Teorema de Bayes con gráficos
with col2:
    # Crear gráfico para el Teorema de Bayes Ejemplo 2
    fig5 = px.bar(x=['Enfermedad A', 'Enfermedad B', 'Enfermedad C'], y=[prob_posterior_A, prob_posterior_B, prob_posterior_C], title="Probabilidades posteriores de enfermedades", labels={'x': 'Enfermedades', 'y': 'Probabilidad Posterior'})
    st.plotly_chart(fig5)

st.success('Diego Kisai Alba Gallart')