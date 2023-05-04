from bs4 import BeautifulSoup
import Card as c

cardName = ""

uriDefault = "https://gatherer.wizards.com/Pages/Default.aspx"
urlSearch = "?name=+[{cn}]".format(cn=cardName)

if __name__ == "__main__":
    testCard = c.Card(1,2,3,4,5,6,7,8,9)
    testCard.Print_Stuff()