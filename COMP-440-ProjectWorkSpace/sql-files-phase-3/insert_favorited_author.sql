CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_favorited_author`(
	user VARCHAR(15), favorited VARCHAR(15))
BEGIN
	IF (NOT EXISTS (SELECT username FROM favorite WHERE username = user AND favorited_user = favorited)) THEN
		INSERT INTO favorite(username, favorited_user)
			VALUES (user, favorited);
	ELSE
		SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'You unfavorited the author';
	END IF;
END