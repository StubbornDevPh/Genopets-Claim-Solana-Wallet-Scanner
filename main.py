# pip install solana
from solana.rpc.api import Client

# https://docs.solana.com/cluster/rpc-endpoints used mainnet beta because
# I need accuracy
http_client = Client("https://api.mainnet-beta.solana.com")

# check for every signatures for the wallet adress in the string
signatures = (
    http_client.get_signatures_for_address(
        "4CTLSnrW22KDuX6bVvdRDiz1do9XNncnJMYb5odGDZJz",
        limit=1000))

# for every signatures remove other data except list of result
signatures = signatures['result']

# make a counter
totalHarvest = 0
try:
    # loop each item in list
    for signature_unprocessed in signatures:
        # get signature for each item
        signature = signature_unprocessed['signature']
        # check transaction details
        tx = http_client.get_transaction(signature)
        # check fee (0.000015) gas fee for harvest shout out to Elias |
        # uNoobs💧#113 (#673 #513)
        fee = tx['result']['meta']['fee']
        # multiply initial fee to 1,000,000,000 since that is being used in
        # blockchain logic
        if fee == 15000:
            # parse logs made by genopet contract
            messageLogs = tx['result']['meta']['logMessages']
            # ensure the logs contain the word HarvestKi
            for log in messageLogs:
                if log == "Program log: Instruction: HarvestKi":
                    # count it
                    totalHarvest += 1
except Exception as e:
    print(e)

print(f"total harvest:{totalHarvest}")
