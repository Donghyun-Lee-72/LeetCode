# Write your MySQL query statement below
SELECT stock_name, SUM(gain) - SUM(loss) as capital_gain_loss
FROM
    (SELECT stock_name, SUM(price) as loss
     FROM Stocks
     WHERE operation='Buy'
     GROUP BY stock_name) as loss_table
    NATURAL JOIN
    (SELECT stock_name, SUM(price) as gain
     FROM Stocks
     WHERE operation='Sell'
     GROUP BY stock_name) as gain_table
GROUP BY stock_name