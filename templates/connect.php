<?php
    $FirstName=$_POST['FirstName'];
    $LastName=$_POST['LastName'];
    $Email=$_POST['Email'];
    $number=$_POST['number'];
    $DateofBirth=$_POST['DateofBirth'];
    $Gender=$_POST['Gender'];
    $UserName=$_POST['UserName'];
    $Password=$_POST['Password'];
    $conn= new mysqli('localhost','root','','hostalproject');
    if($conn->connect_error)
    {
        die('Connection Failed : '.$conn->connect_error);
    }
    else
    {
        $stmt=$conn->prepare("insert into registration(FirstName,LastName,Email,number,DateofBirth,Gender,UserName,Password)
        values(?,?,?,?,?,?,?,?)");
        $stmt->bind_param("sssissss",$FirstName,$LastName,$Email,$number,$DateofBirth,$Gender,$UserName,$Password);
        $stmt->execute();
        echo "Registration Successfully....";
        $stmt->close();
        $conn->close();
    }
?>