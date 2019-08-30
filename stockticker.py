from random import randint
import pickle
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

settings = [line.rstrip('\n') for line in open("config.ini")]

cash, players, turns_per_round, rounds = [int(settings[i].split("=")[1]) for i in range(4)]

rolls = players * turns_per_round * rounds
simulations = 3000000//rolls if rolls > 0 else 0
simulations = min(simulations, 1000000)

name_id = "{}_{}_".format(cash, rolls)

try:
    dat = pickle.load(open(name_id + "dat.pickle", "rb"))
except FileNotFoundError:
    dat = {}
    for k in range(1, 40):
        dat[5 * k] = [[], [], []]  # [[list of dividend yields], [list of final holding values], [list of D + H - C]]

if len(dat[5][0]) < 300000:
    for h in range(simulations):
        stock_data = []
        for i in range(6):
            start = 5 * randint(1, 39)
            stock_data.append([start, start, cash * 100 / start, 0])  # [start value, curr value, # of shares, divs]

        for _ in range(rolls):

            r1 = randint(0, 2)  # 0: div, 1: up, 2: down
            r2 = randint(0, 5)  # 0: stock1, 1: stock2, ... , 5: stock6
            r3 = randint(0, 2)  # 0: 5, 1: 10, 2: 20

            if r3 == 0:
                num = 5
            elif r3 == 1:
                num = 10
            else:
                num = 20

            if r1 == 0 and stock_data[r2][1] >= 100:
                stock_data[r2][3] += (stock_data[r2][2] * num / 100)
            elif r1 == 1:
                stock_data[r2][1] += num
                if stock_data[r2][1] >= 200:
                    stock_data[r2][1] = 100
                    stock_data[r2][2] *= 2
            elif r1 == 2:
                stock_data[r2][1] -= num
                if stock_data[r2][1] <= 0:
                    stock_data[r2][1] = 100
                    stock_data[r2][2] = 0

        for j in range(6):
            key = stock_data[j][0]
            div = stock_data[j][3]
            hold = stock_data[j][1] * stock_data[j][2] / 100
            dat[key][0].append(div)
            dat[key][1].append(hold)
            dat[key][2].append(div + hold - cash)
else:
    print("SIMULATION THRESHOLD EXCEEDED")

x, y_E, y_SD = [], [], []
plot_left = 5  # 40
plot_right = 195  # 60
#  use the commented views to for a better lens into what's actually happening - remove extremes
n_lst = []

for k in range(1, 40):
    if 5*k in dat:
        n = len(dat[5 * k][0])
        n_lst.append(n)
        if n > 0:
            div_stats = [np.mean(dat[5 * k][0]), np.std(dat[5 * k][0])]
            hold_stats = [np.mean(dat[5 * k][1]), np.std(dat[5 * k][1])]
            profit_stats = [np.mean(dat[5 * k][2]), np.std(dat[5 * k][2])]

            s1 = "${:.2f}".format(div_stats[0])
            s2 = "${:.2f}".format(hold_stats[0])
            s3 = "${:.2f}".format(profit_stats[0])
            s4 = "${:.2f}".format(profit_stats[1])
            print("S = {:<10} n = {:<10} E[D] = {:<10} E[H] = {:<10} E[P] = {:10} SD[P] = {:10}".
                  format(5*k, n, s1, s2, s3, s4))
            if plot_left <= 5*k <= plot_right:
                x.append(5 * k)
                y_E.append(profit_stats[0])
                y_SD.append(profit_stats[1])

    else:
        n_lst.append(0)

out = open(name_id + "dat.pickle", "wb")
pickle.dump(dat, out)
out.close()

fig, ax = plt.subplots()

ax.axvline(100, color='k', ls="dashed", label="Par", zorder=-10)
ax.scatter(x, y_E, color='c', label="Expected Value")
ax.scatter(x, y_SD, color='r', label="Standard Deviation")


ax.legend(loc="upper right")

formatter = tck.FormatStrFormatter("$%.0f")
ax.yaxis.set_major_formatter(formatter)

for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_color('green')

plt.xlabel("Initial Stock Value")
plt.title("~{} Profit Simulations Per Stock Value".format(int(np.mean(n_lst))))

plt.show()
