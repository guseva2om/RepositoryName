# TODO Найдите количество книг, которое можно разместить на дискете
kolstr = 100
chisl = 50
kolsim = 25
kod = 4
raz = 1.44
a = kolstr * chisl * kolsim * kod / 1024 ** 2
it = round(raz / a)


print("Количество книг, помещающихся на дискету:", it)
