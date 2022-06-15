from json import loads
from auth_service import get_current_user


def get_all_products():
    with open('./db/products.txt', 'r') as products_file:
        return [loads(line.strip()) for line in products_file]


def buy_product(product_id):
    user = get_current_user()
    with open('./db/users.txt', 'a+') as users_db:
        for line in users_db:
            u = loads(line.strip())
            if u['username'] == user['username']:
                users_db.write(u['products'].append(product_id))

