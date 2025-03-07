# utils/logger.py
import logging

def setup_voice_logger():
    """
    Configura y retorna un logger para los módulos de voz.
    """
    logger = logging.getLogger("voice_logger")
    logger.setLevel(logging.INFO)
    
    # Evita añadir múltiples handlers si ya están configurados.
    if not logger.handlers:
        # Crear un handler para la salida en consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formateador de mensajes
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        # Agregar el handler al logger
        logger.addHandler(console_handler)
    
    return logger