
#CHAT GPT: 
# product_prices = {
#     1: 4,
#     2: 4.50,
#     3: 5,
#     4: 2,
#     5: 1.50
# }

# product = int(input("Informe o número do produto: "))
# quantity = int(input("Informe a quantidade: "))

# if product in product_prices:
#     total = quantity * product_prices[product]
#     print('Total: R$ %.2f' % total)
# else:
#     print("Produto não encontrado.")


# Product = int(input(),10)
# Quantity = int(input(),10)

Product, Quantity = input().split()
Product = int(Product)
Quantity = int(Quantity)

TOTAL = 0

if Product == 1:
    TOTAL = Quantity * 4
elif Product == 2:
    TOTAL = Quantity * 4.50
elif Product == 3:
    TOTAL = Quantity * 5
elif Product == 4:
    TOTAL = Quantity * 2
elif Product == 5:
    TOTAL = Quantity * 1.50

print('Total: R$ %.2f' %TOTAL)


