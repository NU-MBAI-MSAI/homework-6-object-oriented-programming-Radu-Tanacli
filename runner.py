import unittest
from tests import test_city, test_pandemic

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_city))
suite.addTests(loader.loadTestsFromModule(test_pandemic))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)