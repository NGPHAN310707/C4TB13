a = {'name' : 'Phan',
    'role' : 'waiter',
    'hour' : 12,
    'salary per hours($)' : 0.8}                        
b = {'name' : 'Nguyen',
    'role' : 'cook',
    'hour' : 24,
    'salary per hours($)' : 1.5}                                        
c = {'name' : 'Lâm',
    'role' : 'manager',
    'hour' : 20,
    'salary per hours($)' : 2}
luongthang = {
    'luong thang Phan' : 0.8*12,
    'luong thang Nguyen' : 1.5*12,
    'luong thang Lâm' : 2*12
}
for i in enumerate(luongthang):
    print(i)
