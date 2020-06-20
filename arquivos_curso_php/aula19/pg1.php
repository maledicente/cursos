<?php

	session_start();
	
	if($_SESSION['vlog']=="s"){
	
		$_SESSION['vcanal']="vlog do fessor Bruno";
	
		echo "<h3>Segunda página</h3>";
	
		echo $_SESSION['vnome'];
		echo "<br/>".$_SESSION['vtexto'];
	

?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 19 de PHP - Sessão</title>
</head>
<body>

	<br/><br/>
	<a href="aula19.php" target="_self">voltar aula 19</a><br/>
	<a href="pg2.php" target="_self">Terceira página</a>

</body>
</html>

<?php

	}else{
		echo "acesso indevido...";
	}

?>