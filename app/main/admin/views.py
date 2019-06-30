# coding:utf-8
from flask_login import login_required
from flask import request, jsonify, render_template, globals
from app.main.admin.models import *
from app.main.common.alchemyEncoder import AlchemyEncoder
from app.main.admin import admin
import json
from app.main.utils.email import *
from app.main.utils.decorators import auth


def user_dict(p):
    return {
        'id': p.id,
        'username': p.username,
        'phone': p.phone,
        'email': p.email,
        'status': p.status,
        'createTime': p.createTime.strftime('%Y-%m-%d'),
        'roles': p.roles
    }


# 管理员
@admin.route('/list', methods=['GET'])
@login_required
@auth
def admin_list():
    page = request.args.get('page')
    if page is None:
        page = 1
    limit = request.args.get('limit')
    if limit is None:
        limit = 10
    pagination = globals.db.query(User).paginate(int(page), int(limit), error_out=False)
    items = pagination.items
    return render_template('system/admin-list.html', users=items, count=pagination.total)


# 管理员-状态-修改
@admin.route('/change/<id>', methods=['POST'])
@login_required
@auth
def admin_change_status(id):
    if request.method == 'POST':
        user = globals.db.query(User).filter_by(id=id).first()
        status = request.json.get('status')
        user.status = status
        user.update()
        result = {
            "code": '0000',
            "msg": "修改成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)


# 用户-添加
@admin.route('/add/', methods=['GET', 'POST'])
@login_required
@auth
def admin_add():
    roles = globals.db.query(Role).filter().all()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is not None and password is not None:
            user = User(username, password)
            user.status = int(request.form.get('status'))
            user.email = request.form.get('email')
            user.phone = request.form.get('phone')
            role_ids = request.form.get('role_ids')
            roles = json.loads(role_ids)
            for i in range(len(roles)):
                role = globals.db.query(Role).filter(Role.id == roles[i]).first()
                roles.append(role)
            user.roles = roles
            user.update()
            result = {
                "code": "0000",
                "msg": "添加成功"
            }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template("system/admin-add.html", roles=roles, user=None)


# 编辑
@admin.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def admin_edit(id):
    user = globals.db.query(User).filter_by(id=id).first()
    roles = globals.db.query(Role).filter().all()
    if request.method == 'POST':
        user.status = request.form.get('status')
        user.phone = request.form.get('phone')
        user.email = request.form.get('email')
        role_ids = request.form.get('role_ids')
        role_split = []
        if role_ids is not None and role_ids != '':
            role_split = role_ids.split(',')
        role_list = []
        for i in range(len(role_split)):
            role = globals.db.query(Role).filter(Role.id == role_split[i]).first()
            role_list.append(role)
        user.roles = role_list
        user.update()
        result = {
            "code": "0000",
            "msg": "更新成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template("system/admin-edit.html", user=user, roles=roles)


# 删除
@admin.route('/del/<id>', methods=['POST'])
@login_required
def admin_del(id):
    if request.method == 'POST':
        user = globals.db.query(User).filter_by(id=id).first()
        user.delete()
        result = {
            "code": "0000",
            "msg": "删除成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)


# # 角色
# @admin.route('/role/list', methods=['GET', 'POST'])
# @login_required
# def role_list():
#     if request.method == 'POST':
#         page = request.form['page']
#         limit = request.form['limit']
#         pagination = globals.db.query(Role).paginate(int(page), int(limit), error_out=False)
#         items = pagination.items
#         result = {
#             "code": 0,
#             "msg": "获取成功",
#             "count": pagination.pages,
#             "data": items
#         }
#         return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
#     return render_template('system/admin-role.html')


# 角色
@admin.route('/role/list', methods=['GET'])
@login_required
def role_list():
    page = request.args.get('page')
    if page is None:
        page = 1
    limit = request.args.get('limit')
    if limit is None:
        limit = 10
    pagination = globals.db.query(Role).paginate(int(page), int(limit), error_out=False)
    items = pagination.items
    return render_template('system/admin-role.html', roles=items, count=pagination.total)


# 角色-状态-修改
@admin.route('/role/change/<id>', methods=['POST'])
@login_required
def role_change_status(id):
    if request.method == 'POST':
        role = globals.db.query(Role).filter_by(id=id).first()
        status = request.json.get('status')
        role.status = status
        role.update()

        result = {
            "code": "0000",
            "msg": "修改成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)


# 角色-添加
@admin.route('/role/add/', methods=['GET', 'POST'])
@login_required
def role_add():
    menus = set_menus()
    if request.method == 'POST':
        role = Role()
        role.name = request.form.get('name')
        role.describe = request.form.get('describe')
        role.status = request.form.get('status')
        menu_ids = request.form.get('menu_ids')
        menuid_list = json.loads(menu_ids)
        menu_list = []
        for i in range(len(menuid_list)):
            menu = globals.db.query(Menu).filter(Menu.id == menuid_list[i]).first()
            menu_list.append(menu)
        role.menus = menu_list
        role.save()
        result = {
            "code": "0000",
            "msg": "添加成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('system/admin-role-add.html', action='add', role=None, menus=menus)


def role_dict(p):
    return {
        'id': p.id,
        'name': p.name,
        'describe': p.describe,
        'status': p.status,
        'menu_ids': p.menu_ids
    }


# 角色-修改
@admin.route('/role/edit/<id>', methods=['GET', 'POST'])
@login_required
def role_edit(id):
    menus = set_menus()
    role = globals.db.query(Role).filter(Role.id == id).first()
    if request.method == 'POST':
        role.name = request.form.get('name')
        role.describe = request.form.get('describe')
        role.status = request.form.get('status')
        menu_ids = request.form.get('menu_ids')
        menuid_list = json.loads(menu_ids)
        menu_list = []
        for i in range(len(menuid_list)):
            menu = globals.db.query(Menu).filter(Menu.id == menuid_list[i]).first()
            menu_list.append(menu)
        role.menus = menu_list
        role.save()
        result = {
            "code": "0000",
            "msg": "修改成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('system/admin-role-add.html', action='edit', role=role, menus=menus)


# 角色-删除
@admin.route('/role/del/<id>', methods=['POST'])
@login_required
def role_del(id):
    if request.method == 'POST':
        role = globals.db.query(Role).filter(Role.id == id).first()
        role.delete()
        result = {
            "code": "0000",
            "msg": "删除成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)


def set_menus():
    tree = []
    allMenu = globals.db.query(Menu).order_by(Menu.id.asc()).all()
    for i in range(len(allMenu)):
        if allMenu[i].parent_id == 0:
            item = {}
            item['title'] = allMenu[i].name
            item['parent_id'] = allMenu[i].parent_id
            item['id'] = allMenu[i].id
            item['url'] = allMenu[i].url
            item['checked'] = False
            item['spread'] = False
            if allMenu[i].status == 1:
                item['disabled'] = False
            else:
                item['disabled'] = True
            tree.append(item)

    for k in range(len(tree)):
        tree[k]['children'] = get_children_menu(tree[k]['id'], allMenu)
    return tree


def get_children_menu(parentId, allMenu):
    children = []
    for i in range(len(allMenu)):
        if allMenu[i].parent_id is not None:
            if allMenu[i].parent_id == parentId:
                item = {}
                item['title'] = allMenu[i].name
                item['parent_id'] = allMenu[i].parent_id
                item['id'] = allMenu[i].id
                item['url'] = allMenu[i].url
                item['checked'] = False
                if allMenu[i].status == 1:
                    item['disabled'] = False
                else:
                    item['disabled'] = True
                children.append(item)

    for j in range(len(children)):
        if children[j]['url'] is None:
            children[j]['children'] = get_children_menu(children[j]['id'], allMenu)
    return children


# 菜单
@admin.route('/menu/list', methods=['GET', 'POST'])
@login_required
def menu_list():
    page = request.args.get('page')
    if page is None:
        page = 1
    limit = request.args.get('limit')
    if limit is None:
        limit = 10
    pagination = globals.db.query(Menu).paginate(int(page), int(limit), error_out=False)
    menus = pagination.items
    return render_template('system/admin-menu-list.html', menus=menus, count=pagination.total)


# 菜单-添加
@admin.route('/menu/add/<parentId>', methods=['GET', 'POST'])
@login_required
def menu_add(parentId):
    if request.method == 'POST':
        name = request.form.get('name')
        url = request.form.get('url')
        order = request.form.get('order')
        type = request.form.get('type')
        icon = request.form.get('icon')
        status = request.form.get('status')

        menu = Menu()
        menu.parent_id = parentId
        menu.name = name
        menu.url = url
        menu.order = int(order) if order != None else order
        menu.type = int(type) if type != None else type
        menu.icon = icon
        menu.status = int(status) if status != None else status
        menu.save()

        result = {
            "code": "0000",
            "msg": "添加成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('system/admin-menu-add.html', action='add', menu=None, parentId=parentId)


# 菜单-修改
@admin.route('/menu/edit/<parentId>', methods=['GET', 'POST'])
@login_required
def menu_edit(parentId):
    _menu = globals.db.query(Menu).filter(Menu.id == parentId).first()
    if request.method == 'POST':
        name = request.form.get('name')
        url = request.form.get('url')
        order = request.form.get('order')
        type = request.form.get('type')
        icon = request.form.get('icon')
        status = request.form.get('status')

        menu = Menu()
        menu.name = name
        menu.url = url
        menu.order = order
        menu.type = type
        menu.icon = icon
        menu.status = status
        menu.save()

        result = {
            "code": "0000",
            "msg": "添加成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('system/admin-menu-add.html', action='edit', menu=_menu)


# 菜单-状态-修改
@admin.route('/menu/change/<id>', methods=['POST'])
@login_required
def menu_change_status(id):
    if request.method == 'POST':
        menu = globals.db.query(Menu).filter_by(id=id).first()
        status = request.json.get('status')
        menu.status = status
        menu.update()

        result = {
            "code": "0000",
            "msg": "修改成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)


# 删除
@admin.route('/menu/del/<id>', methods=['POST'])
@login_required
def menu_del(id):
    if request.method == 'POST':
        menu = globals.db.query(Menu).filter_by(id=id).first()
        menu.delete()
        result = {
            "code": "0000",
            "msg": "删除成功"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)