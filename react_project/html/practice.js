/** 
console.log("connected succesfully")

var cde=document.getElementById("countdown");
console.log(cde);
var int= cde.innerHTML;


setInterval(function(){
    int=int>0?int-1:0;
    cde.innerHTML=int;
    var bip=int%2===0 ? 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.xUSaGwcL5AxrbliWbQHBFgHaEo%26pid%3DApi&f=1': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.2qLBMowaNBPL7LmPbTW_6gHaEo%26pid%3DApi&f=1';
},1000);
**/
//for changing css properties
/** 
console.log("connected succesfully")
var cde=document.getElementById("countdown");
var bgimg=document.getElementById("bg-img");
console.log(cde);
var int= cde.innerHTML;
setInterval(function(){
    cde.innerHTML=cde.innerHTML>0?int-=1:0;
    cde.style.fontSize=int*100+"px";
    bgimg.style.width=int*10+"%";
},1000);

**/
//adding new classes

console.log("connected succesfully")

var mh=document.getElementById("main-heading");

var but=document.getElementById("btn");
mh.classList.add("big");

but.addEventListener("click",function(){
    mh.classList.remove("big");
},4000);
