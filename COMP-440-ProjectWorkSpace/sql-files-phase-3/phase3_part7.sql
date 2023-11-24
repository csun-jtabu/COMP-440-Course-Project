CREATE PROCEDURE `phase3_part7` ()
BEGIN
	SELECT *
	FROM user
	WHERE username NOT IN
		(SELECT DISTINCT user_reviewed
		FROM review
		WHERE rating = 'poor');
END
