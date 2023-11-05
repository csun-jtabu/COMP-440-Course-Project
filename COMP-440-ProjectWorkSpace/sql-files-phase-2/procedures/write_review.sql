CREATE DEFINER=`root`@`localhost` PROCEDURE `write_review`(
	productid INT, userName VARCHAR(15), rating VARCHAR(15), description VARCHAR(255)
	)
BEGIN
	IF ((SELECT count(*) FROM `review` WHERE `user_reviewed` = userName and `date_reviewed` = current_date()) < 3) THEN
		INSERT INTO `review`(`productid`, `user_reviewed`, `rating`, `description`, `date_reviewed`)
			VALUES (productid, userName, rating, description, current_date());
	ELSE
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'You have reached the maximum number of reviews for today. Please try again tomorrow.';
	END IF;
END