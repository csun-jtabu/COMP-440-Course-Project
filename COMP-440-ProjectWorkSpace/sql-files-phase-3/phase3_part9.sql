CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part9`()
BEGIN
	(SELECT *
	FROM user
	WHERE username NOT IN
		(SELECT user_inserted
		FROM item
		WHERE productid IN
			(SELECT productid
			FROM review
			WHERE rating = 'poor')
		)
	);
END