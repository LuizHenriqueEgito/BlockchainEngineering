from pprint import pprint


from src.blockchain import (
    Blockchain,
    mine_block,
    display_chain,
    valid_blockchain
)

blockchain = Blockchain()

for i in range(5):
    print(f'Mine block: {i + 1}')
    pprint(mine_block(blockchain))
    print('-' * 50)
    print('\n')
print('END \n')

print('Looking at our Chain')
print(display_chain(blockchain))
print('\n')
print('Validating our Blockchain')
print(valid_blockchain(blockchain))
