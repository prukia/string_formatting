# string formatting in python
'{} {}'.format('one', 'two')
'one two'

# old way of formatting
'%s %s' % ('one', 'two')
'one two'

'{1} {0}'.format('one', 'two')
'two one'

# align to the right 10 spaces
'{:>10}'.format('test')
'      test'

# align to the left 10 spaces
'{:10}'.format('test')
'test      '

# align to the left and add _
'{:_<10}'.format('test')
'test______'

# center align
'{:^10}'.format('test')
'   test   '

# total of 6 spaces and align zip in the center
'{:^6}'.format('zip')
' zip  '

# truncating string by 5
'{:.5}'.format('rukiasheikhmohamed')
'rukia'

# truncating + padding 10spaces to the left
'{:10.5}'.format('rukiasheikhmohamed')
'rukia     '

# formatting for integers
'{:d}'.format(42)
'42'


'{}'.format(42)
'42'

# floating
'{:f}'.format(3.141592653589793)
'3.141593'

# padding numbers
'{:4d}'.format(42)
'  42'

# 6 spaces and adding 0 to the left and 2floaters
'{:06.2f}'.format(3.141592653589793)
'003.14'

'{:04d}'.format(42)
'0042'

# only negative numbers are prefixed with a sign but this changes that
'{:+d}'.format(42)
'+42'

'{: d}'.format((- 23))
'-23'

# formatting an array and objects
data = {'first': 'Hodor', 'last': 'Hodor!'}

'{first} {last}'.format(**data)
'Hodor Hodor!'

'{last} {first}'.format(**data)
'Hodor! Hodor'

person = {'first': 'Jean-Luc', 'last': 'Picard'}
'{p[first]} {p[last]}'.format(p=person)
'Jean-Luc Picard'

data = [4, 8, 15, 16, 23, 42]

'{d[4]} {d[5]}'.format(d=data)
'23 42'

'{d[3]} {d[2]}'.format(d=data)
'16 15'


# formatting in class
class Plant(object):
    type = 'tree'
'{p.type}'.format(p=Plant())

'tree'


class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]
'{p.type}: {p.kinds[0][name]}'.format(p=Plant())

'tree: oak'


from datetime import datetime
'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 4, 12, 4, 5))
'2001-04-12 04:05'

'{:{align}{width}}'.format('test', align='^', width='10')
'   test   '

'{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
'Gib = 2.718'

'{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)
' 2.72'

'{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')
'Gib = 2.72'

from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)
'{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')
'2001-02-03 04:05'

'{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)
'     +2.72'

'{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')
'     +2.72'


class HAL9000(object):
    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'
'{:open-the-pod-bay-doors}'.format(HAL9000())
"I'm afraid I can't do that."

# formatting binary
'Binary: {0:b}'.format(24)
'Binary: 11000'

'Binary: {0:b}'.format(324)
'Binary: 101000100'

