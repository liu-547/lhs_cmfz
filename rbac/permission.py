def permission(user, request):
    # 用户存在代表登录成功，则获取当前登录用户的权限

    permission_url = user.roles.filter(permissions__isnull=False).values("permissions__url",
                                                                         "permissions__is_menu",
                                                                         "permissions__title",
                                                                         "permissions__id",
                                                                         "permissions__module").distinct()

    menu_list = []
    permission_list = []

    for url in permission_url:
        permission_list.append(url['permissions__url'])
        # 判断哪些是菜单的url  True是菜单
        if url['permissions__is_menu']:
            temp = {
                "title": url['permissions__title'],
                "url": url['permissions__url'],
                "id": url['permissions__id'],
                "module": url['permissions__module']
            }
            menu_list.append(temp)
    print("menu_list:", menu_list)
    flag = 0
    for ml in menu_list:
        if ml['module'] == 1:
            flag = 1
        elif ml['module'] == 2:
            flag = 2
        elif ml['module'] == 3:
            flag = 3
        elif ml['module'] == 4:
            flag = 4
    request.session['flag'] = flag
    # 将权限列表存入session
    request.session['permission_list'] = permission_list
    # 将菜单权限列表存入session
    request.session['menu_list'] = menu_list
