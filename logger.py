# utils/logger.py

import logging
import sys
from pathlib import Path

def setup_voice_logger():
    logger = logging.getLogger("voice_logger")
    logger.setLevel(logging.DEBUG)
    
    # Formato del log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Handler para archivo
    log_file = Path(__file__).parent.parent / "logs" / "voice_commands.log"
    log_file.parent.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger