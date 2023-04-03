var tm;
var cars;
var cx;
var gameBegin;

var summa = +prompt("Введите вашу сумму");
var c = +prompt("На какую машину (от 0 до 4) вы делаете ставку");
var stavka = +prompt("Сколько вы ставите на выигрыш");
function go()
{
	
	if (gameBegin==1) return;
	gameBegin = 1;	
	cars = [];
    cx = [];
	for (var i=0; i<5; i++)
	{
	   cars[i] = document.getElementById("p"+i);
       cars[i].style.border = "none";
       cx[i] = 680;
	}
	
	tm = setInterval(timerGo, 50);
    
}

function timerGo()
{
	for (var i=0; i<5; i++)
	{
          //случайный шаг перемещения для автомобиля 
	   cx[i] -= parseInt((Math.random()*7+2));
	   if (cx[i]<=0)
	   {
		  clearInterval(tm);
                   gameBegin = 0;
				   if(i==c){
					   alert("Вы победили");
					   summa += stavka;
                       
				   }
				   else{
					    alert("Вы проиграли. До финиша доехала машина с номером "+i);
						 summa -= stavka;
				   }
                   alert("Ваша сумма = "+summa);
                   cars[i].style.border = "5px ridge yellow";
                   return;
	   }
		cars[i].style.left = cx[i]+"px";	   
	}	
}