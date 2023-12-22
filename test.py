from DrissionPage import ChromiumPage

# 用 d 模式创建页面对象（默认模式）
page = ChromiumPage()
# 跳转到登录页面
# page.get('https://gitee.com/login')

# # 定位到账号文本框并输入账号
# page.ele('#user_login').input('kerwin-job')
# # 定位到密码文本框并输入密码
# page.ele('#user_password').input('guojiawei020613')

# # 点击登录按钮
# page.ele('@value=登 录').click()


# base_url = 'https://leetcode.cn/accounts/login/?next=%2F'
# page.get(base_url)
# ele1 = page.ele('.css-1e4fnko-Container e19orumq0')
# # ele1.child().click(by_js=True)
# ele1.child().click(by_js=True)

# # 定位到账号文本框并输入账号
# page.ele('@placeholder=手机/邮箱').input('15665839076')
# # 定位到密码文本框并输入密码
# page.ele('@placeholder=输入密码').input('guojiawei020613')
# # 点击登录按钮
# page.ele('.e4jw0mn0 css-mo585l-BaseButtonComponent-StyledButton ery7n2v0').click(by_js=True)
for i in range(1,2):
    page.get('https://leetcode.cn/problemset/?page='+ str(i))
    ele2 = page.eles('.h-5 hover:text-blue-s dark:hover:text-dark-blue-s')
    for ele_item in ele2:
        item = ele_item.texts()
        item1 = item[0]
        item2 = item[2]
