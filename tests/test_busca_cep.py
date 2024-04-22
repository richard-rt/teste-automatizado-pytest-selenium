from selenium import webdriver
from pages.pagina_busca_cep import PaginaBuscaCep


def test_buscar_cep():
    service = webdriver.ChromeService()
    navegador = webdriver.Chrome(service=service)
    pagina = PaginaBuscaCep(navegador)
    pagina.carregarUrl()
    pagina.inserirEndereco()
    pagina.clicarBottonBuscar()
    pagina.sleep(3)
    endereco, bairro, cidade = pagina.getInformacoesCep()
    assert endereco == 'Avenida Coronel Sezefredo Fagundes - de 14000/14001 ao fim'
    assert bairro == 'Núcleo do Engordador'
    assert cidade == 'São Paulo/SP'
