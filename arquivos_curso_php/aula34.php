<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 33 de PHP - MySQL: Comando Select</title>
</head>
<body>

<table border="1">
	<tr>
		<td>Codigo</td><td>Produto</td><td>Preco</td><td>Qtde</td><td>categoria</td>
	</tr>


<?php

	include "conexao.inc";
	
	$vpes="t%";
	
	$sql="SELECT * FROM tb_produtos WHERE codigo LIKE '$vpes'";
	$res=mysqli_query($con,$sql);
	while($vreg=mysqli_fetch_row($res)){
		$vcod=$vreg[0];
		$vprod=$vreg[1];
		$vpreco=$vreg[2];
		$vqtde=$vreg[3];
		$vcat=$vreg[4];
		
		echo "<tr>";
		echo "<td>$vcod</td><td>$vprod</td><td>$vpreco</td><td>$vqtde</td><td>$vcat</td>";
		echo "</tr>";
	}

	mysqli_close($con);

?>

</table>

</body>
</html>