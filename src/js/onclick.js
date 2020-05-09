function click_like(){
    var like_num=/\d+/.exec(document.getElementById("like_count").innerText)
    document.getElementById("like_count")
    like_num=parseInt(like_num)+1
    var pix=document.body.clientWidth
    window.alert(pix)
    document.getElementById("like_count").innerHTML=like_num+' like'
}

function loadXMLDoc(url)
{
xmlhttp=null;
if (window.XMLHttpRequest)
  {// code for Firefox, Opera, IE7, etc.
  xmlhttp=new XMLHttpRequest();
  }
else if (window.ActiveXObject)
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
if (xmlhttp!=null)
  {
  xmlhttp.onreadystatechange=state_Change;
  xmlhttp.open("GET",url,true);
  xmlhttp.send(null);
  }
else
  {
  alert("Your browser does not support XMLHTTP.");
  }
}

function state_Change()
{
if (xmlhttp.readyState==4)
  {// 4 = "loaded"
  if (xmlhttp.status==200)
    {// 200 = "OK"
    document.getElementById('T1').innerHTML=xmlhttp.responseText;
    }
  else
    {
    alert("Problem retrieving data:" + xmlhttp.statusText);
    }
  }
}
