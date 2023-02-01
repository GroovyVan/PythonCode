card = str('')
for i in range(13):
    card += str(i)
print (card)

def get_hidden_card(card_number,hidden=4):
    card_number = str(card_number)
    return f'{"*"*hidden}{card_number[-4:]}'

x = get_hidden_card(card)
print('card',x)