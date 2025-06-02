def format_name(f_name, l_name):
    if f_name=="" and l_name=="":
        return "invalid"
    if f_name=="" or l_name=="":
        return "missing"

    return f_name.title()+" "+l_name.title()
print(format_name(f_name=input("enter your first name:"),l_name=input("enter your last name")))
