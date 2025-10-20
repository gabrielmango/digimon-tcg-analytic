from time import sleep
from typing import Optional

from src.scrapy.selenium_manager import SeleniumManager
from src.utils.logger import LoggerManager

logger = LoggerManager('DigimonCardDev')


class DigimonCardDev(SeleniumManager):
    def __init__(self, logger, url: Optional[str] = None) -> None:
        super().__init__(logger, url)
        self._url = 'https://digimoncard.dev/'

    def busca_card(self, id_card):
        self._logger.logger.info(f'Processo inicializado: busca informações carta "{id_card}".')
        self.abrir_pagina()
        self.espera_carregar_pagina()
        sleep(2)
        self.fechar_pagina()
        self._logger.logger.info(f'Processo finalizado: informações da carta "{id_card}" encontrados.')


@logger.log_execution
def executa_busca():
    digimon_card_dev = DigimonCardDev(logger)
    digimon_card_dev.busca_card('EX10-001')
