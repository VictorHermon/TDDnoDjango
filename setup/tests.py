from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal


class AnimalTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/victor/PycharmProjects/buscaAnimal/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal='leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """
        Teste para ver se o usuário consegue encontrar um animal pesquisando no site
        :return:
        """
        # Vini, deseja encontrar um novo animal para adotar

        # Ele encontra o site Busca Animal e decide usar o site
        self.browser.get(self.live_server_url + '/')

        # Porque ele vê no menu do site escrito Busca Animal
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')

        # Ele pesquisa por Leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 características do animal pesquisado
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um leão
