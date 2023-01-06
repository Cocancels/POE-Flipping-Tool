import csv
from utils import *

card_data = [
    {
        'name': 'The Patient',
        'type': 'DivinationCard',
        'number': 8,
        'profitItem': 'The Nurse',
        'resultItemType': 'DivinationCard'
    },
    {
        'name': 'The Nurse',
        'type': 'DivinationCard',
        'number': 8,
        'profitItem': 'The Doctor',
        'resultItemType': 'DivinationCard'
    },
    {
        'name': 'The Doctor',
        'type': 'DivinationCard',
        'number': 8,
        'profitItem': 'Headhunter',
        'resultItemType': 'UniqueAccessory'
    },
]

def get_csv_card_data(card):
    type = card['type']
    resultType = card['resultItemType']

    card['chaosValue'] = get_chaos_item_price(type, card['name'])
    card['divineValue'] = get_divine_item_price(type, card['name'])

    card['chaosValueTotal'] = get_chaos_item_price(type, card['name']) * card['number']
    card['divineValueTotal'] = get_divine_item_price(type, card['name']) * card['number']

    card['resultChaos'] = get_chaos_item_price(resultType, card['profitItem'])
    card['resultDivine'] = get_divine_item_price(resultType, card['profitItem'])
    
    card['chaosProfit'] = round(card['resultChaos'] - card['chaosValueTotal'], 2)
    card['divineProfit'] = round(card['resultDivine'] - card['divineValueTotal'], 2)

    return card

def write_card_to_csv(data):
    with open('cards.csv', 'r+', newline='') as file:
        csv_writer = csv.writer(file)

        row = [''] * 4
        row.extend(['Name', 'Number', 'Value (c)', 'Value (div)', 'Value Total (c)', 'Value Total (div)','Result (c)', 'Result (div)', 'Profit (c)', 'Profit (div)'])
        csv_writer.writerow(row)
        

        for card in data:
            row = [''] * 4
            row.extend([card['name'], card['number'], card['chaosValue'], card['divineValue'],  card['chaosValueTotal'], card['divineValueTotal'],card['resultChaos'], card['resultDivine'],card['chaosProfit'], card['divineProfit']])            
            csv_writer.writerow(row)
        
        file.seek(0)
        file_contents = file.read()
        file_contents = file_contents.replace(',', ';')
        file.seek(0)
        file.write(file_contents)
        file.truncate()

def get_csv_cards():
    cards = []
    
    for card in card_data:
        cards.append(get_csv_card_data(card))
    
    return cards