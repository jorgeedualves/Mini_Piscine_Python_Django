#include <stdio.h>


//logica de Chamada dos scripts

//file 4
function puffin()
{
	alert("Exercice réussi!");
}


//file 1
function unicorn()
{
	puffin()
}

//file 3
function whale()
{
	unicorn();
}

//file 2
function cat()
{
	whale();
}

cat()




