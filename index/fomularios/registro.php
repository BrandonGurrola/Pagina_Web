<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user</title>
</head>
<body>
    <?php

        include("db.php");
        $tbl_name = "datos";
        $nombres = $_POST['nombres'];
        $apellidos = $_POST['apellidos'];
        $correo = $_POST['correo'];
        $password = $_POST['password'];

        $sql = "INSERT INTO $tbl_name (nombres,apellidos,correo,password)
         VALUES ('$nombres','$apellidos','$correo','$password')";
        if(mysqli_query($conexion, $sql)){
        } else {
          echo "Error: " . $sql . "<br>" . mysqli_error($conexion);
        }
        //Cerrar Base de Datos//
        mysqli_close($conexion); 
    ?>
    
</body>
</html>