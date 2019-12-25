import logging
from Group import Group

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("basic logging")
    g = Group()
    a = g.Op(2+1j,2+5j)
    print (a)

def test_main():
    g = Group()
    a = g.Op(1,1)
    assert a == 1

if __name__ == "__main__":
    main()