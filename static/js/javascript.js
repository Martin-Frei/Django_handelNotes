

function toggelButton(){
    
    let img = document.getElementById("picture");
    

    if (img.classList.contains("small-picture")){
        //img.style.width= "50px";
        // img.className="big-picture";
        img.classList.remove("small-picture");
        img.classList.add("big-picture");
        // img.classList.toggle("big-picture");

    }

    else{
        // img.classname="small-picture";
        img.classList.remove("big-picture");
        img.classList.add("small-picture");
        // img.classList.toggle("small-picture");
    }
} 