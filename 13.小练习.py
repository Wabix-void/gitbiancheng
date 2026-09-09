name = "公司"
stock_price = 12.33
stock_code = "003032"
stock_price_daily_growth_factor = 1.1
growth_days = 19
print("""公司：%s，股票代码：%s，当前股价：%f
每日增长系数是：%f，经过%d天的增长后，股价达到了：%f"""%(name,stock_code,stock_price,stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
#出现问题：股票复利上涨，用幂函数**，不是直接乘*