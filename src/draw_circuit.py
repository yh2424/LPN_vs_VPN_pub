# Draw circuit
# https://schemdraw.readthedocs.io/en/latest/index.html

import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
d.add(elm.Line)
d.push()
d.add(elm.Capacitor(d='down',label='$C_0$'))
d.add(elm.Line(d='left'))
d.add(elm.SourceSin(d='up',reverse=True))
d.pop()
d.add(elm.RBox(d='right',label='$2R_1$'))
d.add(elm.Inductor(d='down',botlabel='$L_1$',l=2))
d.add(elm.Capacitor(label='$0.5C_1$',l=1))
d.add(elm.Line(d='left'))


d.draw()
# d.save('basic_rc.svg')

# 기본 l값 3
# Capacitor, Line ,Resigster, Inductor, RBox
# tox => 두가지 더함