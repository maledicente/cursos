<?php

	$transp=array("Carro","Moto","Bicicleta","Ônibus","Avião","Navio");
	
	foreach($transp as $veiculo){
		echo "$veiculo<br/>";
		/*
		if($veiculo == "Bicicleta"){
			break;
		}
		*/
	}
	echo "<hr/>";
	foreach($transp as $veiculo){
		if($veiculo == "Bicicleta"){
			echo "Bicicleta está na lista de veículos<br/>";
			break;
		}
			
		if($veiculo == "Trem")
			echo "Trem está na lista de veículos<br/>";
	}
	


?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 10 de PHP - Loop FOREACH</title>
</head>
<body>

</body>
</html>