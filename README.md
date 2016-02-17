# GCX-Python-Client
Python client for connecting to the GCX API 

Using the Python GCX Bindings you can connect to GCX and view your balance, place trades or email/sms Gold Grams.

More information/documentation can be found on https://gcx.io/api/


Login
```
from gcx import gcx
gcx = gcx()
trader_id = gcx.login("username","password")[0]["trader_id"]
```

Get balance
```
gcx.getbalance(trader_id)
```

Get bids
```
gcx.getbids()
```

Get asks
```
gcx.getasks()
```

Get orders
```
gcx.getorders(trader_id)
```

Cancel order
```
gcx.cancelorder(oid)
```

Withdraw fiat
```
gcx.withdrawfiat(trader_id,amount)
```

Place trade to buy/sell Gold
```
gcx.trade(trader_id,shares,price,bidask,order)
```

Email gold
```
gcx.emailgold(trader_id,recipientemail,amount)
```
SMS Gold
```
gcx.smsgold(trader_id,recipientmobile,amount)
```



