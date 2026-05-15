import streamlit as st
import qrcode
from io import BytesIO

# 1. TÍTULOS Y ENTRADA DE DATOS (Fuera del botón para que siempre se vean)
st.title("🧬 Gestión de Citogenética")
st.markdown("Introduce los datos de la muestra para generar el QR.")

especie = st.text_input("Especie o Variedad de la Planta", placeholder="Zea mays")
fijador = st.selectbox("Protocolo de Fijación", ["Fijador Farmer (3:1)", "Carnoy", "Otro"])
sonda = st.text_input("Sonda de Hibridación (FISH)", placeholder="180pb-bio")
dapi = st.checkbox("¿Aplicó tinción de contraste DAPI?")
notas = st.text_area("Notas adicionales")

st.divider() # Una línea visual

# 2. EL BOTÓN Y SU LÓGICA
# Solo lo que está "tabulado" (con espacios) a la derecha debajo del 'if' 
# ocurrirá cuando presiones el botón.
if st.button("Guardar Muestra y Generar QR"):
    
    if especie == "":
        st.warning("⚠️ Por favor, escribe al menos el nombre de la especie.")
    else:
        # Texto que irá al QR
        contenido = f"Muestra: {especie}\nFijador: {fijador}\nSonda: {sonda}\nDAPI: {dapi}\nNotas: {notas}"
        
        # Generar QR
        qr = qrcode.make(contenido)
        buf = BytesIO()
        qr.save(buf)
        byte_im = buf.getvalue()
        
        st.success(f"✅ QR Generado para {especie}")
        st.image(byte_im, width=250)
        st.download_button(
            label="Descargar Imagen QR",
            data=byte_im,
            file_name=f"QR_{especie}.png",
            mime="image/png"
        )
