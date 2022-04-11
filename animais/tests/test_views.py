from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal='calopsita',
            predador='Não',
            venenoso='Não',
            domestico='Sim'
        )

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste que verificar se a index retorna com as caracteristicas do animal pesquisado"""
        response = self.client.get('/', {'buscar': 'calopsita'})
        caracaterisiticas_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracaterisiticas_animal_pesquisado[0].nome_animal, 'calopsita')
