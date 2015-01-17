stock = {
	'GOOG': 520.42,
	'FB': 76.45,
	'YHOO': 39.28,
	'T': 34
	}

print(min(zip(stock.values(), stock.keys())))
print(sorted(zip(stock.values(), stock.keys())))
print(sorted(zip(stock.keys(),stock.values())))
