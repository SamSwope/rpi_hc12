<?php
header('context-type: text/json');
$db=new SQLite3('/home/pi/rpi_hc12/db/3W.db');
$statement=$db->prepare("select * from data");
$result=$statement->execute();
while ($row = $result->fetchArray()) {
    $data['data1'][]=['t' => $row[0] . " " . $row[1], 'y' => $row[2]];
    $data['data2'][]=['t' => $row[0] . " " . $row[1], 'y' => $row[3]];
    $data['data3'][]=['t' => $row[0] . " " . $row[1], 'y' => $row[4]];
    $data['data4'][]=['t' => $row[0] . " " . $row[1], 'y' => $row[5]];
    $data['data5'][]=['t' => $row[0] . " " . $row[1], 'y' => $row[6]];
}
echo json_encode($data);
$db->close();
?>
