<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 42 de PHP - Trabalhando com Arquivos - Parte 2 - Livro de visitas</title>
</head>
<body>

	<?php
	
		$arquivo=fopen("visitas.txt","r");
		while(!feof($arquivo)){
			echo fgets($arquivo,4096);
			echo "<br/>".fgets($arquivo,100);
			echo "<br/><br/>";
		}
		
		fclose($arquivo);
	
	?>

	<hr/>
	<a href="index.html" target="_self">voltar</a>
	
</body>
</html>