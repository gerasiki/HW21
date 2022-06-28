from classes import Request


def main(store, shop):
    while(True):
        user_input = input("Введите запрос ")

        if user_input == 'стоп':
            break

        try:
            request = Request(user_input)
        except Exception as e:
            print(f'Некорректный запрос: {e}')
            print(f'Пример правильного запроса:'
                  f'Доставить 4 сок из склад в магазин')
            continue

        from_ = store if request.from_ == 'склад' else shop
        to = shop if request.to == 'магазин' else store

        if request.product in from_.items:
            print(f"Нужный товар есть в пункте {request.from_}")
        else:
            print(f"В пункте {request.from_} нет такого товара")
            continue

        if from_.items[request.product] >= request.amount:
            print(f"Нужное количество есть в пункте {request.from_}")
        else:
            print(f"В пункте {request.from_} не хватает {request.amount - from_.items[request.product]}")
            continue

        if to.get_free_space >= request.amount:
            print(f"В пункте {request.to} достаточно места")
        else:
            print(f"В пункте {request.to} не хватает: {request.amount - to.get_free_space}")
            continue

        if request.to == "магазин" and to.get_unique_items_count == 5 and request.product not in to.items:
            print("В магазине достаточно уникальных значений")
            continue

        print(f"{from_}, {to}")
        from_.remove(request.product, request.amount)
        print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}")
        print(f"Курьер везёт {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}")
        to.add(request.product, request.amount)
        print(f"Курьер доставил {request.amount} {request.product} из пункта {request.to}")

        print("="*30)
        print(f"На складе:")
        for title, count in store.items.items():
            print(f"{title}: {count}")
        print(f"Свободного места {store.get_free_space}")
        print("=" * 30)
        print(f"В магазине:")
        for title, count in shop.items.items():
            print(f"{title}: {count}")
        print(f"Свободного места {shop.get_free_space}")
        print("=" * 30)
