<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 39 de PHP - MySQL: Login</title>
</head>
<body>

	<?php

		if(isset($_COOKIE["numLogin"])){
			$n1=$_GET["num1"];
			$n2=$_COOKIE["numLogin"];
			if($n1 != $n2){
				echo "login nao efetuado";
				exit;
			}
		}else{
			echo "login nao efetuado";
			exit;			
		}
		
		include "conexao.inc";
		
		echo "Pagina inicial";

		mysqli_close($con);

	?>

</body>
</html>