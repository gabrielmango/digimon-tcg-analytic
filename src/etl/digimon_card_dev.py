from time import sleep
from typing import Optional

from src.scrapy.selenium_manager import SeleniumManager
from src.utils.logger import LoggerManager

logger = LoggerManager('DigimonCardDev')


class DigimonCardDev(SeleniumManager):
    def __init__(self, logger, url: Optional[str] = None) -> None:
        super().__init__(logger, url)
        self._url = 'https://digimoncard.dev/'

    def pesquisa_pagina(self, id_card):
        self._logger.logger.info(f'Pesquisa na barra de busca: {id_card}')
        self.abrir_pagina()
        self.espera_carregar_pagina()
        self.escrever(self.criar_locator('id', 'tags-filled'), id_card, enter=True)
        sleep(3)
        self._logger.logger.info('Pesquisa finalizada!')


@logger.log_execution
def executa_busca():
    digimon_card_dev = DigimonCardDev(logger)
    digimon_card_dev.pesquisa_pagina('EX10-001')
