# mev

An analysis of Maximal Extractable Value (MEV) on the Ethereum network by Garret Nourse, Josh Garbuio, Lia Garrett, Padelis Deligiannis, and Rohan Sanjay. Check out our presentation [here](https://docs.google.com/presentation/d/1rjGLqzAC9AX6Zu7wz3HW_WnYiwd6P-zHn4CMNgsUalU/edit#slide=id.gf093013c0a_0_16)!

### Table of contents

- [Codebase structure](#Codebase-structure)
- [Data sources](#Data-sources)
- [Using mev-inspect](#Using-mev-inspect)
- [Using the mev-blocks API](#Using-the-mev-blocks-API)
- [General MEV terminology](#General-MEV-terminology)

### Codebase structure

```bash
.
├── LICENSE
├── README.md
├── data
│   ├── mev_api
│   │   ├── blocks.csv
│   │   └── transactions.csv
│   └── mev_inspect
│       ├── arbitrage_swaps.csv
│       ├── arbitrages.csv
│       ├── blocks.csv
│       ├── latest_block_update.csv
│       ├── liquidations.csv
│       ├── miner_payments.csv
│       ├── prices.csv
│       ├── punk_bid_acceptances.csv
│       ├── punk_bids.csv
│       ├── punk_snipes.csv
│       ├── swaps.csv
│       └── transfers.csv
├── notebooks
│   ├── analysis
│   │   ├── ML_models_MEV.ipynb
│   │   ├── flashbots.ipynb
│   │   └── mev_eth2.ipynb
│   └── data_extraction
│       ├── mev_api_data.ipynb
│       └── mev_inspect_data.ipynb
└── presentation.pdf
```

Our [data folder](https://github.com/rohansanjay/math-446-mev/tree/main/data) contains CSV files of our data pulled from Flashbot's [mev-inspect](https://docs.flashbots.net/flashbots-data/mev-inspect-py/overview) and [mev-blocks API](https://docs.flashbots.net/flashbots-data/blockapi) data sources. Note that our mev-inspect data corresponds to all blocks mined on 2021-12-10 (0ver 7000 blocks) and our mev-blocks API data corresponds to the 10,000 most recent Flashbots blocks as of 2021-12-13. 

Our [notebooks](https://github.com/rohansanjay/math-446-mev/tree/main/notebooks) folder contains our code used to analyze the Flashbots data and MEV in ETH2. 

### Data sources

We pulled data from [Flashbots](https://docs.flashbots.net/), a research and development organization working on mitigating the negative externalities of current Maximal Extractable Value (from now on MEV) extraction techniques and avoiding the existential risks MEV could cause to state-rich blockchains like Ethereum.

They offer two free services for MEV data: [mev-inspect](https://docs.flashbots.net/flashbots-data/mev-inspect-py/overview) and the [mev-blocks API](https://docs.flashbots.net/flashbots-data/blockapi).

### Using mev-inspect

[mev-inspect](https://docs.flashbots.net/flashbots-data/mev-inspect-py/overview) is a Flashbots tool for analyzing historical MEV activity on-chain that finds miner payments, tokens transfers and profit, swaps and arbitrages, and more for any given block. The data is stored in a Postgres instance on a local Kubernetes cluster. To set up mev-insepct on your local machine, follow the instructions below: 

1. Clone the [mev-inspect-py](https://github.com/flashbots/mev-inspect-py) repo

2. Follow the installation instructions on the repository [README](https://github.com/flashbots/mev-inspect-py#readme)

   1. Running the client requires a RPC_URL endpoint connection to a node on the Ethereum blockchain to fetch blocks, which can be setup for free through [Pokt Portal](https://www.portal.pokt.network/#1)'s "Ethereum Mainnet Archival with trace calls" host

3. Note: when applying the database migrations for the first time, type "heads" instead of "head"

   ```./mev exec alembic upgrade heads```

4. Happy inspecting and exploring!

While it's a bit of a process to setup, the mev-inspect client is a phenomenal resource with a comprehensive variety of MEV data. Once blocks are inspected, the corresponding data is automatically stored in the Postgres instance database. You can connect to this database directly from the command line through the Kubernetes pod to query and explore the data. However, we wanted to conduct our analysis in Python, so we wrote a [script](https://github.com/rohansanjay/math-446-mev/blob/main/notebooks/data_extraction/mev_inspect_data.ipynb) to establish a connection  to the database from a python shell on a local machine, query all the data frames, and download them into CSV files on the host machine. 

### Using the mev-blocks API

The [mev-blocks API](https://blocks.flashbots.net/) contains data for Flashbots blocks and transactions. These are blocks mined by Flashbot miners who select the most profitable bundle of transactions (selected by searchers in the public mempool) and mine it in the next block.   Miners get paid by searchers through a direct transfer smart contract, instead of through transaction fees, so that searchers only pay miners if the transaction didn’t fail.     

The API is fairly easy to access and use with requests—our code to pull the 10,000 most recent blocks and corresponding transactions can be found [here](https://github.com/rohansanjay/math-446-mev/blob/main/notebooks/data_extraction/mev_api_data.ipynb).

### General MEV terminology 

MEV: Maximal (or miner) Extractable Value

Front-running: when a miner steals a profitable opportunity (such as arbitrage) for themselves by sending the same transaction with a higher gas price

Sandwiching: profiting off slippage in liquidity pools by buying and selling before and after large transactions posted in the mempool

DEX arbitrage: If two DEXes are offering a token at two different prices, one can buy the token on the lower-priced DEX and sell it on the higher-priced DEX

Liquidations: if the value of a borrowed asset exceeds the collateral, anyone can liquidate the collateral and collect the liquidation fee for themselves
