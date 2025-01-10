CREATE VIEW pizza_schema.view_orders_summary AS
SELECT o.order_id, c.name AS customer_name, o.total_price
FROM pizza_schema.orders o
JOIN pizza_schema.customers c ON o.customer_id = c.customer_id;

CREATE VIEW pizza_schema.view_employee_orders AS
SELECT e.name AS employee_name, COUNT(o.order_id) AS orders_count
FROM pizza_schema.employees e
LEFT JOIN pizza_schema.orders o ON e.employee_id = o.employee_id
GROUP BY e.name;

CREATE VIEW pizza_schema.view_pizza_prices AS
SELECT MIN(price) AS min_price, MAX(price) AS max_price
FROM pizza_schema.pizzas;