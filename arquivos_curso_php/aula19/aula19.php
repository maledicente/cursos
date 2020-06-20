<?php

	session_start();
	$_SESSION['vnome']="Bruno";
	$_SESSION['vtexto']="texto para teste";
	$_SESSION['vlog']="n";
	
	//unset($_SESSION['vnome']);
	
	echo $_SESSION['vnome'];
	echo "<br/>".$_SESSION['vtexto'];
	
	if(isset($_SESSION['vcanal'])){
		echo "<br/>".$_SESSION['vcanal'];
	}else{
		echo "<br/>Variável vcanal NÃO foi definida";
	}
	
	//session_destroy();

?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 19 de PHP - Sessão</title>
</head>
<body>

	<br/>
	<a href="pg1.php" target="_self">Segunda página</a>

</body>
</html>
