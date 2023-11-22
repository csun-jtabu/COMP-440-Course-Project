CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part5`(
	user1 VARCHAR(15), user2 VARCHAR(15))
BEGIN
	SELECT *
	FROM user
	WHERE username IN 
		(SELECT f1.favorited_user
		FROM
			(SELECT *
			FROM favorite
			WHERE username = user1) AS f1
		INNER JOIN
			(SELECT *
			FROM favorite
			WHERE username = user2) AS f2
		ON f1.favorited_user = f2.favorited_user);
END