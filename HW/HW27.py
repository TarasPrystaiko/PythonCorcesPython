def list_item_generator(lst, iter_num=None):
    if iter_num is None:
        while True:
            yield from lst
    else:
        for _ in range(iter_num):
            yield from lst

lst = ['a', 'b']
for i in list_item_generator(lst, iter_num=2):
    print(i)
