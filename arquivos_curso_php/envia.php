<?php

	$vmail=$_POST['email_txt'];
	$vassunto=$_POST['assunto_txt'];
	$vmsg=$_POST['msg_txt'];
	
	if(mail($vmail,$vassunto,$vmsg,"Reply-To:resp_canal@gmail.com")){
		echo "Mensagem enviada<br/>";
		echo "<a href=aula26.php target=_self>voltar</a>";
	}else{
		echo "Erro ao enviar, tente novamente";
	}
	


?>

<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Aula 26 de PHP - Enviando e-mails</title>
</head>
<body>


</body>
</html>