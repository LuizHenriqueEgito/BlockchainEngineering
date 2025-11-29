from fastapi import FastAPI
from fastapi.responses import ORJSONResponse, RedirectResponse

from src.blockchain import (
    Blockchain,
    mine_block,
    display_chain,
    valid_blockchain
)


# Para rodar: uvicorn 01_api_blockchain:app --reload
app = FastAPI(default_response_class=ORJSONResponse)

blockchain = Blockchain()

@app.get("/")
def root():
    return RedirectResponse(url="/get-chain")

@app.get('/mine-block')
def mine_block_api():
    response = mine_block(blockchain)
    return response


@app.get('/get-chain')
def display_chain_api():
    response = display_chain(blockchain)
    return response


@app.get('/valid-blockchain')
def valid_blockchain_api():
    response = valid_blockchain(blockchain)
    return response
