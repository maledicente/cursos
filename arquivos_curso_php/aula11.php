<?php

	$vet=array("mouse","teclado","monitor","memória","sair","microfone","impressora");
	$tam=count($vet);
	$i=0;
	
	echo "Loop While<br/>";
	$i=0;
	while($i<$tam){
		echo "$vet[$i]<br/>";
		$i++;
		if($vet[$i] == "sair"){
			break;
		}
	}
	echo "<br/><hr/><br/>";
	echo "Loop Do While<br/>";
	$i=0;
	do{
		echo "$vet[$i]<br/>";
		$i++;
		if($vet[$i] == "sair"){
			break;
		}
	}while($i<$tam);
	
	echo "<br/><hr/><br/>";
	echo "Loop For<br/>";
	for($i=0;$i<$tam;$i++){
		if($vet[$i] == "sair"){
			break;
		}
		echo "$vet[$i]<br/>";		
	}
	
	echo "<br/><hr/><br/>";
	echo "Loop Foreach<br/>";
	foreach($vet as $pc){
		if($pc == "sair"){
			break;
		}
		echo "$pc<br/>";		
	}	


?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 11 de PHP - Break</title>
</head>
<body>

</body>
</html>