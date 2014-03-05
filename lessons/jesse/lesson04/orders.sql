#orders.sql
-- What customers are from the UK
SELECT * FROM Customers WHERE Country='UK';

-- What is the name of the customer who has the most orders?
SELECT Customers.CustomerName, COUNT(*) FROM Customers
JOIN Orders ON (Customers.CustomerID = Orders.CustomerID)
Group by Customers.CustomerName
ORDER BY COUNT(Orders.OrderID) DESC Limit 1;


-- What supplier has the highest average product price?
SELECT Suppliers.*, AVG(Products.Price) AS AverageProdPrice FROM Products
JOIN Suppliers ON (Products.SupplierID = Suppliers.SupplierID)
Group by Suppliers.SupplierName 
ORDER BY AverageProdPrice DESC Limit 1;


-- What category has the most orders?
SELECT Categories.CategoryName, COUNT(*) FROM Categories
JOIN Products ON (Products.CategoryID = Categories.CategoryID)
JOIN OrderDetails ON (OrderDetails.ProductID = Products.ProductID)
JOIN Orders ON (Orders.OrderID = OrderDetails.OrderID)
Group by Categories.CategoryName
ORDER BY Count(Orders.ProductID) DESC Limit 1;


-- What employee made the most sales (by number of sales)?
SELECT Employees.FirstName, Employees.LastName, SUM(OrderDetails.Quantity) FROM Employees
JOIN Orders ON (Orders.EmployeeID = Employees.EmployeeID)
JOIN OrderDetails On (OrderDetails.OrderID = Orders.OrderID)
Group by Employees.FirstName, Employees.LastName
Order by SUM(OrderDetails.Quantity) DESC Limit 1;


-- What employee made the most sales (by value of sales)?
SELECT Employees.FirstName, Employees.LastName, SUM(OrderDetails.Quantity * Products.Price) AS TotalValue FROM Employees
JOIN Orders ON (Orders.EmployeeID = Employees.EmployeeID)
JOIN OrderDetails On (OrderDetails.OrderID = Orders.OrderID)
JOIN Products ON (Products.ProductID = OrderDetails.ProductID)
Group by Employees.FirstName, Employees.LastName
Order by TotalValue DESC Limit 1;

-- What employees have BS degrees? (Hint: Look at LIKE operator)
SELECT * FROM Employees
WHERE Employees.Notes Like '%BS%';


-- What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)
SELECT Suppliers.SupplierName, AVG(Products.Price) AS AverageProdPrice FROM Suppliers
JOIN Products ON (Products.SupplierID = Suppliers.SupplierID)
Group by Suppliers.SupplierID
HAVING COUNT(Products.ProductID) > 2
ORDER BY AverageProdPrice DESC Limit 1;

