import logging
from dataclasses import dataclass

@dataclass
class LogConfig:

    log_file: str = 'logs/logging.log'

    format: str = "%(asctime)s - %(levelname)s - %(message)s"

    log_level: int = logging.DEBUG
