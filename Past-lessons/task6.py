print('-' * 30, 'Задание 1', '-' * 30)

my_string = 'By and by, when we got up, we turned over the truck the gang had stole off of the wreck, ' \
            'wreck and found boots, and blankets, and clothes, and all sorts of other things, and a lot of books,' \
            ' and a spyglass, and three boxes of seegars.'
words = dict()
my_string = my_string.lower()
for key in my_string.replace(',', '').replace('.', '').split():
    words[key] = my_string.count(key)
print(words)

print('-' * 30, 'Задание 2', '-' * 30)
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_price(stock: dict, prices: dict):
    sum_pr = 0
    for k, v in stock.items():
        if k in prices.keys():
            sum_pr += prices[k] * v
    return sum_pr


print(total_price(stock, prices))
print('-' * 30, 'Задание 2', '-' * 30)

print([(x, x * x) for x in range(11)])

test_dict = [{f'{x}': x * x} for x in range(11)]
test_dict2 = dict()
for i in test_dict:
    test_dict2.update(i)
print(test_dict2)
