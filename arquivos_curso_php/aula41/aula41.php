<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 41 de PHP - Trabalhando com Arquivos</title>
</head>
<body>

	<?php

		//r = Abre p/leitura, ponteiro no início
		//r+ = Abre p/leitura e escrita
		//w = Abre p/escrita, ponteiro no início e zera, se arquivo não existir ele o cria
		//w+ = Abre p/leitura e escrita
		//a = Abre p/escrita, ponteiro no final, se arquivo não existir ele o cria
		//a+ = Abre p/leitura e escrita
		//x = Abre p/escrita, ponteiro no início, se arquivo já existir ele gera um erro do tipo E_WARNING
		//x+ = Abre p/leitura e escrita

		$arquivo=fopen("aula.txt","a");
		fwrite($arquivo,"\r\nCurso de PHP.");
		
		$arquivo=fopen("aula.txt","r");
		$conteudo=fread($arquivo,100);
		
		echo $conteudo;
		
		fclose($arquivo);

	?>

</body>
</html>