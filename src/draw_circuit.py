# Draw circuit
# https://schemdraw.readthedocs.io/en/latest/index.html

import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
d.add(elm.Line())
d.add(elm.Resistor())
d.add(elm.Inductor(d='down', label='L'))
d.add(elm.Capacitor(d='down', label='C'))
d.add(elm.Line(d='left'))

# d.add(elm.Capacitor(d='down', label='10$\mu$F'))
# d.add(elm.Line(d='left'))
# d.add(elm.SourceSin(d='up', label='10V'))

d.draw()
# d.save('basic_rc.svg')