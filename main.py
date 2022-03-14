#!/usr/bin/env python3
# Soubor:  main.py
# Datum:   14.03.2022 13:24
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:
############################################################################

from pylab import plot, pi, sin, cos, figure
import pylab as pl

f = 50

# časová osa
t = pl.linspace(0, 50e-3, 444)

# napětí
u = cos(2 * pi * f * t + 0 * pi)

# proud
i = cos(2 * pi * f * t + pl.deg2rad(0))

# výkon
p = u * i

figure(1)
plot(t, u, label="napětí", color="green")
plot(t, i, label="proud", color="#dd6644")
plot(t, p, label="výkon")

pl.grid(True)
pl.legend()
pl.title("Výkon střídavého proudu")
pl.xlabel("t [s]")
pl.ylabel("u [V], i[A], p[W]")

pl.xlim(12e-3, 44e-3)
pl.ylim(-1.2, 1.4)

figure(2)
# dva řádky,dva sloupce, první graf
pl.subplot(2, 2, 1)
plot(t, u, ":", label="napětí")

# dva řádky,dva sloupce, druhý graf
pl.subplot(2, 2, 2)
plot(t, i, "--", label="proud")

# dva řádky,dva sloupce, třetí graf
pl.subplot(2, 2, 3)
plot(t, p, "-.", label="výkon")


pl.show()
