import logging
from Group import Group
from Field import Field

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("basic logging")
    s = {1,2,3}
    g = Group(s)
    print(g)
    
if __name__ == "__main__":
    main()