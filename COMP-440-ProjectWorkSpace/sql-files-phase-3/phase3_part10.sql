CREATE DEFINER=`root`@`localhost` PROCEDURE `phase3_part10`()
BEGIN
	(SELECT *
	FROM 
		(SELECT distinct t1.user_inserted, t1.user_reviewed
		FROM
			(SELECT i1.productid, i1.user_inserted, r1.user_reviewed, r1.rating
			FROM item i1 INNER JOIN review r1
			ON i1.productid = r1.productid) as t1
		INNER JOIN
			(SELECT i2.productid, r2.user_reviewed, i2.user_inserted, r2.rating
			FROM item i2 INNER JOIN review r2
			ON i2.productid = r2.productid) as t2
		ON (t1.user_inserted = t2.user_reviewed) AND (t1.user_reviewed = t2.user_inserted)
		WHERE t1.rating = 'excellent' AND t2.rating = 'excellent') as newT1
	LEFT JOIN 
		(SELECT distinct t1b.user_inserted, t1b.user_reviewed
		FROM
			(SELECT i1b.productid, i1b.user_inserted, r1b.user_reviewed, r1b.rating
			FROM item i1b INNER JOIN review r1b
			ON i1b.productid = r1b.productid) as t1b
		INNER JOIN
			(SELECT i2b.productid, r2b.user_reviewed, i2b.user_inserted, r2b.rating
			FROM item i2b INNER JOIN review r2b
			ON i2b.productid = r2b.productid) as t2b
		ON (t1b.user_inserted = t2b.user_reviewed) AND (t1b.user_reviewed = t2b.user_inserted)
		WHERE t1b.rating != 'excellent' OR t2b.rating != 'excellent') as newT2
	
    ON (newT1.user_inserted = newT2.user_inserted) AND (newT1.user_reviewed = newT2.user_reviewed)
	WHERE newT2.user_inserted is null);

END