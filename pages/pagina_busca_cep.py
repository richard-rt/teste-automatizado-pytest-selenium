import time
from selenium.webdriver.common.by import By


class PaginaBuscaCep:
    url = 'https://buscacepinter.correios.com.br/app/endereco/index.php'
    cep = '02368000'

    def __init__(self, navegador):
        self.navegador = navegador

    @staticmethod
    def sleep(segundos):
        time.sleep(segundos)

    def carregarUrl(self):
        self.navegador.get(self.url)

    def inserirEndereco(self):
        self.navegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys(self.cep)

    def clicarBottonBuscar(self):
        self.navegador.find_element(By.XPATH,
                                    '/html/body/main/form/div[1]/div[1]/div/section/div[3]/div/div/button').click()

    def getInformacoesCep(self):
        tabela = self.navegador.find_element(By.ID, 'resultado-DNEC')
        endereco = tabela.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
        bairro = tabela.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
        cidade = tabela.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
        return endereco.text, bairro.text, cidade.text
