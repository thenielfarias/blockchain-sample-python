from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('First block')
    blockchain.add_new_block('New block')
    blockchain.add_new_block('Another block')

    print(blockchain.get_all())