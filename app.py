import streamlit as st

# Configuración del título de la página web
st.set_page_config(page_title="Citogenética Vegetal", page_icon="🧬")

st.title("🧬 Gestión de Cromosomas - FISH & DAPI")
st.write("Bienvenido al sistema de trazabilidad de preparados citogenéticos.")

# Creamos dos pestañas en la interfaz web
pestana_registro, pestana_buscar = st.tabs(["📋 Registrar Nueva Muestra", "🔍 Escanear / Buscar Historial"])

# --- PESTAÑA 1: REGISTRO ---
with pestana_registro:
    st.header("Ingreso de Datos del Preparado")
    
    # Campos de texto para que el usuario complete
    especie = st.text_input("Especie o Variedad de la Planta (Ej: Zea mays):")
    protocolo = st.selectbox("Protocolo de Fijación:", ["Fijador Farmer (3:1)", "Carnoy", "Otro"])
    sonda = st.text_input("Sonda de Hibridación (FISH):")
    dapi = st.checkbox("¿Aplicó tinción de contraste DAPI?")
    notas = st.text_area("Notas adicionales o modificaciones del protocolo:")
    
    # Botón para guardar
    botón_guardar = st.button("Guardar Muestra y Generar QR")
    
    if botón_guardar:
        st.success(f"¡Hiciste clic en guardar! (Próximamente procesaremos a: {especie})")

# --- PESTAÑA 2: BUSCADOR ---
with pestana_buscar:
    st.header("Trazabilidad Hacia Atrás")
    st.write("Escribe el código de la muestra o usa el lector para ver el historial.")
    
    codigo_escaner = st.text_input("Código de la Muestra (Ej: CROMO-001):")
    
    if codigo_escaner:
        st.info(f"Buscando el historial para el código: {codigo_escaner}...")
