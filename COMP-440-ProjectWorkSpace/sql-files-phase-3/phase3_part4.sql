CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part4`(
	dateToSearch DATE)
BEGIN
	SELECT u.username, u.password, u.firstName, u.lastName, u.email, count(*)
	FROM item i2 LEFT JOIN user u
	ON i2.user_inserted = u.username
	WHERE i2.date_inserted = dateToSearch
	GROUP BY i2.user_inserted
	HAVING count(*) = 
		(SELECT MAX(total) FROM
			(SELECT count(*) as total
			FROM item i
			WHERE i.date_inserted = dateToSearch
			GROUP BY i.user_inserted) 
		AS totalFromEach);
END