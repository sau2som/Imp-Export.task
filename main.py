from mathOperation.addop import addvalue
from mathOperation.divop import divvalue
from mathOperation.subop import subvalue
from mathOperation.multop import multvalue

if __name__ == '__main__':
 print('this is main code')
val1=eval(input('enter the first no:= '))
val2=eval(input('enter the second no:= '))
op=input('which math operation you want to carry, add,sub,mult,div :')


if op.lower() =='add':
    a1=addvalue(val1,val2)
    print(f'addition={a1}')
elif op.lower() =='sub':
    a2=subvalue(val1,val2)
    print(f'substraction={a2}')
elif op.lower() =='mult':
    a3=multvalue(val1,val2)
    print(f'multiplication={a3}')
elif op.lower() =='div':
    a4=divvalue(val1,val2)
    print(f'division={a4}')
else:
    print('please enter right operation')