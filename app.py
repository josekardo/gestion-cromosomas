import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# ... (tus campos de texto anteriores) ...

if st.button("Guardar Muestra y Generar QR"):
    # 1. Agrupamos la información que irá dentro del QR
    contenido_qr = f"""
    ID: {especie}
    Fijador: {fijador}
    Sonda: {sonda}
    DAPI: {dapi}
    Notas: {notas}
    """
    
    # 2. Generamos el QR
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(contenido_qr)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white")
    
    # 3. Convertimos la imagen para que Streamlit la muestre
    buf = BytesIO()
    img_qr.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    # 4. Mostramos el resultado
    st.success("✅ ¡Código generado con éxito!")
    st.image(byte_im, caption=f"QR para la muestra {especie}", width=300)
    
    # 5. Botón para descargar e imprimir
    st.download_button(
        label="Descargar código QR para imprimir",
        data=byte_im,
        file_name=f"QR_{especie}.png",
        mime="image/png"
    )
