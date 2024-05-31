import yfinance

vix = yfinance.Ticker("^VIX")

print(vix.options)

first_expire = vix.options[0]
print(vix.option_chain(first_expire))
