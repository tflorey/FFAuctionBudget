# author: Trent Florey
# 07/11/21
# interpret fantasy football data to improve
# auction draft spending this fall
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# create a webdriver and make sure it is up to date
options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options,)

def main():
    # only positions we care about are these 4 (only ones rosterd in my league)
    positions = ["QB", "RB", "WR", "TE"]
    # this information is used for web scraping the preSeason projections
    positionIterationMap = {
        "QB": 3,
        "RB": 4,
        "WR": 6,
        "TE": 3
    }
    # these are the total expected number of rostered players by position
    # group in my league
    numberRosteredMap = {
        "QB": 30,
        "RB": 52,
        "WR": 84,
        "TE": 36
    }
    # these are the years for which I want to compare predictions and results
    years = [year for year in range(2011, 2021)]
    # scrape all the players' names with index being their projected ranking
    # for each position each year
    playerNames = [[[] for position in positions] for year in years]
    # loop through each year, each position group within each year and iteration
    # has to do with the way the website stores the rankings (only has 10 per page
    # in some cases) but we have a number we want to reach based on numberRosteredMap
    for yearIndex in range(len(years)):
        for positionIndex in range(len(positions)):
            for iteration in range(1, positionIterationMap.get(positions[positionIndex]) + 1):
                url = getPreseasonUrl(years[yearIndex], positions[positionIndex], iteration)
                try:
                    driver.get(url)
                    getPlayerNames(playerNames[yearIndex][positionIndex], numberRosteredMap.get(positions[positionIndex]))
                except:
                    continue

def getPreseasonUrl(season, position, iteration):
    # url naming convention for each position
    positionIdMap = {
        "QB": "quarterbacks",
        "RB": "runningbacks",
        "TE": "tightends",
        "WR": "widereceivers"
    }
    positionId = positionIdMap.get(position)
    if iteration > 1:
        url = "https://www.walterfootball.com/fantasy{}{}_{}.php".format(season, positionId, iteration)
    else:
        url = "https://www.walterfootball.com/fantasy{}{}.php".format(season, positionId)

    return url

def getPlayerNames(playerNames, maxLength):
    players = driver.find_elements_by_xpath("//div[@id='MainContentBlock']/ol/li/b[1]")
    length = len(players)
    index = 0
    count = len(playerNames)

    # we only want a certain number of names based on our numberRosteredMap
    # this is passed in as maxLength so we make sure playerNames does not
    # exceed that size so go until that or if there are fewer names available
    # stop when you run out of names
    while(index < length and count < maxLength):
        text = players[index].text
        # accounts for error where michael vick's name is removed
        if(text == "QB Eagles No. 7, QB, Eagles. Bye: 7."):
            text = "Michael Vick,"
        # format the text to have just the first and last name
        commaIndex = text.index(",")
        playerNames.append(text[0:commaIndex])
        index += 1
        count += 1

main()
driver.close()