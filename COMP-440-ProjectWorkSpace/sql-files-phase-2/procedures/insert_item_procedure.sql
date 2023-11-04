CREATE PROCEDURE `insert_item_procedure`(
   userName VARCHAR(15), title VARCHAR(50), description VARCHAR(255), category VARCHAR(255), price INT
)
BEGIN
    IF ((SELECT count(*) from `item` WHERE `user_inserted` = userName and `date_inserted` = current_date()) < 3) THEN 
        INSERT INTO `item`(`productid`, `user_inserted`, `title`, `description`, `category`, `price`, `date_inserted`) 
            VALUES (default, userName, title, description, category, price, current_date());
    ELSE 
       SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'You reached the max number of item inserts for today. Please try tomorrow.';
    END IF;
END