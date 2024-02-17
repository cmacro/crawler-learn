students = []
fields = ['name','tel','qq']

def print_menu():
    print(r'======================')
    print(r'  学生系统 v0.1')
    print(r'----------------------')
    print(r' 1. add')
    print(r' 2. delete')
    print(r' 3. modify')
    print(r' 4. find')
    print(r' 5. show all')
    print(r' 6. exit')
    print(r'----------------------')
    
def student_indexOf(name):
    for i, s in enumerate(students):
        if name == s[fields[0]]:
            return i
    return -1

def student_inputInfo():
    info = {}
    for field in fields:
        info[field] = input(f'请输入{field}:')
    return info

def student_add():
    info = student_inputInfo()
    if student_indexOf(info[fields[0]]) >= 0:
        print(f"当前学生{info[fields[0]]}已经存在")
        return
    students.append(info)
    print(f"add {info[fields[0]]} ")

def student_delete():
    idx = int(input(f'请输入删除学生Index:'))
    if idx < 0 or idx >= len(students):
        print('超出索引范围')
        return 
    info = students.pop(1)
    print(f'del fnished: {info[fields[0]]}')

def student_modify():
    idx = int(input(f'请输入修改学生Index:'))
    if idx < 0 or idx >= len(students):
        print('超出索引范围')
        return 
    
    newinfo = student_inputInfo()
    newinfo = {key: value for key, value in newinfo.items() if value is not None and value != ''}
    if fields[0] in newinfo and newinfo[fields[0]] != students[idx][fields[0]] and student_indexOf(newinfo[fields[0]]) >= 0:
        print(f"当前学生{newinfo[fields[0]]}已经存在")
        return

    students[idx] = {**students[idx], **newinfo}
    print(f'修改学生信息索引{idx}完成{students[idx]}')

def student_find():
    name = input(f'请输入查询{fields[0]}:')
    idx = student_indexOf(name)
    print(f'学生{name}不存在' if idx < 0 else " | ".join(str(students[idx][field]) for field in fields))

def student_showall():
    print('idx | ' + ' | '.join(fields))
    print('--------------------------')
    for i, s in enumerate(students):
        row = " | ".join(str(s[field]) for field in fields)
        print(f'{i} | {row}')
    print('--------------------------')
    print(f'count({len(students)})')    


def main():
    opts = {
        '1': student_add, 
        '2':student_delete, 
        '3':student_modify, 
        '4':student_find, 
        '5':student_showall}
    opt = ''
    while opt != '6':
        if opt in opts:
            opts[opt]()
        print('')
        print_menu()
        opt = input('请输入菜单编号：')


if __name__ == "__main__":
    main()
    
