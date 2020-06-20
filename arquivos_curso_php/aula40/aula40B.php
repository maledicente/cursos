<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 40 de PHP - MySQL: Login com sessões</title>
</head>
<body>

	<?php
		
		session_start();
		
		if(isset($_SESSION["numLogin"])){
			$n1=$_GET["num1"];
			$n2=$_SESSION["numLogin"];
			if($n1 != $n2){
				echo "login nao efetuado";
				exit;
			}
		}else{
			echo "login nao efetuado";
			exit;			
		}
		
		include "../conexao.inc";
		
		echo "Pagina inicial<br/>";
		echo "Username: ".$_SESSION['username']."<br/>";
		
		
		//unset($_SESSION['numLogin']);
		//session_unregister('numLogin');
	
		//$_SESSION=array();
		//session_destroy();

		mysqli_close($con);

	?>

</body>
</html>