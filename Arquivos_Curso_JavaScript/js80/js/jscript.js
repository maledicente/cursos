var diryJ,dirxJ,jog,velJ,pjx,pjy;
var tamTelaW,tamTelaH;
var jogo;
var frames;

function teclaDw(){
	var tecla=event.keyCode;
	if(tecla==38){//Cima
		diryJ=-1;
	}else if(tecla==40){//Baixo
		diryJ=1;
	}
	if(tecla==37){//Esquerda
		dirxJ=-1;
	}else if(tecla==39){//Direita
		dirxJ=1;
	}
	if(tecla==32){//Espaço / Tiro
		//TIRO
	}
}
function teclaUp(){
	var tecla=event.keyCode;
	if((tecla==38)||(tecla==40)){
		diryJ=0;
	}
	if((tecla==37)||(tecla==39){//Esquerda
		dirxJ=0;
	}
}

function controlaJogador(){
	//pjy+=
}

function gameLoop(){
	if(jogo){
		//FUNÇÕES DE CONTROLE
	}
	frame=requestAnimationFrame(gameLoop);
}

function inicia(){
	jogo=false;

	//Ini Tela
	tamTelaH=window.innerHeight;
	tamTelaW=window.innerWidth;

	//Ini Jogador
	dirxJ=diryJ=0;
	pjx=tamTelaW/2;
	pjy=tamTelaH/2;
	velJ=5;
	jog=document.getElementById("naveJog");
	jog.style.top=pjy+"px";
	jog.style.çeft=pjx+"px";

}

window.addEventListener("load",inicia);
document.addEventListener("keydown",teclaDw);
document.addEventListener("keyup",teclaUp);