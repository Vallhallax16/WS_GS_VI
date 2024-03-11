import csv
import GetLinks
import Scholar
import os

from CCamel_Case import Formato_camello as FC

class HTML_Table_GS:

    def htmlTableGS(self):
        links = list()
        nombres = list()
        imagenes = list()
        paises = list()

        links, nombres, imagenes = GetLinks.getLinksGS()
        column_names = ['Nombre', 'Universidad', 'Correo', 'Palabras Clave', 'Citas', 'Indice h', 'Indice i10','Link a imagen','País']

        f = None

        fc = FC()

        try:
            ruta_de_archivo = os.path.abspath("dataGS.csv")
            os.remove(ruta_de_archivo)

            f = csv.writer(open(ruta_de_archivo, 'w', newline=''))
        except:
            f = csv.writer(open(ruta_de_archivo, 'w', newline=''))

        f.writerow(column_names)

        lines = []
        lines.append('<!--INICIO_DEL_REEMPLAZO-->\n')
        lines.append('                <tbody>\n')

        pais = str()

        i = 0
        for link in links:
            citas, indiceh, indicei10, universidad, correo, palabras,pais = Scholar.GetInfoGS(link)
            f.writerow([fc.Formatear(nombres[i]), fc.Formateo_escaso(universidad),correo,palabras,citas, indiceh, indicei10, imagenes[i], pais])
            lines.append('                <tr>\n')
            lines.append(f'                    <td class="column0">'+ f'<a href="{link}">' + f'{fc.Formatear(nombres[i])}' + '</a>' +'</td>\n')
            lines.append(f'                    <td class="column1">{universidad}</td>\n')
            lines.append(f'                    <td class="column2">{fc.Formateo_escaso(palabras)}</td>\n')
            lines.append(f'                    <td class="column3">{citas}</td>\n')
            lines.append(f'                    <td class="column4">{indiceh}</td>\n')
            lines.append(f'                    <td class="column5">{indicei10}</td>\n')
            lines.append(f'                    <td class="column6">{pais}</td>\n')
            lines.append('                </tr>\n')
            i += 1

        lines.append('                </tbody>\n')
        lines.append('<!--FIN_DEL_REEMPLAZO-->\n')

        return ''.join(lines)