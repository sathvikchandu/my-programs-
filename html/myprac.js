document.getElementById("but").onclick= function fun1(){
    document.getElementById("confirm").innerHTML="order confirmed, go screw yourself now";
    document.getElementById("but").style.display="none"; //this line helps in disappearing of button after clicking on it
}

//var username=prompt()
//alert("screw you "+username)

/* if you want your variables to be hidden from being global then you have to use them in function*/
function fun1(){
    var af=5 //howwvwer, if you remove the var, it becomes global and can be accessible
    console.log(af+y)
}; 
let y=4;
let ny="sathvik"
ny=ny.toLocaleUpperCase();  // here string is primitive, but when u calling an onject function, the string is wrapped into object and that function is executed and it is turned back into primitive
console.log(ny+" ");
const rt=4;
let r=Number.parseFloat("56.31221");
console.log(rt+r);

var inp=Number(prompt("enter a number to see the magic "));
console.log("the number in decimal is ", Number.parseInt(inp,10))
console.log("the number in binary is  ", Number.parseInt(inp,2 ))
console.log("the number in octal is   ", Number.parseInt(inp,8))
console.log("the number in hex is     ", Number.parseInt(inp,16))

console.log("the number is             ",inp.toString(10))
console.log("the numberr in decimal is ",inp.toString(2))
console.log("the numeber in octal is   ",inp.toString(8))
console.log("the number in hexadeci is ",inp.toString(16))
let x=21321321312
console.log("**")
console.log(x.toLocaleString())

var abs=Math.abs(-324)
console.log(abs)

let content="hello, nice to meet you, i am mister potato";
let s1="o";
console.log("welcome mr.potato");
console.log(content.indexOf(s1,content.indexOf(s1)+1)); // if you want to find the second time where the substring is present
console.log(content.lastIndexOf(s1));
console.log(content.substring(6,13)); // returns characterns from 6 to 13
console.log(content.substr(3,15)); //returns 15 characters after 3 index
console.log(content.trim());
console.log(content.repeat(300));

{
    let pos = {
        x:10,
        y:20,
        print: function(){
            console.log(`X: ${this.x}, Y: ${this.y}`);

        },
        myobj:{idk:"i dont know"},

    }
    pos.print();
    console.log(pos.myobj.idk);

}


var age=prompt("enter the age to check the status for vaccine");
switch(age){
    case age>18 && age<45:
        console.log("u r not eligible for vaccine right now");
        break;
    case age>45 && age<60:
        console.log("u r eligible for vaccine but limited doses r available");
        break;
    case age>60:
        console.log("get vaccinated before we run out of doses for your category");
        break;
    default:
        console.log("age error");
        break;
}

