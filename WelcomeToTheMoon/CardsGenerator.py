import csv
from typing import List

class SpacecraftCard:
    number: int = any
    actionSymbol: str = any
    
    def __str__(self):
        return f"{self.number} / {self.actionSymbol}"

cards: List[SpacecraftCard] = []
print(cards)

with open('data/SpacecraftCards.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        card: SpacecraftCard = SpacecraftCard()
        card.number = row['Number']
        card.actionSymbol = row['ActionSymbol']
        
        cards.append(card)

print(cards)
