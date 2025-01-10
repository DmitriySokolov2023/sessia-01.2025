UPDATE pizza_schema.customers
SET address = 'ул. Новая, д. 10'
WHERE customer_id = 1;

UPDATE pizza_schema.pizzas
SET price = 700.00
WHERE name = 'Четыре сыра';

UPDATE pizza_schema.employees
SET position = 'Старший менеджер'
WHERE employee_id = 1;