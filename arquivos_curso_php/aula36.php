<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 36 de PHP - MySQL: Deletando registros selecionados</title>
</head>
<body>

<form name="f_excluir" method="post" action="aula36.php">

	<table border="1">
		<tr>
			<td>Codigo</td><td>Nome</td><td>Selecionar</td>
		</tr>
	
		<?php
	
			include "conexao.inc";
			
			if(isset($_POST['sel'])){
				foreach($_POST['sel'] as $codigo){
					$sql="delete FROM tb_cadastro WHERE cod=$codigo";
					$res=mysqli_query($con,$sql);
				}
			}else{
				echo "form NÃO submetido";
			}
	
			$sql="SELECT * FROM tb_cadastro order by cod";
			$res=mysqli_query($con,$sql);
			
			while($vreg=mysqli_fetch_row($res)){
				$vcod=$vreg[0];
				$vnome=$vreg[1];
				
				echo "<tr>";
				echo "<td>$vcod</td><td>$vnome</td>";
				echo "<td align=center><input type=checkbox value=$vcod name=sel[]></td>";
				echo "</tr>";
			}
	
			mysqli_close($con);
	
		?>
		
	</table>
	
	<br/>
	
	<input type="submit" value="Excluir" name="bt_excluir"/>
	
</form>


</body>
</html>