CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part8`()
BEGIN
	SELECT *
	FROM user
	WHERE username IN
		(SELECT r1.user_reviewed
		FROM
			(SELECT user_reviewed, count(*) as totalCount
			FROM review
			GROUP BY user_reviewed) as r1
		INNER JOIN
			(SELECT user_reviewed, count(*) as poorCount
			FROM review
			WHERE rating = 'poor'
			GROUP BY user_reviewed
			HAVING count(*)) as r2
		ON r1.user_reviewed = r2.user_reviewed
		WHERE totalCount = poorCount);
END