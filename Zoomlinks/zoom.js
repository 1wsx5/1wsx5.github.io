const today = new Date();

var odd = ["https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdadeschools.zoom.us%2Fj%2F4402441257%3Fpwd%3DQnlZNUFVNm5nTFE2OHZsZ1YySHFJZz09&data=04%7C01%7C0409113%40students.dadeschools.net%7C4131bec139d54c5285a908d880bbbbf0%7C4578f68f86cd4af9b31793e3826ca0f5%7C0%7C0%7C637400891089832308%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=6ucFv7iPGGcyQ5OBGBrmKhk4nRCvMCj1mT8ezVc2JyA%3D&reserved=0", "https://dadeschools.zoom.us/j/94800510926?pwd=ZUxjNml6bEp3a0k4NSs0SW43bDB6QT09", "https://us02web.zoom.us/j/88094591047?pwd=NC83WHVHUnY5TW51SlRoWW85VHEvZz09"];

var even = ["https://zoom.us/j/7867939413?pwd=ZVh4ZXMxMXhIZTQ3SXNjOEFVOVRBUT09", "https://dadeschools.zoom.us/j/96893942696?pwd=Z3JvY2FwWmhHRHgzdnhxSTdUNzlZZz09", "https://us02web.zoom.us/j/2717974361?pwd=VXg3cG1yNVkxNFJOcUlTUitBVmFtUT09", "https://us02web.zoom.us/j/6875367389?pwd=bFZQT2R2bTdBaHd0dnMrejlRSUNTZz09"];

setInterval(function(){ 
  if(today.getDay() != 6 && today.getDay() != 0) {
    if (today.getMonth() === 11 || today.getMonth() === 0 && today.getDate() != 1 || today.getMonth === 1 && today.getDate() != 15 || today.getMonth() === 2 && today.getDate() <= 25 || today.getMonth === 3 && today.getDate() >= 5 || today.getMonth === 4 && today.getDate() <= 27 || today.getMonth === 5 && today.getDate() <= 9) {
      if (today.getDate() <= 18) {
        if (today.getDate() % 2 === 0) {  
          if (today.getHours() === 7 && today.getMinutes() === 15) {
            window.open(even[0], "blank_");
          } else if (today.getHours() === 8 && today.getMinutes() === 59) {
            window.open(even[1], "blank_");
          } else if (today.getHours() === 10 && today.getMinutes() === 37) {
            window.open(even[2], "blank_");
          } else if (today.getHours() === 12 && today.getMinutes() === 50) {
            window.open(even[3], "blank_");
          }
        } else {
          if (today.getHours() === 7 && today.getMinutes() === 15) {
            window.open(odd[0], "blank_");
          } else if (today.getHours() === 10 && today.getMinutes() === 37) {
            window.open(odd[1], "blank_");
          } else if (today.getHours() > 12 && today.getMinutes() < 50) {
            window.open(odd[2], "blank_");
          }
        }
      } 
    } 
  } 
}, 54000);
