<?php

	interface CarroPadrao{
		function liga();
		function desliga();
		function status();
		function acelera();
		function freia();
	}
	
	interface CarroGuerra{
		function atiraCanhao();
		function atiraMetralhadora();
	}
	
	abstract class CarroBase implements CarroPadrao, CarroGuerra{
		public $potencia;
		public $velMax;
		private $ligado=false;
		
		function liga(){
			$this->ligado=true;
		}
		
		function desliga(){
			$this->ligado=false;
		}
		
		function status(){
			echo "<hr/>";
			echo "Potencia: ".$this->potencia;
			echo "<br/>Velocidade Máxima: ".$this->velMax;
			echo "<br/>";
			if($this->ligado){
				echo "Esta carro está ligado";
			}else{
				echo "Este carro NÃO está ligado";
			}
			echo "<hr/>";
		}
		
		function acelera(){}
		function freia(){}
		function atiraCanhao(){}
		function atiraMetralhadora(){}
	
	}
	
	class Carro extends CarroBase{
		function Carro($pt,$vm){
			$this->potencia=$pt;
			$this->velMax=$vm;
			
			$this->liga();
			$this->status();
		}
	}

	$carro1=new Carro(150,280);
	//$carro1->liga();
	//$carro1->status();

?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 23 de PHP - Classes parte 4</title>
</head>
<body>

</body>
</html>