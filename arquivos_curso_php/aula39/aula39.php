<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 39 de PHP - MySQL: Login</title>
</head>
<body>

	<?php

		include "conexao.inc";
		
		$user=$_POST['f_user'];
		$senha=$_POST['f_senha'];
		
		$sql="SELECT * FROM tb_cadastro WHERE username='$user' AND senha='$senha'";
		$res=mysqli_query($con,$sql);
		$linha=mysqli_affected_rows($con);
		
		if($linha > 0){
			$num=rand(100000,900000);
			setcookie("numLogin",$num);
			header("Location:aula39B.php?num1=$num");
		}else{
			echo "ERRO no login<br/>";
			echo "<a href='formAula-39.html'>voltar</a>";
		}

		mysqli_close($con);

	?>

</body>
</html>