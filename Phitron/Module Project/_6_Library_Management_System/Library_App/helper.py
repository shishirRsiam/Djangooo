import os, random, string


def generate_transaction_id():
        transaction_id = random.choice(string.ascii_uppercase)
        for i in range(9):
            if i % 2 == 0:
                transaction_id += str(random.randint(0, 9))
            else:
                transaction_id += random.choice(string.ascii_uppercase)

        return transaction_id
