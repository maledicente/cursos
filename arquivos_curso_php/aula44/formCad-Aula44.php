<?php

	include "../conexao.inc";

?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
	<title>Aula 44 de PHP - MySQL - Formulário com múltiplas tabelas</title>
</head>
<body>

	<h1>Pesquisa:</h1>
	
	<form name="fcad" action="processaAula44.php" method="get">
	
		<label>Nome:</label><br/>
		<input type="text" name="fnome"><br/><br/>
		
		<label>Selecione seu estado:</label><br/>
		<select name="fuf">
			<?php
				$sql="SELECT * FROM tb_uf order by uf";
				$res=mysqli_query($con,$sql);
				while($vreg=mysqli_fetch_row($res)){
					$vuf=$vreg[0];
					$vsigla=$vreg[1];
					echo "<option value=$vsigla>$vuf</option>";
				}
			?>
		</select>
		<br/><br/>
		
		<label>Selecione seus meios de transporte favoritos</label><br/>
		<?php
			$sql="SELECT * FROM tb_transportes";
			$res=mysqli_query($con,$sql);
			while($vreg=mysqli_fetch_row($res)){
				$vcod=$vreg[0];
				$vtra=$vreg[1];
				echo "<input type=checkbox name=ftransp[] value=$vcod>$vtra<br/>";
			}
		?>		
		
		<br/>
		
		<input type="submit" value="Gravar Pesquisa"/>
	
	</form>

</body>
</html>

<?php

	mysqli_close($con);

?>