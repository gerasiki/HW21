from classes import Store, Shop
from main import main

if __name__ == '__main__':

    store = Store()
    shop = Shop()

    goods = {
        "вода": 15,
        "сок": 10,
        "хлеб": 20,
        "печеньки": 10,
        "молоко": 10,
        "собачка": 1
    }
    store.items = goods
    main(store, shop)
