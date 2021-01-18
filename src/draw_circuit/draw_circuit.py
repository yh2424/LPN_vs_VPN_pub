# Draw circuit
# https://schemdraw.readthedocs.io/en/latest/index.html
import schemdraw
import schemdraw.elements as elm

#Circuit normal
d = schemdraw.Drawing()
d.add(elm.Line)
d.push()
d.add(elm.Capacitor(d='down',label='$C_0$'))
d.add(elm.Line(d='left'))
d.add(elm.SourceSin(d='up',reverse=True,l=1.5))
d.add(elm.Resistor(d='up',l=1.5,label='$Z_s$'))
d.pop()
d.add(elm.RBox(d='right',label='$R_s$'))
d.add(elm.Inductor(d='down',botlabel='$L$',l=2))
d.add(elm.Capacitor(label='$C_j$',l=1))
d.add(elm.Line(d='left'))

d.draw()
d.save('normal.svg')


#Circuit SD
d = schemdraw.Drawing()
d.add(elm.Line)
d.push()
d.add(elm.Capacitor(d='down',label='$C_0$'))
d.add(elm.Line(d='left'))
d.add(elm.SourceSin(d='up',reverse=True,l=1.5))
d.add(elm.Resistor(d='up',l=1.5,label='$Z_s$'))
d.pop()
d.add(elm.RBox(d='right',label='$2R_s$'))
d.add(elm.Inductor(d='down',botlabel='$L$',l=2))
d.add(elm.Capacitor(label='$0.5C_j$',l=1))
d.add(elm.Line(d='left'))

d.draw()
d.save('sd.svg')


# 기본 l값 3
# Capacitor, Line ,Resigster, Inductor, RBox
# tox => 두가지 더함