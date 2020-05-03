function click_like(){
    var like_num=/\d+/.exec(document.getElementById("like_count").innerText)
    document.getElementById("like_count")
    like_num=parseInt(like_num)+1
    document.getElementById("like_count").innerHTML=like_num+' like'
}

function login(){
    var login_Obj=new XMLHttpRequest()
    login_Obj.open("POST")
    
}