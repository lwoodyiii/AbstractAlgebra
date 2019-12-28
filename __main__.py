import logging
from Group import Group
from Field import Field
from Vector import Vector

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("basic logging")
    t = (1,2,3)
    v = Vector(t)
    ans = v * 3
    print(v)
    
if __name__ == "__main__":
    main()
