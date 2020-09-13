## nulspy-tokenomics

This project contains the code for:  http://westteam.nulstar.com/tokenlife .

The project was created as a prop for a class on blockchain at Portland State University. The class intended to teach the basic six (6) underlining elements (modules) of a functioning blockchain, set-up tokenomic parameters, genesis block, seed node, blockchain explorers, wallets, smart contracts, decentralized application development and deployment, node network and consensus mechanisms.

The dapp allows a user to visualize the tokenomics of a blockchain over time by trying out these settings:

- Total Supply: This is the initial total token supply that will be created for the new blockchain. There are many variables to consider when selecting an initial total token supply including; valuation, funding strategy, consensus node rewards, application use case (s), number/size of transactions, number of users, use case road map and community incentive programs. (Example “100000000”).

- Initial Inflation: The fixed number of new tokens that will be generated to incentivize the blockchain network. (Example “110000000”).

- Total Inflation: Total Supply plus the Initial Amount of Inflation. This will be the maximum supply of tokens for the blockchain. 
The maximum supply cannot be changed in the future unless the code of blockchain is hard forked. Establishing a max supply triggers the need for a deflation rate in order to reach the max supply. Most blockchains opt for a max supply or a deflationary token because it creates token scarcity which might lead to an increased token value over time. Once a max is reached, the network will become reliant on transaction fees to incentivize its continued operations. (Example '210,000,000').

- Inflation Starting Time: The calendar date the inflation commences.

- Deflation Ratio: Is the rate at which the creation of new tokens (inflation) will be decreased at a set interval of time. (example; '0.4' % Deflation Ration).

- Interval (in days): The frequency which the deflation ratio is enforced to decrease the creation of new tokens over time. (example 30 days).

Example:

- NULS was born July 12, 2018. NULS economic specifications are:
- Initial supply on July 12, 2018 was 100,000,000 NULS
- Each year an additional 5,000,000 NULS is created and used for consensus payments, etc. The 5,000,000 NULS is made available each month.  The actual amount available each month is 5,000,000/12 NULS. This is inflation and will continue until the total supply of NULS is 210,000,000. This will take 22 years. (210-100)/5 = 22 
- Deflation begins July 2020, i.e. deflation begins 24 months/intervals after July 2018. Deflation reduces the inflation by 0.4% every month. i.e. deflation is compounded)

The app/dapp aims to help understand the economic ramifications of these settings over time.

To setup and run: You'll need at least python 3.7, flask, and the other goodies in the repo. The easiest way to run it yourself is to use flask as the server. Otherwise you'll need Nginx with Gunicorn, Waitress, or something similar that will serve Python.

To run - see the Instructions.md file. The other run files are provided as helpers for your server setup.

On the server - gunicorn must be running. The python part is in flask_app.py and appsupport.py and runs on port 8084 by nginx and gunicorn via the systemctl file tokenlifeapp.service. The tokenlife service takes care of that. You need sudo to stop and start it, replace it, etc.
