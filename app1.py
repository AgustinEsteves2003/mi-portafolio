# app.py (o el nombre que le des a tu archivo principal)
import streamlit as st

st.set_page_config(page_title="Portafolio de Agustin Esteves", layout="wide", page_icon="👤")

# --- Encabezado ---
st.title("¡Hola! Soy Agustin Esteves")
st.write("Bienvenido/a a mi portafolio de proyectos de Streamlit. Este espacio está dedicado a exhibir mis proyectos en Big Data y Machine Learning, donde aplico técnicas avanzadas para resolver problemas complejos, identificando patrones significativos y generando insights accionables que impactan directamente en la toma de decisiones económicas.")

st.markdown("---")

# --- Acerca de mí (Opcional) ---
st.header("Acerca de mí")
st.write("Soy un Economista recibido en la Facultad de Ciencias Economicas de la UBA. Mi formación en economía me ha proporcionado una sólida base en análisis cuantitativo, teoría de juegos y modelado econométrico, lo que me permite abordar los problemas desde una perspectiva holística y entender el contexto económico detrás de cada conjunto de datos.")
st.write("""Mi interés en la ciencia de datos surgió al darme cuenta del potencial ilimitado de estas herramientas para mejorar la precisión de las predicciones económicas, optimizar recursos y descubrir oportunidades que los métodos tradicionales no pueden revelar. He aprendido a cargar, filtrar y limpiar grandes volumenes de datos con Pandas y a crear modelos de aprendizaje supervisado como Random Forests y XGBoost. Tengo conocimientos intermedios en lenguaje Python y basicos en STATA y R.""")
st.markdown("---")
st.header("Mis Proyectos")
col1, col2 = st.columns(2)

with col1:
    # --- Proyectos ---
    
    
    # Proyecto 1
    st.subheader("1. Baja de clientes en empresa de telecomunicaciones")
    st.write("Este modelo es un XGBoost con un Recall del 82% que busca detectar aquellos clientes que dejaran el servicio para que la empresa haga un esfuerzo por retenerlos.")
    st.image("telco.PNG") # Reemplaza con una captura de pantalla de tu app
    st.write("[Haga click aqui para ver el proyecto en accion](https://churn-telecomunicaciones-dyrhttuifv7e4phpo9rfqf.streamlit.app/)") # Enlace a la app desplegada
    st.write("[Código Fuente en GitHub](https://github.com/AgustinEsteves2003/churn-telecomunicaciones)")
    

with col2:
    # Proyecto 2
    st.subheader("2. Default crediticio en Taiwan")
    st.write("Creado a modo de trabajo final para la materia Big Data & Machine Learning de la facultad, este modelo de Random Forests con un Recall del 84% "
             " busca predecir la probabilidad de impago de la tarjeta de credito del cliente el proximo mes.")
    st.image("taiwan.PNG") # Reemplaza con una captura de pantalla de tu app
    st.write("[Haga click aqui para ver el proyecto en accion](https://taiwan-big-data-app-itapp2x9fdrmeen2w3itqft.streamlit.app/)")
    st.write("[Código Fuente en GitHub](https://github.com/AgustinEsteves2003/Taiwan-Big-Data-App)")
    
st.markdown("---")
# Agrega más proyectos siguiendo el mismo formato

# --- Contacto ---
st.header("Contacto")
st.write("Puedes conectar conmigo en:")
st.write("[LinkedIn](https://www.linkedin.com/in/agustin-esteves/)")
st.write("[GitHub](https://github.com/AgustinEsteves2003)")
st.write("[agustinesteves2003@gmail.com](mailto:agustinesteves2003@gmail.com)")

