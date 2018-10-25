# Homework 7

Create class representing money in different currencies. It has to support the following operations:

```python
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z +  3.11*x + y*0.8) # result in “EUR”
>>543.21 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]

s = sum(lst)

print(s) #result in “BYN”
>>123.45 BYN
```

(Optional): Get the latest exchange rates from any free API. For example, https://currencylayer.com/

