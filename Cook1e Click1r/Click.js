var clicks = 0;
var x = 0
function onClick() {
  clicks += 1;
  document.getElementById("clicks").innerHTML = clicks;
};
function SteamClick(){
if (clicks == 50 && document.getElementById("steampunk").onclick) {
  ;
  clicks -= 50;
  x += 1;
  }
};
// Will execute myCallback every 0.5 seconds 
var intervalID = setInterval(myCallback, x*1000);

function myCallback() {
  clicks += 1;
}
console.log(x);
console.log(clicks);
