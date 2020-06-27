window.onload =function load_all(){
    change_pixel()
}
function change_pixel(){
    var curr_screen_width=document.body.clientWidth
    if(curr_screen_width>1519){
        curr_screen_width=(curr_screen_width-1519)/2
    }else{
        curr_screen_width=0
    }
    var title=document.getElementById("head");
    var content=document.getElementById("box_content");
    var tail=document.getElementById("tail");
    title.style.marginLeft=curr_screen_width;
    content.style.marginLeft=curr_screen_width;
    tail.style.marginLeft=curr_screen_width;
}

var xmlhttp;
function loadXMLDoc(url){
    xmlhttp=null;
    if (window.XMLHttpRequest){// code for Firefox, Opera, IE7, etc.
        xmlhttp=new XMLHttpRequest();
    }else if (window.ActiveXObject){// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    if (xmlhttp!=null){
        xmlhttp.onreadystatechange=state_Change;
        xmlhttp.open("GET",url,true);
        xmlhttp.send(null);
  }else{
    alert("Your browser does not support XMLHTTP.");
  }
}

function state_Change(){
    if (xmlhttp.readyState==4){// 4 = "loaded"
        if (xmlhttp.status==200){// 200 = "OK"
            document.getElementById('loginDiv').innerHTML=xmlhttp.responseText;
        }else{
            alert("Problem retrieving data:" + xmlhttp.statusText);
    }
  }
}
//document.getElementById('loginDiv').innerHTML=xmlhttp.responseText;
