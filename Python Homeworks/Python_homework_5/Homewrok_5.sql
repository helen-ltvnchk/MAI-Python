-- 1
SELECT product_name
FROM products
WHERE unit_price BETWEEN 3 AND 6;

-- 2
SELECT MIN(unit_price) AS min_price
FROM products
WHERE category_id = 1;

-- 3
SELECT supplier_id, MAX(unit_price) AS max_price
FROM products
WHERE supplier_id IN (1, 3, 5)
GROUP BY supplier_id
ORDER BY supplier_id;