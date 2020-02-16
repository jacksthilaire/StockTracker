import bs4
import time
from urllib import request
import DBManage


def find_data(stock):
    # takes a stock ticker and scrapes data from yahoo finance

    # request to open yahoo finance page, with extension of stock ticker
    r = request.urlopen("https://finance.yahoo.com/quote/" + stock)

    # open a BS html parser, with the requested URL
    soup = bs4.BeautifulSoup(r, "html.parser")

    # find stockprice, percent change, close/open, pe, eps, 52 week range
    try:
        stockprice = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        percent = soup.find_all('span', {'class': 'Trsdu(0.3s)'})[1].text
        prevclose = soup.find_all('span', {'class': 'Trsdu(0.3s)'})[2].text
        openprice = soup.find_all('span', {'class': 'Trsdu(0.3s)'})[3].text
        fiftytwo = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'}).text
        peratio = soup.find_all('td', {'data-test': 'PE_RATIO-value'})[0].find('span').text
        eps = soup.find_all('td', {'data-test': 'EPS_RATIO-value'})[0].find('span').text
    except:
        print("Unable to obtain stock price, ticker may be incorrect.")
        stockprice = "0.0"
        percent = "0.0"
        prevclose = "0.0"
        openprice = "0.0"
        fiftytwo = "0.0"
        peratio = "0.0"
        eps = "0.0"

    # print all of the data retreived
    print("*--------------------*")
    print(stock)
    print("Price: " + stockprice)
    print("Change: " + percent)
    print("Previous Close: " + prevclose)
    print("Open: " + openprice)
    print("52 Week Range: " + fiftytwo)
    print("PE Ratio: " + peratio)
    print("EPS: " + eps)
    print("*--------------------*")


# main program loop
while True:
    # give the user a choice to view the current list, and see all of the data, or edit the stock list
    choice = input("'V': view stock list, 'E': edit stock list")

    # view list, retreive from DB, and find data if not null
    if choice == 'V':
        stock_list = DBManage.retrieveDB()
        for stock in stock_list:
            if stock != "":
                find_data(stock)

    # edit stock list, show the current list then allow an add or deletion
    elif choice == 'E':
        stock_list = DBManage.retrieveDB()
        print("Current list: ")
        for stock in stock_list:
            if stock != "":
                print(stock)
        addrem = input("Add or remove: 'A' or 'R'")
        if addrem == 'A':
            ticker = input("Enter ticker to add: ")
            DBManage.addDB(ticker)
        elif addrem == 'R':
            ticker = input("Enter ticker to delete: ")
            DBManage.delDB(ticker)
        else:
            print("Error, option not available")
