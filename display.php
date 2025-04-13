<?php
// Kiểm tra lệnh shell_exec
$command = escapeshellcmd('python3 process.py');
echo "Lệnh đang được chạy: " . $command . "<br>";  // In ra lệnh
$output = shell_exec($command);
echo"haha";

// Echo kết quả để kiểm tra đầu ra
echo "<pre>" . htmlspecialchars($output) . "</pre>";  // In ra kết quả trả về từ Python

// Chuyển kết quả JSON thành mảng PHP
$data = json_decode($output, true);

// Kiểm tra nếu có dữ liệu và hiển thị
if ($data) {
    echo "<table border='1'>
            <tr>
                <th>MaGV</th>
                <th>HoTenGV</th>
                <th>BoMon</th>
            </tr>";
    
    // Lặp qua dữ liệu và hiển thị trong bảng
    foreach ($data as $row) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['MaGV']) . "</td>";
        echo "<td>" . htmlspecialchars($row['HoTenGV']) . "</td>";
        echo "<td>" . htmlspecialchars($row['BoMon']) . "</td>";
        echo "</tr>";
    }
    echo "</table>";
} else {
    echo "No data found!";
}
?>
