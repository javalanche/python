import urllib

att_url = 'http://real-chart.finance.yahoo.com/table.csv?s=T&d=11&e=29&f=2014&g=d&a=6&b=19&c=1984&ignore=.csv'

def download_stock_data(csv_url):
    response = urllib.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'att.csv'
    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\n")
	
    fx.close()

download_stock_data(att_url)
