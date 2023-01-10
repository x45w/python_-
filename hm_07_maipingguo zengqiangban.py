
price_str=input("苹果单价:")

weight_str=input("苹果重量:")

# 注意：两个字符串变量之间是不能直接用乘法的。
#money=price_str*weight_str

# 价格，重量转换成小数
price=float(price_str)
weight=float(weight_str)

money=price * weight

print(money)