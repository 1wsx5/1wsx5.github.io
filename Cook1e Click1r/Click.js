var clicks = 0;
var x = 0;
function onClick() {
  clicks += 1;
  setInterval(function() {
  document.getElementById("clicks").innerHTML = clicks;
   }, 100);
}
function SteamClick(){
if (clicks >= 10) {
   clicks -= 10;
   x += 1;
   setInterval(function() {
   document.getElementById("steampunk").innerHTML = x;
    }, 100);
  }
}
// Will execute myCallback every 0.5 seconds 
setInterval(function() {
    clicks += 1*x;
    document.getElementById("clicks").innerHTML = clicks;
  }, 1000);

setInterval(function() {
console.log(x);
console.log(clicks);
}, 100);
