soda_machine = {
    'cans': [
        {
            'type': 'grape',
            'quantity': 10,
            'cost': 0.50
        },
        {
            'type': 'cola',
            'quantity': 10,
            'cost': 0.50
        },
    ],
    'coins': {
        'quarters': 30,
        'dimes': 40,
        'nickels': 50
    },
    'accepts_credit_card': True
}


print(soda_machine['cans'][0]['type'])
print(soda_machine['cans'][0]['cost'])

soda_machine['cans'][0]['cost'] += 0.10

print(soda_machine['cans'][0]['cost'])

for soda in soda_machine['cans']:
    print(f'{soda["type"]} - ${soda["cost"]}')

soda_machine['coins']['quarters'] += 2

soda_machine['accepts_credit_card'] = False

print(soda_machine)
11:35
# -------------------- Another Example in video at 11:35 car = {} --------------------