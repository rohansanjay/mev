import requests as r
import pandas as pd
import numpy as np



def callapi(blockssavepath,transactionssavepath,block_number):
    blocks_df = pd.DataFrame(columns=['block_number', 'miner_reward', 'miner', 'coinbase_transfers', 'gas_used', 'gas_price', 'is_megabundle'])
    transactions_df = pd.DataFrame(columns=['transaction_hash', 'tx_index', 'bundle_type', 'bundle_index', 'block_number', 'eoa_address', 'to_address', 'gas_used', 'gas_price', 'coinbase_transfer', 'total_miner_reward'])

    blocks = r.get('https://blocks.flashbots.net/v1/blocks?limit='+str(block_number)+'').json()

    for block in blocks['blocks']:
        transactions = block['transactions']
        del block['transactions']
        blocks_df = blocks_df.append(block, ignore_index=True)
        
        for transaction in transactions:
            transactions_df = transactions_df.append(transaction, ignore_index=True)

    blocks_df.to_pickle(blockssavepath)
    transactions_df.to_pickle(transactionssavepath)

    print('API called for '+str(block_number)+' blocks.')