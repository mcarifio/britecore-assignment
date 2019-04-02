# From https://engineering-application.britecore.com/quiz/wsmvjefnvwmdkvnen
# The unstated strategy is to diagnose and fix the logic errors.

from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABco3LG1TDv8SsG15ZKa06EiBKP2FpVJ0b9_9kPSzqF0TQiFhROcgQuvRlSHatV5s90UZRZpgYJLmoaMzXbgLiVDCzA3wmFr8xdu8GiUCDYrUFr2KTb3MsFdev6imG603RNOZ-c9LHHaKiEdTnTVcj7_rBf1F5LmWpEPGrtakUTaLy3HK8='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()