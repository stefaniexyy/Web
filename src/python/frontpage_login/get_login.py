#!/usr/bin/python

class get_page:

    def generate_full_page(self):
        content="""                    <form method="POST">
                        <div id="login_bar">
                            <input type="text" name="login_username" style="width: 160px;" placeholder="用户名" required="">
                        </div>
                        <div id="login_bar">
                            <input type="text" name="login_password" style="width: 160px;" placeholder="密码" required="">
                        </div>
                        <div id="login_bar">
                            <button  type="submit" id="login_botton"  onclick="loadXMLDoc('/frontpage_login.html')" >登录</button>
                        </div>
                    </form>"""
        return content