from twttr import shorten

def main():
    test_lower()
    test_upper()
    test_novowel()


def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_lower():
    assert shorten("twitter") == "twttr"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_novowel():
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()