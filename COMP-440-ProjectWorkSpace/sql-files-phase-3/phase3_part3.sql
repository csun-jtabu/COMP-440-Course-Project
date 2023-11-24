CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part3`(
	userName VARCHAR(15))
BEGIN
	SELECT *
	FROM item i3
	WHERE i3.productid IN (SELECT i.productid
		FROM item i INNER JOIN review r
		ON i.productid = r.productid
		WHERE (i.user_inserted = userName) 
		AND NOT (r.rating = 'poor' OR r.rating = 'fair') 
		AND (i.productid NOT IN
				(SELECT i2.productid
			FROM item i2 INNER JOIN review r2
			ON i2.productid = r2.productid
			WHERE (i2.user_inserted = userName) AND (r2.rating = 'poor' OR r2.rating = 'fair')
			GROUP BY i2.productid))
			GROUP BY i.productid);
END