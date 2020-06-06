from decor import *
import json


def viewing(lst_prod, read):
    lst_prod = []
    with open('goods.txt') as f:
        for line in f.readlines():
            lst_prod.append(Good(json.loads(line)))
    for i in lst_prod:
        print(i)

def read(lst_prod):
    with open('goods.txt') as f:
        for line in f.readlines():
            lst_prod.append(Good(json.loads(line)))

def write(lst_prod):
    for i in lst_prod:
        print(i)
    with open('goods.txt', 'w') as f:
        f.truncate()
        for elem in lst_prod:
            print(json.dumps(elem.__dict__), file=f)


def main():
    lst_prod = []
    while True:
        print('-'*110)
        print('1. Просмотр каталога товаров')
        print('2. Сделать новый заказ')
        print('3. Просмотр корзины')
        print('4. Удалить из корзины')
        print('5. Провести черную пятницу (скидка 10%) на всю покупку')
        print('6. Сделать наценку на всю покупку 10%')
        print('7. Выход')
        print('-' * 110)
        n = input('Введите номер задачи: ')
        print()
        if n=='1':
            print('-' * 110)
            print('|{:^5}|{:^20}|{:^20}|{:^20}|{:^20}|{:20}|'.format('Номер', 'Наименование', 'Штрих-код',
                                                                     'Цена', 'Цвет', 'Производство'))
            print('-' * 110)
            viewing(lst_prod, read)
            print('-' * 110)
        elif n == '2':
            buyer = input('Введите данные(ФИ): ')
            date = input('Укажите дату покупки: ')
            print('-' * 110)
            print('|{:^5}|{:^20}|{:^20}|{:^20}|{:^20}|{:20}|'.format('Номер', 'Наименование', 'Штрих-код',
                                                                     'Цена', 'Цвет', 'Производство'))
            print('-' * 110)
            viewing(lst_prod, read)
            print('-' * 110)
            lst = []
            buy_goods = []
            goods = input('Введите номер товара(-ов), который хотите приобрести (через пробел): ')
            for i in goods.split():
                lst.append(int(i))
            lst_prod = []
            lst_basket = []
            read(lst_prod)
            count = 0
            for i in lst_prod:
                for j in lst:
                    if int(i.get_num()) == j:
                        count += 1
                        buy_goods.append(count)
                        buy_goods.append(i.name)
                        buy_goods.append(i.price)
                        lst_basket.append(buy_goods)
            s = lst_basket[0]
            basket = [s[i:i + 3] for i in range(0, len(s), 3)]
            total = 0
            for i in basket:
                order = Basket(i, buyer, date, total)
                order.buy()
            if len(basket) ==0:
                print('Заказ не произведен! Попробйуте еще раз.')
            else:
                print('Товар добавлен в корзину.')
        elif n == '3':
            print('-' * 110)
            print('Ваша корзина')
            print('-' * 110)
            print('|{:^4}|{:^25}|{:^15}|{:^25}|{:^10}|'.format('№', 'Покупатель', 'Дата ', 'Товар', 'Цена'))
            total = 0
            for i in basket:
                order = Basket(i, buyer, date, total)
                total = order.buy()
                print(order)
            print('Итого покупка на сумму:', total, 'руб.')
        elif n == '4':
            delete = int(input('Выберите номер позиции удаляемого товара: '))
            total = 0
            for i in basket:
                order = Basket(i, buyer, date, total)
                if int(order.count) == delete:
                    basket.remove(i)
            print('Товар удален.')
        elif n == '5':
            total = 0
            for i in basket:
                order = Basket(i, buyer, date, total)
                total = order.buy()
                new_total = order.down()
                print(order)
            print('Итого покупка на сумму (со скидкой):', new_total, 'руб.')
        elif n == '6':
            total = 0
            for i in basket:
                order = Basket(i, buyer, date, total)
                total = order.buy()
                new_total = order.pr_up()
                print(order)
            print('Итого новая стоимость:', new_total, 'руб.')
        elif n == '7':
            print('Программа завершена!')
            return False
        else:
            print('Нет такой задачи. Попробуйте еще раз!')

if __name__=="__main__":
    main()