# x = 0
# while x < 4:
#     print(x)
#     x += 1
#
# print('\n')
# for x in range(2, 7):
#     print(x)


months = ['jan', 'feb', 'mar']
for m in months:
    print(m)
    for x in range(10, 20):
        # if x == 15:
        #     break
        if x % 5 == 0:
            continue
        print(x)

