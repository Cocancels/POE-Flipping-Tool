from utils import *
from cards import *
            
def main():
    cards = get_csv_cards()

    write_card_to_csv(cards)

if __name__ == '__main__':
    main()
