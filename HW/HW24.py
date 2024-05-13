dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan', '10-Dec']
sorted_dates = sorted(dates, key=lambda x: (int(x[:x.index('-')]), x[x.index('-')+1:]))
print(sorted_dates)