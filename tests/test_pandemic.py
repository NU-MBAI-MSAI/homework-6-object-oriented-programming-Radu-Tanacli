from unittest import TestCase
from unittest import mock
# from city_data.city import City
# from city_data.pandemic import Pandemic
import io


class TestPandemic(TestCase):
    # init tests
    def setUp(self):
        pass
    #     self.p = Pandemic()
    #     self.p.cities = [City('Chicago'), City('Miami')]

    def test_init(self):
        pass
    #     p1 = Pandemic()
    #     self.assertEqual([], p1.cities)

    # add_city tests
    def test_add_city_new(self):
        pass
    #     self.p.add_city('Atlanta')
    #     cities = [City('Chicago'), City('Miami'), City('Atlanta')]
    #     self.assertEqual(cities, self.p.cities)

    def test_add_city_fail(self):
        pass
    #     with self.assertRaises(ValueError):
    #         self.p.add_city('Chicago')

    # edit_city tests
    def test_edit_city_existing(self):
        pass
    #     self.p.edit_city('Chicago', 172666, 148133, 7590)
    #     city = City('Chicago')
    #     city.infected = 172666
    #     city.recovered = 148133
    #     city.death = 7598
    #     cities = [city, City('Miami')]
    #     self.assertEqual(cities, self.p.cities)

    def test_edit_city_not_existing(self):
        pass
    #     with self.assertRaises(ValueError):
    #         self.p.edit_city('Dallas', 46813, 28865, 605)

    # display_city tests
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_city_existing(self, mock_stdout):
        pass
    #     self.p.display_city('Miami')
    #     exp_out = 'Name: Miami\nInfected: 0, Recovered: 0, Deaths: 0\n'
    #     self.assertEqual(exp_out, mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_city_none(self, mock_stdout):
        pass
    #     self.p.display_city('Austin')
    #     exp_out = 'City not in list\n'
    #     self.assertEqual(exp_out, mock_stdout.getvalue())

    # display_all_city_states tests
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_all_city_stats_by_name(self, mock_stdout):
        pass
    #     self.p.cities = [City('Chicago'), City('Miami'), City('Detroit'), City('Dallas')]
    #     self.p.display_all_city_stats('name')
    #     exp_out = City('Chicago').__str__() + '\n' + City('Dallas').__str__() + '\n' + City('Detroit').__str__() + '\n' + City('Miami').__str__() + '\n'
    #     self.assertEqual(exp_out, mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_all_city_stats_by_infected(self, mock_stdout):
        pass
    #     self.p.cities = [City('Chicago', 200, 3, 19), City('Miami', 500, 2, 35), City('Detroit', 84, 45, 3), City('Dallas')]
    #     self.p.display_all_city_stats('infected')
    #     exp_out = City('Dallas').__str__() + '\n' + City('Detroit', 84, 45, 3).__str__() + '\n' + City('Chicago', 200, 3, 19).__str__() + '\n' + City('Miami', 500, 2, 35).__str__() + '\n'
    #     self.assertEqual(exp_out, mock_stdout.getvalue())