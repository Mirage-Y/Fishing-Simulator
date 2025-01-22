#** Year 1 **
#Focus this year: salmon
#This year's profit (or loss): $40000
#Total profit (or loss): $40000
import random
#function to print year 
def textyear(n):
    print("** Year", n, "**")
#function used for textfish
def textfish(n):
    fishtype = "Salmon"
    if n %3 == 0:
        fishtype = "Crabs"
    print("Focus this year:", fishtype)
#function used to define profit
def textprofit(n):
    print("Total profit (or loss):", n)
#function used for chance of profit
def textyearprofit(n):
    if n %3 == 0:
        profitchance = random.randint(1,10)
        if profitchance > 6:
            profit = 50000
        else:
            profit = -5000
    else:
        profitchance = random.randint(1,100)
        if profitchance <= 5:
            profit = 100000
        elif profitchance <= 80:
            profit = 40000
        else:
            profit = -10000
    print("This year's profit (or loss)", profit)
    return profit
#function for coding the profit streak
def profitstreak(n):
    if len(n) < 5:
        return False
    for x in range(5):
        if n[-x - 1] < 0:
            return False
    return True
x = 1
totalprofit = 0
profitlist = []
fishing = True
#conditions for what the manager will do
while fishing:
    textyear(x)
    textfish(x)
    profit = textyearprofit(x)
    profitlist.append(profit)
    totalprofit += profit
    textprofit(totalprofit)
    if totalprofit < 0:
        #manager retires if the profit sucks
        print("The total profit is negative at year-end. The manager will close the fishing operation and look for a new career")
        fishing = False
        #manager makes bank and retires
    if totalprofit >= 250000:
        print("Over $250,000 in total profit. The manager happily retires.")
        fishing = False
    if profitstreak(profitlist):
        #manager gets lucky with profit and retires
        print("There are five consecutive years of positive profit. The manager will happily retire.")
        fishing = False
    x += 1
    


