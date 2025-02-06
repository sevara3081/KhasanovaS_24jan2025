-- Очистка данных перед вставкой новых
DELETE FROM Nutritional_Information;
DELETE FROM Products;
DELETE FROM Categories;

-- Создание таблицы категорий
CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT
);

-- Создание таблицы продуктов
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category_id INTEGER,
    calories INTEGER,
    price DECIMAL(10,2),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Создание таблицы пищевой ценности
CREATE TABLE IF NOT EXISTS Nutritional_Information (
    product_id INTEGER,
    protein DECIMAL(10,2),
    carbohydrates DECIMAL(10,2),
    fat DECIMAL(10,2),
    fiber DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Вставка тестовых данных в Categories
INSERT INTO Categories (category_id, category_name) VALUES
(1, 'Фрукты'),
(2, 'Овощи'),
(3, 'Мясо'),
(4, 'Молочные продукты');

-- Вставка тестовых данных в Products
INSERT INTO Products (product_id, product_name, category_id, calories, price) VALUES
(1, 'Яблоко', 1, 52, 1.50),
(2, 'Морковь', 2, 41, 0.80),
(3, 'Говядина', 3, 250, 7.90),
(4, 'Молоко', 4, 60, 2.30),
(5, 'Банан', 1, 96, 1.20);

-- Вставка тестовых данных в Nutritional_Information
INSERT INTO Nutritional_Information (product_id, protein, carbohydrates, fat, fiber) VALUES
(1, 0.3, 14, 0.2, 2.4),
(2, 0.9, 10, 0.2, 6.0),
(3, 26, 0, 20, 0),
(4, 3.3, 5, 3.5, 0),
(5, 1.3, 23, 0.3, 2.6);

-- Запрос: Вывести все уникальные названия продуктов
SELECT DISTINCT product_name FROM Products;

-- Запрос: Вывести id, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов
SELECT P.product_id, P.product_name, P.price
FROM Products P
JOIN Nutritional_Information N ON P.product_id = N.product_id
WHERE N.fiber > 5;

-- Запрос: Вывести название продукта с самым высоким содержанием белка (protein)
SELECT P.product_name
FROM Products P
JOIN Nutritional_Information N ON P.product_id = N.product_id
ORDER BY N.protein DESC
LIMIT 1;

-- Запрос: Подсчитать общую сумму калорий для продуктов каждой категории (исключая продукты с нулевым жиром)
SELECT P.category_id, SUM(P.calories) AS total_calories
FROM Products P
JOIN Nutritional_Information N ON P.product_id = N.product_id
WHERE N.fat > 0
GROUP BY P.category_id;

-- Запрос: Рассчитать среднюю цену товаров каждой категории
SELECT C.category_name, AVG(P.price) AS avg_price
FROM Products P
JOIN Categories C ON P.category_id = C.category_id
GROUP BY C.category_name;