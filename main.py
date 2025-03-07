# main.py
import os
import logging
import time
import sys
import threading 
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication
from config.settings import Settings
from modules.model_manager import ModelManager
from modules.nlp_processor import NLPProcessor
from modules.voice_handler import VoiceCommandHandler
from modules.ai.conversational_assistant import AsistenteConversacional
from ui.holographic_ui import HolographicUI
from utils.logger_setup import setup_voice_logger
from modules.nlp_processor import NLPProcessor 

logger = setup_voice_logger()

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = HolographicUI()  # Crea la UI
        self.nlp = NLPProcessor()
        self.voz = VoiceCommandHandler(self.nlp, self.ui)
        self.inicializar_sistema()  # ✅ Llama al método de inicialización

    def inicializar_sistema(self):  # ✅ Método faltante
        """Inicializa los componentes principales del sistema."""
        try:
            self.ui.mostrar_respuesta("Inicializando modelos...")
            self.model_manager = ModelManager()
            self.ui.mostrar_respuesta("Cargando procesador NLP...")
            self.nlp = NLPProcessor()
            self.ui.mostrar_respuesta("Configurando módulo de voz...")
            self.voz = VoiceCommandHandler(self.nlp, self.ui)
            self.ui.mostrar_respuesta("Preparando manejador de comandos...")
            self.conversational = AsistenteConversacional()
            self.ui.mostrar_respuesta("Sistema listo. Escuchando comandos...")
        except Exception as e:
            logging.critical(f"Error de inicialización: {str(e)}")
            self.ui.mostrar_respuesta("Error crítico en la carga del sistema")
            raise

    def run(self):
        """Ejecuta la aplicación."""
        self.ui.show()
        sys.exit(self.app.exec_())

def mostrar_banner(cargando_event):
    """
    Muestra el banner de ISISIA y una animación de carga.
    :param cargando_event: Objeto threading.Event para controlar el bucle.
    """
    banner = """
    ░██████╗░██████╗░██╗░░░░░███████╗██╗░░░██╗
    ██╔════╝██╔═══██╗██║░░░░░██╔════╝╚██╗░██╔╝
    ╚█████╗░██║██╗██║██║░░░░░█████╗░░░╚████╔╝░
    ░╚═══██╗╚███╔╝██║██║░░░░░██╔══╝░░░░╚██╔╝░░
    ██████╔╝░╚══╝░╚═╝███████╗███████╗░░░██║░░░
    ╚═════╝░░░░░░░░░░░╚══════╝╚══════╝░░░╚═╝░░░
    """
    print(banner)
    try:
        while cargando_event.is_set():  # ✅ Usa el evento para controlar el bucle
            for i in range(4):
                print(f"\rCargando módulos{'.' * i}", end="")
                time.sleep(0.5)
        print("\nSistema ISISIA operativo")
    except KeyboardInterrupt:
        print("\n✅ Carga interrumpida por el usuario.")
        cargando_event.clear()

        cargando_event.clear()
   

if __name__ == "__main__":
    cargando_event = threading.Event()
    cargando_event.set()  # Activa el evento (inicia la animación)
    
    # Inicia el banner en un hilo separado
    banner_thread = threading.Thread(target=mostrar_banner, args=(cargando_event,))
    banner_thread.start()
    
    # Inicia la aplicación
    try:
        aplicacion = Application()  # Tu clase Application existente
        aplicacion.run()
    except KeyboardInterrupt:
        print("\n🔒 Cerrando aplicación...")
    finally:
        cargando_event.clear()  # Detiene la animación
        banner_thread.join()  # Espera a que el hilo del banner termine