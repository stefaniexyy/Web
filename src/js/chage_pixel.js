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