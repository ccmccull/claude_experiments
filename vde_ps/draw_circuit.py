"""Draw the loaded voltage divider schematic used in README.md."""

import schemdraw
import schemdraw.elements as elm

schemdraw.config(fontsize=13)

with schemdraw.Drawing(file="circuit.svg", show=False) as d:
    d.config(unit=2.5)

    src = elm.SourceV().up().label(r"$V_\mathrm{in}$" + "\n12 V", loc="top")
    elm.Line().right(0.75)
    r1 = elm.Resistor().right().label(r"$R_1$", loc="bottom")
    elm.CurrentLabel(top=True, length=1.2).at(r1).label(r"$i_1$")
    out = elm.Dot().label(r"$V_\mathrm{out}$", loc="top")

    r2 = elm.Resistor().down().label(r"$R_2$", loc="bottom")
    elm.CurrentLabel(top=False, length=1.2).at(r2).label(r"$i_2$")
    elm.Dot()
    elm.Line().left().tox(src.start)

    elm.Line().right(3).at(out.center)
    r3 = elm.Resistor().down().label(r"$R_3$" + "\n(load)", loc="bottom")
    elm.CurrentLabel(top=False, length=1.2).at(r3).label(r"$i_3$")
    elm.Line().left().to(r2.end)
    elm.Ground().at(r2.end)
