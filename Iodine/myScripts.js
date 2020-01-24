function myLoop(){
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;
  var count = document.getElementById("count").value;
  
  console.log(typeof start);
  console.log(typeof end);
  console.log(typeof count);
  
  start= Number(start);
  end = Number(end);
  count = Number(count);
  
  console.log(typeof start);
  console.log(typeof end);
  console.log(typeof count);
  
  for(var i = start; i <= end; i+=count)
    {
     document.write('<p>' + i + '<p>');
    }
}
