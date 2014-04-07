###Pseudo code for "Walmart Recruiting - Store Sales Forecasting"

"" 

1. Read data into dataframe
2. Merge data using joins "Store - Date", "Store"
3. Run mulitvariable regression determining feature significance
4. Once features determined, setup loop to do time-series model store-by-store
5. Predict Sales by time - store-by-store
6. Setup loop to do time-series model by Dept
7. Predict Sales by time - by Dept