CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part9`()
BEGIN
	(SELECT DISTINCT t1.username, t1.password, t1.firstName, t1.lastName, t1.email
	FROM
		(SELECT u.username, u.password, u.firstName, u.lastName, u.email
		FROM user u INNER JOIN item i
		ON u.username = i.user_inserted
		INNER JOIN review r
		ON i.productid = r.productid
		WHERE r.rating != 'poor') as t1
	WHERE t1.username NOT IN
			(SELECT u2.username
			FROM user u2 INNER JOIN item i2
			ON u2.username = i2.user_inserted
			INNER JOIN review r2
			ON i2.productid = r2.productid
			WHERE r2.rating = 'poor') 
	);
END