#!/usr/bin/python
# -*- coding: utf8 -*-

class get_content:


    def content_head(self):
        content_head="""        <div class="box_out_title" id="head">
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
        </div>"""
        return content_head

    def content_tail(self):
        content_tail="""        <div id="tail">
            <div class="box_tail_out" id="tail_out">
                <div class="box_tail_in" id="box_tail_in">
                    Powered by
                </div>
                <div class="box_tail_in" id="box_tail_in">
                    <img src="../res/logo/python_logo.png">
                </div>
                <div class="box_tail_in" id="box_tail_in">
                    <img src="../res/logo/mariadb_logo.png">
                </div>
                <div class="box_tail_in" id="box_tail_in">
                    <img src="../res/logo/rspi_logo.png" height="50px">
                </div>
            </div>
            <div id="title" style="font-family: Microsoft JhengHei;font-size: 10px;">
                stefaniexyy@hotmail.com V0.1
            </div>
        </div>"""
        return content_tail


    def content_left_formart(self,title,comments_count,update_date,img_url,location):
        content_left="""                <div class="box_conetnt_in" id="box_conetnt_in">
                    <div class="box_content_title" style="position:relative;">
                        <div style="position:absolute; left:0;bottom: 0;font-size: 40px;font-family: Microsoft JhengHei;">
                        """+title+"""
                        </div>
                        <div style="position:absolute; right:0;bottom: 0;line-height:1px;font-family: Microsoft Yahei">
                        <p style="color:grey ;">
                            """+str(comments_count)+""" Comments
                        </p>
                        <p  >
                            """+update_date+"""
                        </p>
                        </div>
                    </div>
                    <div class="box_content_mid" id="box_content_mid">
                        <img src='"""+img_url+"""' height='300px'>
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
                            """+location+"""
                        </div>                        
                    </div>
                </div>"""
        return content_left

    def content_left(self):
        conetent_left_begin="""        <div class="box_content" id="box_content">
            <div calss="box_left" id="box_left">"""
        content_left_end="""                <div class="box_conetnt_page" id="box_conetnt_page">
                    <div class="box_page_in" id="box_page_in">
                        1
                    </div>
                    <div class="box_page_in" id="box_next_page_in">
                        下一页
                    </div>
                </div>
            </div>"""
        content_full=conetent_left_begin+self.content_left_formart('魔幻智利，游行见闻',0,'2020-04-27','../res/Chile_strike/plaza_italia_small.png','智利-圣地亚哥')+self.content_left_formart('圣地亚哥之旅',0,'2020-04-29','../res/Santigo_trip/santigo_view_small.JPG','智利-圣地亚哥')+content_left_end
        return content_full

    def content_right(self):
            content_right="""        <div class="box_right" id="box_right">
                <dv class="box_icon" style="position:relative;">
                    <form method="post">
                        <input type="text" name="fontpage_search" style="width: 180px;" placeholder="搜索博文" required="">
                        <button type="submit" id="seach_botton"></button>
                    </form>
                </dv>
                <div class="link_bar" id="link_bar">
                    <div id="link_bar_mini">
                        <a href="https://space.bilibili.com/104319509?spm_id_from=333.788.b_765f7570696e666f.1"><img src='../res/logo/bilibili_logo.png' width="40px"></a>
                    </div>
                    <div id="link_bar_mini">
                        <img src='../res/logo/weibo_logo.png' width="40px">
                    </div>
                    <div id="link_bar_mini">
                        <a href="https://www.youtube.com/channel/UCAYbstnb-m9_HvP7e552UjQ"><img src='../res/logo/youtube_logo.png' width="40px"></a>
                    </div>
                </div>
                <div id="name" style="font-size: 18px;">
                    Willy "Stefaniexyy" Xi
                </div>
                <div id="name" style="font-size: 14px;">
                    @Chile
                </div>
                <div class="box_icon">
                    <img src="../res/my.png" height="180px">
                </div>
                <div class="login_bar_out" id="login_bar_out">
                    <form method="POST">
                        <div id="login_bar">
                            <input type="text" name="login_username" style="width: 160px;" placeholder="用户名" required="">
                        </div>
                        <div id="login_bar">
                            <input type="text" name="login_password" style="width: 160px;" placeholder="密码" required="">
                        </div>
                        <div id="login_bar">
                            <button  type="submit" id="login_botton"  >登录</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>"""
            return content_right




    def body_content(self):
        body_begin="""   <body>
        <script src="../js/chage_pixel.js"></script>
        <script src="../js/onclick.js"></script>"""
        body_end="</body>"
        body_head=self.content_head()
        body_middle_left=self.content_left()
        body_middle_right=self.content_right()
        body_tail=self.content_tail()
        
        body_content=body_begin+body_head+body_middle_left+body_middle_right+body_tail+body_end

        return body_content