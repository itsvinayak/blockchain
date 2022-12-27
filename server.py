import os
from flask import Flask, jsonify

# env
PORT = os.getenv('PORT', 8080)
DEBUG = os.getenv('DEBUG', True)

app = Flask(__name__)

from blockchain import Blockchain

blockchain = Blockchain()


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Blockchain</h1>", 200


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {}
    response['message'] = "Blocked is just mined !!"
    response['index'] = block['index']
    response['timestamp'] = block['timestamp']
    response['previous_hash'] = block['previous_hash']
    response['proof'] = block['proof']

    return jsonify(response), 201

@app.route('/get_chain', methods=['GET'])
def get_chain():
    blockchain_clone = blockchain.get_chain()
    return jsonify(blockchain_clone), 200

@app.route('/get_chain_length', methods=['GET'])
def get_chain_length():
    blockchain_len = blockchain.get_length()
    return jsonify(blockchain_len), 200

@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {}
        response['message'] = "Blockchain is valid"
        return jsonify(response), 200
    else:
        response = {}
        response['message'] = "Blockchain is not valid"
        return jsonify(response), 200



if __name__ == "__main__":
  app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
