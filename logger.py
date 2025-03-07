# utils/logger.py

import logging
import os
import sys
import speech_recognition as sr
from config.settings import Settings
from utils.logger import setup_voice_logger

# Agrega el directorio raíz del proyecto (C:\Users\Isaac\Desktop\IsisIA> ) al path de Python.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

logger = setup_voice_logger()

class ModelManager:
    def __init__(self, config=None):
        self.config = config
        
    def _validate_paths(self):
        """Verifica que existan los archivos necesarios."""
        if not os.path.exists(self.config.LLAMA_EXECUTABLE):
            raise FileNotFoundError(f"Ejecutable no encontrado: {self.config.LLAMA_EXECUTABLE}")
            
    def cargar_modelo(self):
        """Carga el modelo usando llama.cpp."""
        self._validate_paths()
        logger.info("Modelo cargado correctamente.")
        return self.config.LLAMA_EXECUTABLE

# Ejemplo de uso
if __name__ == "__main__":
    try:
        config = Settings()
        model_manager = ModelManager(config)
        model_manager.cargar_modelo()
    except Exception as e:
        logger.critical(f"Error crítico: {str(e)}", exc_info=True)


