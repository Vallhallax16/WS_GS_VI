import csv
import GetLinks
import Scholar
import os

class HTML_Table_GS:

    def htmlTableGS(self):
        links = list()
        nombres = list()
        imagenes = list()
        paises = list()

        links, nombres, imagenes = GetLinks.getLinksGS()
        column_names = ['Nombre', 'Universidad', 'Correo', 'Palabras Clave', 'Citas', 'Indice h', 'Indice i10','Link a imagen','País']

        f = None

        try:
            ruta_de_archivo = os.path.abspath("dataGS.csv")
            os.remove(ruta_de_archivo)

            f = csv.writer(open(ruta_de_archivo, 'w', newline=''))
        except:
            f = csv.writer(open(ruta_de_archivo, 'w', newline=''))

        f.writerow(column_names)

        lines = []
        lines.append('<!--START HERE GS-->\n')
        lines.append('\t\t\t\t\t\t<table id="tableGS" class="display">\n')
        lines.append('\t\t\t\t\t\t\t<thead>\n')
        lines.append('\t\t\t\t\t\t\t\t<tr class="table100-head">\n')
        column = 0
        for name in column_names:
            if(name != column_names[column_names.__len__()-1]):
                lines.append(f'\t\t\t\t\t\t\t\t\t<th class="column{column}">{name}</th>\n')
                column += 1
        lines.append('\t\t\t\t\t\t\t\t</tr>\n')
        lines.append('\t\t\t\t\t\t\t</thead>\n')
        lines.append('\t\t\t\t\t\t<tbody>\n')

        pais = str()

        i = 0
        for link in links:
            citas, indiceh, indicei10, universidad, correo, palabras,pais = Scholar.GetInfoGS(link)
            f.writerow([nombres[i], universidad,correo,palabras,citas, indiceh, indicei10, imagenes[i], pais])
            lines.append('\t\t\t\t\t\t\t\t<tr>\n')
            # lines.append(
            # f'\t\t\t\t\t\t\t\t\t<td class="column0"><img alt="{nombres[i]}" sizes="54px" src="https://scholar.google.com{imagenes[i]}" width="54" height="56"></td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column0">'+ f'<a href="{link}">' + f'{nombres[i]}' + '</a>' +'</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column1">{universidad}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column2">{palabras}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column3">{citas}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column4">{indiceh}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column5">{indicei10}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column6">{pais}</td>\n')
            lines.append('\t\t\t\t\t\t\t\t</tr>\n')
            i += 1

        lines.append('\t\t\t\t\t\t\t</tbody>\n')
        lines.append('\t\t\t\t\t\t</table>\n')
        lines.append('\t\t\t\t\t<!--END HERE GS-->')

        return ''.join(lines)