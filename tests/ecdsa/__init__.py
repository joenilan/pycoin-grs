import doctest
import pycoin_grs.tx.script.microcode


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pycoin_grs.tx.script.microcode))
    return tests
