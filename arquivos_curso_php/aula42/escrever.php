<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 42 de PHP - Trabalhando com Arquivos - Parte 2 - Livro de visitas</title>
</head>
<body>

	<?php
	
		$nome=$_POST['f_nome'];
		$msg=$_POST['f_msg'];
		$conteudo=$msg."\r\n".$nome."\r\n";
		
		$arquivo=fopen("visitas.txt","a");
		fwrite($arquivo,$conteudo);
		
		echo "Mensagem gravada: $conteudo";
		
		fclose($arquivo);
	
	?>

	<hr/>
	<a href="index.html" target="_self">voltar</a>
	
</body>
</html>