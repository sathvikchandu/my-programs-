console.log('Hello, World!');

var input=document.getElementById('menu');

var btnadd=document.getElementById('additem');

var list=document.getElementById('todo');

var updatebtn=document.getElementById('updateitem');

var removebtn=document.getElementById('removeitem');

curr_input=""
input.addEventListener('input',function(e){
   curr_input=e.target.value; 
});


input.addEventListener('keyup',function(e){
    if(e.keyCode==13){
        addlistitem();
            
    }
});

function createnewnode(){
    var new_element =document.createElement('li');

 

        var textnode=document.createTextNode(curr_input);
        
        new_element.appendChild(textnode);

        new_element.id="item"+(list.childElementCount+1);
        return new_element;
}


function addlistitem(){
    if (curr_input!==""&& curr_input!=="null" && curr_input!=="undefined"){
        
        var new_element=createnewnode();

        list.appendChild(new_element);
        
        input.value="";
        curr_input="";



    }

    else{
        alert("Add a fuckin accepted value u cheap fuck!");
    }
}

btnadd.addEventListener('click',addlistitem);

updatebtn.addEventListener('click',function(){
    var firstelem=list.firstElementChild;
    var new_element=createnewnode();
    list.replaceChild(new_element,firstelem);
});

removebtn.addEventListener('click',function(){
    list.removeChild(list.firstElementChild);
});


