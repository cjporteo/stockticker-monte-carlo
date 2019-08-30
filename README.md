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
![](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-9/69456433_592841787913987_7051997083514961920_n.jpg?_nc_cat=107&_nc_oc=AQmtfxUNqj0fThe3PEpIDge78NOU4xI6HMUHWqU7BusgiuhENHfRjhuZRh42ey-Ky2E&_nc_ht=scontent-yyz1-1.xx&oh=6faf8f223afc6c56335943fe0212e414&oe=5E1217D3)
<br>
![](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-9/69257246_951981681829466_2498932949156626432_n.jpg?_nc_cat=102&_nc_oc=AQlpqqOmFhGLuvxrYW3KClfDaEwWrQ_sclRmsT3X2ZUFBBA52jlxjDQ7Egg0EUq_BpM&_nc_ht=scontent-yyz1-1.xx&oh=189be0dccf7d26a9a3e27f049dbd70c1&oe=5E13E420)
<br>
## Details
- a maximum of 1M simulations are allowed per execution for runtime purposes; this can be modified in lines ``12`` and ``13`` of the code
- completed simulations are serialized as *pickles* in local storage for future recall
- the limit for number of stored simulations is set around 12M; this can be modified in line ``24`` of the code
