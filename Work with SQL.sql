CREATE SCHEMA games;
-- Created Schema called 'games' and uploaded the 3 datasets into tables --

SELECT * FROM games_description;

SELECT * FROM games_revenue;

SELECT * FROM games_reviews;

-- Just quick way to view each dataset --

SELECT * FROM games_description LEFT JOIN games_revenue
ON games_description.game_id = games_revenue.game_id;
-- ON operator is table name.column name of the first table = table name.column name of the second table --

SELECT number_of_reviews_from_purchased_people, number_of_purchases, b.game_id FROM games_reviews b LEFT JOIN games_revenue a
ON b.game_id = a.game_id;
-- pulls and shows specific columns from seperate tables using a & b --

-- TASK 3: QUESTION 1 ------------------------------------------------------------------------------------------------------ --
SELECT
    genre,
    Total_Revenue,
    RANK() OVER (ORDER BY Total_Revenue DESC) AS Ranked_revenue
FROM (
    SELECT
        a.genre,
        SUM(b.Number_of_purchases * b.Unit_price) AS Total_Revenue
    FROM games_revenue b
    JOIN games_description a
        ON a.game_id = b.game_id
    GROUP BY a.genre
) t
ORDER BY Total_Revenue DESC;

-- TASK 3: QUESTION 2 ------------------------------------------------------------------------------------------------------ --
SELECT
	ROUND(SUM(number_of_reviews_from_purchased_people) / SUM(number_of_purchases) * 100, 1) AS percentage_of_customers_who_left_a_review
FROM 
	games_reviews b 
JOIN
	games_revenue a
ON
	b.game_id = a.game_id;

-- Question: Out of the total purchases, what percentage of customers left a review --
-- Answer: 63.8%

SELECT a.game_id, a.game_name, b.number_of_english_reviews, b.number_of_reviews_from_purchased_people FROM games_reviews b LEFT JOIN games_description a
ON b.game_id = a.game_id;
-- ^ this just shows the columns to be used --

-- Task 3: QUESTION 3 ------------------------------------------------------------------------------------------------------ --

SELECT 
	a.game_id, a.game_name, b.number_of_english_reviews, b.number_of_reviews_from_purchased_people,
	ROUND((number_of_english_reviews /  number_of_reviews_from_purchased_people) * 100, 1)
AS
	percentage_english_purchased
FROM
	games_reviews b 
JOIN
	games_description a ON b.game_id = a.game_id
    
ORDER BY 
	percentage_english_purchased DESC;
    
-- 29 games had 40% english reviews but the most frequent instances were 50% and 60% where both had 50 games with their percentage of english reviews --
-- There are a total of 10 games where the number of english reviews is greater than the number of reviews from purchased people --

-- Question: Out of the total number of reviews written for each game, what percentage are written in english? --
-- game_name, number_of_english_reviews, game_id --

-- Task 3 - QUESTION 4 ------------------------------------------------------------------------------------------------------ --

SELECT 
	a.genre,
    SUM(b.Number_of_purchases*b.Unit_price) AS Total_Revenue
FROM 
	games_revenue b
JOIN 
	games_description a ON a.game_id = b.game_id
GROUP BY 
	a.genre
ORDER BY
	Total_Revenue DESC;

-- Task 4 - Part one ------------------------------------------------------------------------------------------------------ --

SELECT 
	game_id, game_name, genre, total_revenue,
RANK() OVER (PARTITION BY genre ORDER BY Total_Revenue DESC) AS revenue_ranking_by_genre
FROM(
SELECT 
	a.game_name, a.game_id, a.genre,
    SUM(b.Number_of_purchases*b.Unit_price) AS Total_Revenue
FROM 
	games_revenue b
JOIN 
	games_description a ON a.game_id = b.game_id
GROUP BY 
	a.game_name, a.game_id, a.genre
ORDER BY
	Total_Revenue DESC
) t ORDER BY revenue_ranking_by_genre AND genre DESC;

-- Task 4 - Part two ------------------------------------------------------------------------------------------------------ --

SELECT a.game_id, a.game_name, b.number_of_reviews_from_purchased_people, a.genre,
RANK() OVER (PARTITION BY genre ORDER BY number_of_reviews_from_purchased_people DESC) AS review_ranking_by_genre
FROM 
	games_reviews b
JOIN 
	games_description a ON a.game_id = b.game_id
GROUP BY 
	a.game_name, a.game_id, b.number_of_reviews_from_purchased_people, a.genre
ORDER BY
	number_of_reviews_from_purchased_people AND genre DESC;
