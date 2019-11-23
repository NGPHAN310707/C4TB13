a = {'name' : 'Nguyen',
    'role' : 'waiter',
    'hour' : 12,
    'salary per hours($)' : 0.8}                        
b = {'name' : 'Phan',
    'role' : 'cook',
    'hour' : 24,
    'salary per hours($)' : 1.5}                                        
c = {'name' : 'Lâm',
    'role' : 'manager',
    'hour' : 20,
    'salary per hours($)' : 2}
luongthang = {
    'luong thang Nguyen' : 0.8*12,
    'luong thang Phan' : 1.5*12,
    'luong thang Lâm' : 2*12
}
totalsalary = {
    wage['luong thang Nguyen'] + wage['luong thang Phan'] + wage['luong thang Lâm']
}
print('Giám đốc trả lương cho các nhân viên : ',totalsalary)
