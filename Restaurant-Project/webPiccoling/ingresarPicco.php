<?php
    $user = $_POST["usuario"];
    $clave = $_POST["clave"];

    $servurl = "http://192.168.100.3:3001/usuarios/$user/$clave";
    $curl = curl_init($servurl);

    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    curl_close($curl);

    if ($response === false) {
        header("Location:index.html");
        exit(); // Asegúrate de que el script se detenga después de la redirección
    }

    $resp = json_decode($response);

    // Verifica si json_decode devolvió null
    if ($resp === null) {
        header("Location:index.html");
        exit(); // Asegúrate de que el script se detenga después de la redirección
    }

    // Verifica si $resp es un array y tiene elementos
    if (is_array($resp) && count($resp) != 0) {
        session_start();
        $_SESSION["usuario"] = $user;
        if ($user == "admin") { 
            header("Location:adminPicco.php");
        } else { 
            header("Location:usuarioPicco.php");
        }
    } else {
        header("Location:index.html");
        exit(); // Asegúrate de que el script se detenga después de la redirección
    }
?>
