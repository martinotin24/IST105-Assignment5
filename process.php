<?php
$command = escapeshellcmd("python3 process.py");
$output = shell_exec($command);
echo $output;
?>
