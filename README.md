# FFAuctionBudget
## What is this project?
This project web scrapes data from the past 10 NFL seasons (2011-2020) to gather preseason rankings and compare that with regular season production, effectively mapping ranking to points produced. It then performs calculations to determine value using a points above replacement approach and divides by the total available money in our auction draft to determine the value that should have been spent on each position group. These results are then averaged into one 2D array that holds a list for each of the 4 position groups that we use in our league (QB, RB, WR, TE) up to the number of each that is expected to be rostered, determining the average that should have been spent on each preseason ranking (i.e. the first index in the QB list is the average value of the QB's that were considered the top fantasy QB's before the season began for each of the past 10 years, second index is the average of the second ranked prospects, etc.). The results are displayed in an excel sheet for ease of use on draft day.
## Why did I make this?
I have always been curious throughout my years of doing fantasy football auction drafts as to how value was determined for players and why running backs went for so much more than quarterbacks or tight ends. I wanted to have data that proved to me how much players were truly worth, and this has provided exactly that. Further, my fantasy football league has different rules and a different roster configuration than most, so I believed the values assigned to players on sites like ESPN or NFL.com for auction drafts might be misleading for my league.
## What did I find?
In fantasy football, running backs have been long thought to be the most valuable players because there are few that get a high level of volume in terms of carries, receptions, snaps, etc. However, because my league is a 2 QB league (meaning you must play 2 QB's each week rather than the standard 1 QB league), the value of the QB increases dramatically. The same is true at the TE position. Although I believed this to be true already because it makes sense logically, it was hard for me to quantify how much quarterbacks were actually worth, so this project gives me a clear understanding that they are significantly more valuable than running backs or wide receivers, and have been undervalued in our league.
## How do you run this project?
To run this project, make sure you have Python installed and download the FFAuction.py file from this repo. Next make sure you have the selenium and openpyxl dependencies installed. Once you have all the dependencies installed, open a terminal and type: "python FFAuction.py" and that will run the web scraper. The process does take a while (it took about 20 min for me) because it is a lot of data to gather, but once it is done it will export that to an excel sheet, and you can verify against the results from the excel sheet seen in the repo.
## What are the limitations of this project?
The way that value is calculated could be debated to some extent because although many players are rostered, the only players that produce value for your team are the ones you start. Further, there is some strategy surrounding picking suspended players because they may miss 4 or 8 games but have a very high points per game. Because this project only accounts for season totals, it does not provide a clear strategy for that edge case. Additionally, some may argue that it is worth spending more money for players that you are highly confident will produce because they are much easier to predict and there is merit to that argument as well, but it is very tough to quantify that and therefore was not taken into account here.