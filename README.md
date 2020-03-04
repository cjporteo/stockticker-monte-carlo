# Stock Ticker Monte Carlo Simulation
## About
A Python script to apply Monte Carlo simulation the board game *Stock Ticker*.
My published Medium article on this project can be found [here](https://medium.com/@cjporteo/cracking-an-82-year-old-stock-trading-board-game-using-monte-carlo-simulation-384c26eeff6c).
## Installation and Usage
To install:

``$ git clone https://github.com/cjporteo/stockticker-monte-carlo``

The **config.ini** file contains the parameters for the simulation: amount of cash, number of players, and number of rounds. After configuring, run the script with the following command:

``$ python stockticker.py``

Results will be displayed (textually and graphically) after the simulation finishes.
<br>
### Output Explanation

 - **S** = initial stock price
 - **n** = number of simulations
 - **D** = dividend yield
 - **H** = value of final holdings
 - **P** = D + H - inital cash = profit
## Details
- a maximum of 1M simulations are allowed per execution for runtime purposes; this can be modified in lines ``12`` and ``13`` of the code
- completed simulations are serialized as *pickles* in local storage for future recall
- the limit for number of stored simulations is set around 12M; this can be modified in line ``24`` of the code
