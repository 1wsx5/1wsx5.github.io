var clicks = 0;
var x = 0;
var bun = 0;
function onClick() {
  clicks += 1;
  setInterval(function() {
  document.getElementById("clicks").innerHTML = clicks;
   }, 100);
}
function SteamClick(){
if (clicks >= 50) {
   clicks -= 50;
   x += 1;
   setInterval(function() {
   document.getElementById("steampunk").innerHTML = x;
    }, 100);
  }
}
// Will execute myCallback every 0.5 seconds 
function BunClick(){
if (clicks >= 100) {
   clicks -= 100;
   bun += 1;
   setInterval(function() {
   document.getElementById("bunbun").innerHTML = bun;
    }, 100);
  }
}

setInterval(function() {
    clicks += 1*x;
    clicks += 2*bun;
    document.getElementById("clicks").innerHTML = clicks;
  }, 1000);

setInterval(function() {
console.log(x);
console.log(clicks);
}, 100);
