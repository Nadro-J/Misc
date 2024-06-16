import os
import time
import json
from substrateinterface import SubstrateInterface, Keypair
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Environment variables from .env
SUBSTRATE_WSS = os.getenv('SUBSTRATE_WSS')
MNEMONIC = os.getenv('MNEMONIC')

substrate = SubstrateInterface(url=SUBSTRATE_WSS, auto_reconnect=True)


def submit(call):
    keypair = Keypair.create_from_mnemonic(MNEMONIC)
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    print(f"Extrinsic '{receipt.extrinsic_hash}' sent and included in block '{receipt.block_hash}'")
    time.sleep(3)


def make_it_rain(asset_id: int, snapshot: str):
    """
    This function reads a JSON file containing a list of addresses with corresponding amounts,
    creates and sends batch transactions to transfer a fixed amount to each address, and updates
    the JSON file to remove processed addresses.

    The function processes the addresses in batches of 100. For each batch, it:
    1. Composes transfer calls for each address.
    2. Composes a batch call containing the transfer calls.
    3. Submits the batch call.
    4. Removes the processed addresses from the JSON file.
    5. Updates the JSON file with the remaining addresses.

    Parameters:
    asset_id (int): The ID of the asset to be transferred.

    Example of input JSON (output_data.json):
    {
        "7LMzi8NGEtDYN6pwQhjcB7MrqS69vRmXDXNrYfT71NSdj7qE": 13485530000000000,
        "7MuXj4KmGv2FkmKeR6rAixiapasCUQimXgDybpwnBrbPDiBc": 5370950000000000,
        "7LbcT8uagimaBuJEFW7wFtR4d6sS5BdAAyPSRtjsFYXB7iov": 4416100000000000,
        "7KcBM3YRJAvhNQn5ir96h2JJf8sXQWViMGUyguZRU7qGM9Vi": 1717530000000000
    }
    """
    with open(snapshot, 'r') as file:
        addresses = json.load(file)

    calls = []
    counter = 0
    processed_keys = []

    # Iterate through the address data and create calls
    for destination, amount in list(addresses.items()):
        counter += 1
        call = substrate.compose_call(
            call_module='Tokens',
            call_function='transfer',
            call_params={
                'dest': destination,
                'currency_id': asset_id,  # Asset ID on Hydration
                'amount': 69000000000     # Amount to send
                # You can use variable 'amount' to create a type of
                # multiplier based on what the account is holding at the time.
            }
        )
        calls.append(call)
        processed_keys.append(destination)

        if counter % 100 == 0:
            batch_call = substrate.compose_call(
                call_module='Utility',
                call_function='batch_all',
                call_params={
                    'calls': calls
                }
            )

            submit(batch_call)
            print(f"Processed: {counter} | Left: {len(addresses)}")

            # Remove processed keys from the original dictionary
            for key in processed_keys:
                addresses.pop(key)

            # Update the JSON file
            with open(snapshot, 'w') as file:
                json.dump(addresses, file, indent=4)

            calls.clear()
            processed_keys.clear()

    # Process any remaining calls
    if calls:
        print(f"Processing final batch of {len(calls)}")
        batch_call = substrate.compose_call(
            call_module='Utility',
            call_function='batch_all',
            call_params={
                'calls': calls
            }
        )
        submit(batch_call)

        # Remove processed keys from the original dictionary
        for key in processed_keys:
            addresses.pop(key)

        # Update the JSON file
        with open(snapshot, 'w') as file:
            json.dump(addresses, file, indent=4)


if __name__ == '__main__':
    make_it_rain(asset_id=1000019, snapshot='sample-snapshot-asset-1000019.json')
