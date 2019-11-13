<?php
$x = 0;
$prev_number = 1;
$range_number = 100000;
while ($x < $range_number) {
    if ($x % 3 == 0) {
      echo $x % 5 == 0 ? 'Maria Health' : 'Maria';
    } else if ($x % 5 == 0) {
      echo 'Health';
    } else {
      echo $x;
    }
    $x = ($x + $prev_number);
    $prev_number = ($x - $prev_number);
    echo '<br />';
}
?>