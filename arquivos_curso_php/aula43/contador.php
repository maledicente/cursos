<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 43 de PHP - Trabalhando com Arquivos - Parte 3 - Contador de acessos</title>
</head>
<body>

	<?php

		//r = Abre p/leitura, ponteiro no início
		//w = Abre p/escrita, ponteiro no início e zera, se arquivo não existir ele o cria		
	
		$arquivo=fopen("contador.txt","r");
		$cont=fread($arquivo,21);
		$cont++; //$cont+=1;  cont=cont+1;
		$arquivo=fopen("contador.txt","w");
		fwrite($arquivo,$cont);
		fclose($arquivo);
	
		echo "Quantidade de acessos: $cont<br/>";
	
	?>

	
</body>
</html>