# 作者:ZhaoYu Wang
# 日期:2021年10月19日

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models=[]

def print_models (unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Model:"+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("printed:\n")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

def show_magicians(magicians):
    for magician in magicians:
        print("Hello",magician)

magicians=['aaaa','bbbb','cccc','dddd']
show_magicians(magicians)
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i]="The Greet "+magicians[i]

make_great(magicians[:])
print(magicians)
make_great(magicians)
print(magicians)