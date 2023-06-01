#
#<?php die('Forbidden.'); ?>
#Date: 2023-06-01 09:26:03 UTC
#Software: Joomla! 4.3.1 Stable [ Bora ] 2-May-2023 16:00 GMT

#Fields: datetime	priority clientip	category	message
2023-06-01T09:26:03+00:00	INFO ::1	update	Update started by user admin (621). Old version is 4.3.1.
2023-06-01T09:26:05+00:00	INFO ::1	update	Downloading update file from https://s3-us-west-2.amazonaws.com/joomla-official-downloads/joomladownloads/joomla4/Joomla_4.3.2-Stable-Update_Package.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA6LXDJLNUINX2AVMH%2F20230601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230601T092550Z&X-Amz-Expires=60&X-Amz-SignedHeaders=host&X-Amz-Signature=7bc01f1ce1390b454b399979f46b7db930e8bcb6a00f69c903276b0665a650f2.
2023-06-01T09:26:12+00:00	INFO ::1	update	File Joomla_4.3.2-Stable-Update_Package.zip downloaded.
2023-06-01T09:26:12+00:00	INFO ::1	update	Starting installation of new version.
2023-06-01T09:26:35+00:00	INFO ::1	update	Finalising installation.
2023-06-01T09:26:35+00:00	INFO ::1	update	Start of SQL updates.
2023-06-01T09:26:35+00:00	INFO ::1	update	The current database version (schema) is 4.3.0-2023-03-29.
2023-06-01T09:26:35+00:00	INFO ::1	update	Ran query from file 4.3.2-2023-03-31. Query text: UPDATE `#__guidedtour_steps` SET `title` = 'COM_GUIDEDTOURS_TOUR_BANNERS_STEP_DE.
2023-06-01T09:26:35+00:00	INFO ::1	update	Ran query from file 4.3.2-2023-05-03. Query text: UPDATE `#__extensions`    SET `params` = '{"template_positions_display":"0","upl.
2023-06-01T09:26:35+00:00	INFO ::1	update	Ran query from file 4.3.2-2023-05-20. Query text: ALTER TABLE `#__user_mfa` ADD COLUMN `tries` int NOT NULL DEFAULT 0 ;.
2023-06-01T09:26:35+00:00	INFO ::1	update	Ran query from file 4.3.2-2023-05-20. Query text: ALTER TABLE `#__user_mfa` ADD COLUMN `last_try` datetime ;.
2023-06-01T09:26:35+00:00	INFO ::1	update	End of SQL updates.
2023-06-01T09:26:35+00:00	INFO ::1	update	Deleting removed files and folders.
2023-06-01T09:26:37+00:00	INFO ::1	update	Cleaning up after installation.
2023-06-01T09:26:37+00:00	INFO ::1	update	Update to version 4.3.2 is complete.
