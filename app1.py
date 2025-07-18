# app.py (o el nombre que le des a tu archivo principal)
import streamlit as st

st.set_page_config(page_title="Portafolio de Agustin Esteves", layout="wide")

# --- Encabezado ---
st.title("¡Hola! Soy Agustin Esteves")
st.write("Bienvenido a mi portafolio de proyectos de Streamlit.")
st.write("Soy un estudiante de ultimo año de economia en la Facultad de Ciencias Economicas de la UBA con pasión por crear aplicaciones interactivas y útiles.")
st.markdown("---")

# --- Acerca de mí (Opcional) ---
st.header("Acerca de mí")
st.write("""
    Actualmente me estoy adentrando en el mundo del Data Science:
    aprendi a cargar, filtrar y limpiar grandes volumenes de datos con Pandas y a crear modelos de aprendizaje supervisado
    como Random Forests y XGBoost. Tengo conocimientos intermedios en lenguaje Python y basicos en STATA y R.
""")
st.markdown("---")

# --- Proyectos ---
st.header("Mis Proyectos")

# Proyecto 1
st.subheader("1. en proceso")
st.write("Una breve descripción del proyecto, qué problema resuelve y qué tecnologías se utilizaron (ej. Pandas, Plotly, Scikit-learn).")
st.image("https://via.placeholder.com/600x300.png?text=Imagen+del+Proyecto+1") # Reemplaza con una captura de pantalla de tu app
st.write("[Ver el Proyecto 1 en acción](https://tu-enlace-al-proyecto-1.streamlit.app/)") # Enlace a la app desplegada
st.write("[Código Fuente en GitHub](https://github.com/tu-usuario/tu-repo-proyecto-1)")
st.markdown("---")

# Proyecto 2
st.subheader("2. Default crediticio en Taiwan")
st.write("Creado a modo de trabajo final para la materia Big Data & Machine Learning de la facultad, este modelo de Random Forests alimentado con datos de 30000 clientes "
         "taiwaneses busca predecir la probabilidad de impago de la tarjeta de credito del cliente el proximo mes. Librerias utilizadas: pandas, scikit-learn, joblib.")
st.image("taiwan.png") # Reemplaza con una captura de pantalla de tu app
st.write("[Haga click aqui para ver el proyecto en accion](https://taiwan-big-data-app-itapp2x9fdrmeen2w3itqft.streamlit.app/)")
st.write("[Código Fuente en GitHub](https://github.com/AgustinEsteves2003/Taiwan-Big-Data-App)")
st.markdown("---")

# Agrega más proyectos siguiendo el mismo formato

# --- Contacto ---
st.header("Contacto")
st.write("Puedes conectar conmigo en:")
st.write("[LinkedIn](https://www.linkedin.com/in/agustin-esteves-0617b22b4/)")
st.write("[GitHub](https://github.com/AgustinEsteves2003)")
st.write("[agustinesteves2003@gmail.com](mailto:agustinesteves2003@gmail.com)")