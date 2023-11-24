CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part6`()
BEGIN
	(SELECT *
		FROM user
		WHERE username NOT IN
		(SELECT user_inserted
		FROM item
		WHERE productid IN
			(SELECT productid
			FROM review
			WHERE rating = 'excellent'
			GROUP BY productid
			HAVING count(*) >= 3)
		)
	);
END