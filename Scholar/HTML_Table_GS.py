import csv
import GetLinks
import Scholar
import os

class HTML_Table_GS:

    def htmlTableGS(self):
        links = list()
        nombres = list()
        imagenes = list()

        links, nombres, imagenes = GetLinks.getLinksGS()
        column_names = ['Nombre', 'Universidad', 'Correo', 'Palabras Clave', 'Citas', 'Indice h', 'Indice i10','Link a imagen']

        f = None

        try:
            ruta_de_archivo = os.path.abspath("dataGS.csv")
            os.remove("dataGS.csv")
            f = csv.writer(open('dataGS.csv', 'w', newline=''))
        except:
            f = csv.writer(open('dataGS.csv', 'w', newline=''))

        f.writerow(column_names)

        lines = []
        lines.append('<!--START HERE GS-->\n')
        lines.append('\t\t\t\t\t\t<table id="tableGS" class="display">\n')
        lines.append('\t\t\t\t\t\t\t<thead>\n')
        lines.append('\t\t\t\t\t\t\t\t<tr class="table100-head">\n')
        column = 0
        for name in column_names:
            lines.append(f'\t\t\t\t\t\t\t\t\t<th class="column{column}">{name}</th>\n')
            column += 1
        lines.append('\t\t\t\t\t\t\t\t</tr>\n')
        lines.append('\t\t\t\t\t\t\t</thead>\n')
        lines.append('\t\t\t\t\t\t<tbody>\n')

        i = 0
        for link in links:
            citas, indiceh, indicei10, universidad, correo, palabras = Scholar.GetInfoGS(link)
            f.writerow([nombres[i], universidad,correo,palabras,citas, indiceh, indicei10, imagenes[i]])
            lines.append('\t\t\t\t\t\t\t\t<tr>\n')
            lines.append(
                f'\t\t\t\t\t\t\t\t\t<td class="column0"><img alt="{nombres[i]}" sizes="54px" src="https://scholar.google.com{imagenes[i]}" width="54" height="56"></td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column1">{nombres[i]}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column2">{universidad}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column3">{correo}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column4">{palabras}</td>\n')

            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column5">{citas}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column6">{indiceh}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column7">{indicei10}</td>\n')
            lines.append('\t\t\t\t\t\t\t\t</tr>\n')
            i += 1

        lines.append('\t\t\t\t\t\t\t</tbody>\n')
        lines.append('\t\t\t\t\t\t</table>\n')
        lines.append('\t\t\t\t\t<!--END HERE GS-->')

        return ''.join(lines)