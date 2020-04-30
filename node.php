<?php
$truepass = "yourpass";
$password = !empty($_GET['pass']) ? $_GET['pass'] : '0-0';
$fnc = !empty($_GET['func']) ? $_GET['func'] : '0-0';
if($fnc == 1){
if(password == truepass)
{
$addr = $_GET['addr'];
$fp = fopen('data.txt', 'w+');
fwrite($fp, $addr);
fclose($fp);
}
}
if($fnc == 2){
$fp = fopen('data.txt', 'r');
$dat = fread($fp, filesize('data.txt'));
fclose($fp);
echo($dat);
}
?>