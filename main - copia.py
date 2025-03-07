# main.py
import sys
import threading
import time
import logging  
import os
from PyQt5.QtWidgets import QApplication
from ui.holographic_ui import HolographicUI
from modules.nlp_processor import NLPProcessor
from modules.voice_handler import VoiceCommandHandler
from modules.model_manager import ModelManager
from utils.logger_setup import setup_voice_logger
from modules.ai.conversational_assistant import AsistenteConversacional


logger = setup_voice_logger()

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = HolographicUI()
        self.nlp = NLPProcessor()
        self.voz = VoiceCommandHandler(self.nlp, self.ui)
        self.inicializar_sistema()  # ✅ Llama al método de inicialización

        self.ui.show()  # Muestra la UI inmediatamente
        
    

    def _inicializar_sistema(self):
        """Carga los módulos esenciales con manejo de errores"""
        try:
            self.ui.mostrar_respuesta("🚀 Inicializando modelos...")
            self.model_manager = ModelManager()
            
            self.ui.mostrar_respuesta("🧠 Cargando procesador NLP...")
            self.nlp = NLPProcessor()
            
            self.ui.mostrar_respuesta("🎙 Configurando voz...")
            self.voz = VoiceCommandHandler(
                nlp_processor=self.nlp,
                ui=self.ui,
                modelo_ruta=self.model_manager.modelo_actual
            )
            
            self.ui.mostrar_respuesta("💬 Preparando conversación...")
            self.conversational = AsistenteConversacional()
            
            self.ui.mostrar_respuesta("✅ Sistema listo | Di 'Hola Isis'")
            self.voz.iniciar_escucha()  # Comienza la escucha continua
            
        except Exception as e:
            self.ui.mostrar_respuesta(f"❌ Error crítico: {str(e)}")
            self._liberar_recursos()

    def _liberar_recursos(self):
        """Libera recursos de forma segura"""
        if self.voz:
            self.voz.detener_escucha()
        if self.conversational:
            self.conversational.cerrar()

    def run(self):
        """Ejecuta el bucle principal de la aplicación"""
        try:
            sys.exit(self.app.exec_())
        finally:
            self._liberar_recursos()

if __name__ == "__main__":
    print("🌟 Iniciando ISISIA - Asistente Virtual")
    aplicacion = Application()
    aplicacion.run()