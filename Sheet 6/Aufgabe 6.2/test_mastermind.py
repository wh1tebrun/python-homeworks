from mastermind import *


def test_remove_char():
    assert remove_char("hallo", "l") == "halo"
    assert remove_char("hallo", "o") == "hall"
    assert remove_char("hallo", "x") == "hallo"
    assert remove_char("DAEAB", "A") == "DEAB"


def test_perfect_chars():
    assert perfect_chars("hallo",
                         "hola ") == "hl"
    assert perfect_chars("ABBBBC",
                         "BBAAAA") == "B"
    assert perfect_chars("DABACC",
                         "AAEACD") == "AAC"
    assert perfect_chars("DCADB",
                         "CCADD") == "CAD"
    assert perfect_chars("ACBDE",
                         "CDEAC") == ""
    assert perfect_chars("Supercalifragilisticexpialidocious",
                         "Donaudampfschifffahrtsgesellschaft") == "afic"


def test_correct_chars():
    assert correct_chars("ABBDC",
                         "AACCD") == "ADC"
    assert correct_chars("AACCD",
                         "ABBDC") == "ACD"
    assert correct_chars("ABABA",
                         "CDBCD") == "B"
    assert correct_chars("hallo",
                         "hola ") == "halo"
    assert correct_chars("ABABA",
                         "CDCDC") == ""
    assert correct_chars("Supercalifragilisticexpialidocious",
                         "Donaudampfschifffahrtsgesellschaft") == "upercalifaglstceados"
    assert correct_chars("Donaudampfschifffahrtsgesellschaft",
                         "Supercalifragilisticexpialidocious") == "oaudapfsciartsgeellc"


def test_compare():
    assert compare("hallo",
                   "hola ") == (2, 2)
    assert compare("BAECC",
                   "BAAEC") == (3, 1)
    assert compare("ABCDE",
                   "EADCB") == (0, 5)
    assert compare("ACABA",
                   "CDBBC") == (1, 1)
    assert compare("ABABA",
                   "CDCDC") == (0, 0)
    assert compare("Donaudampfschifffahrtsgesellschaft",
                   "Supercalifragilisticexpialidocious") == (4, 16)


if __name__ == '__main__':
    test_remove_char()
    test_perfect_chars()
    test_correct_chars()
    test_compare()
