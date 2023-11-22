CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_favorited_author`(
	user VARCHAR(15), favorited VARCHAR(15))
BEGIN
	IF (EXISTS (SELECT username FROM favorite WHERE username = user AND favorited_user = favorited)) THEN
		DELETE FROM favorite WHERE username = user AND favorited_user = favorited;
	END IF;
END