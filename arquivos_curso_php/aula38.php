<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 38 de PHP - MySQL: Comando Update</title>
</head>
<body>

	<?php

		include "conexao.inc";
		
		//UPDATE tabela SET campo a ser alterado WHERE condição
		$sql="UPDATE tb_cadastro SET telefone='3155555555' WHERE cod=14";
		
		$res=mysqli_query($con,$sql);
		
		if($res){
			echo "Registro atualizado com sucesso!";
		}else{
			echo "ERRO na atualizacao do registro";
		}

		mysqli_close($con);

	?>

</body>
</html>