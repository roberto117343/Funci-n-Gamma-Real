#* «Copyright 2022 Roberto Reinosa»
#*
#* This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#*

import matplotlib.pyplot as plt

def productorio(valor):

    resultado = 1

    for n in range(1, 30000):

        resultado *= pow((1.0 + (1.0/n)), valor)/(1.0 + (valor/n))

    return resultado


vector_x = []
vector_y = []

valor = -5.00001

while valor < 5.0:

    valor_funcion = (1.0/valor) * productorio(valor)

    if valor_funcion < 6.0:

        if valor_funcion > -6.0:

            vector_x.append(valor)
            vector_y.append(valor_funcion)

    valor += 0.00002

plt.scatter(vector_x, vector_y, s=1)

plt.axvline(0, c='black', ls='-')
plt.axhline(0, c='black', ls='-')

plt.xlim(-5.1, 5)
plt.ylim(-6.0, 6)

plt.show()
