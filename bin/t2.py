#!//usr/bin/python
import json
# -*- coding: utf8 -*-


a="""<html><head>
    <meat http-equiv="Content-Type" content="text/html" charset="gb2312">
    <link type="text/css" rel="stylesheet" href="../css/frontpage.css"> 
    <title>Technical Test Field-A Blog For Stefaniexyy</title>
</head>   <body>
        <script src="../js/chage_pixel.js"></script>
        <script src="../js/onclick.js"></script>        <div class="box_out_title" id="head">
            <div class="box_in_title_K" id="title" >
                <div class="box_in_title_mid">
                    <div class="box_in_title_inner" id="title_small">
                        <title3>差旅随笔  </title3>
                    </div>
                    <div  class="box_in_title_inner" id="title_small">
                        <title3>代码笔记  </title3>
                    </div>
                    <div  class="box_in_title_inner" id="title_small">
                        <a href='https://github.com/stefaniexyy' id="title_small" style="text-decoration:none" >Github</a>
                    </div>
                    <div  class="box_in_title_inner" id="title_small">
                        <title3>关于  </title3>
                    </div>    
                </div>          
            </div>
            <div class="box_in_title" id="title"  >
                <title1>技术试验田<br></title1>
                <title2>A Stefaniexyy's Blog<br></title1>
            </div>
        </div>        <div class="box_content" id="box_content">
            <div calss="box_left" id="box_left">                <div class="box_conetnt_in" id="box_conetnt_in">
                    <div class="box_content_title" style="position:relative;">
                        <div style="position:absolute; left:0;bottom: 0;font-size: 40px;font-family: Microsoft JhengHei;">
                        魔幻智利，游行见闻
                        </div>
                        <div style="position:absolute; right:0;bottom: 0;line-height:1px;font-family: Microsoft Yahei">
                        <p style="color:grey ;">
                            0 Comments
                        </p>
                        <p  >
                            2020-04-27
                        </p>
                        </div>
                    </div>
                    <div class="box_content_mid" id="box_content_mid">
                        <img src='../res/Santigo_trip/santigo_view_small.JPG' height='300px'>
                    </div>
                    <div class="box_content_title" style="position:relative;">
                        <div id="box_content_tail_left;font-size: 20px;" >
                            <div style="position:absolute;left:10;bottom: 20;" id="demon">                               
                                <button onclick="click_like()" id="like_botton" ></button>
                            </div>
                            <div style="position:absolute;left:35;bottom: 18;" id="like_count">
                                0 Like
                            </div>
                        </div>
                        <div style="position:absolute; right:0;bottom: 0;">
                            智利圣地亚哥
                        </div>                        
                    </div>
                </div>                <div class="box_conetnt_in" id="box_conetnt_in">
"""
print(bytes(a,'gb2312'))