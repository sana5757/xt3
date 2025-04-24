from pyxt.perp import Perp

xt = Perp(host="https://fapi.xt.com", access_key='e4bfaa0a-6445-4a15-85f4-c9e06f6f35dc', secret_key='260ce1c11134556159a79e91a8ff6d874a3e570e')

# دریافت سرمایه حساب فیوچرز
capital = xt.get_account_capital()
print(capital)
