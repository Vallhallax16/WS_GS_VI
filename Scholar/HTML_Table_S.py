import GetLinks
import Scholar

class HTML_Table_S:

    def htmlTableS(self):
        links = list()

        links = GetLinks.getLinksS()

        column_names = ['Nombre', 'Universidad', 'ID del Autor', 'Citas', 'Indice h', 'Documentos']

        # f = csv.writer(open('dataScorpus.csv', 'w', newline=''))

        lines = []
        lines.append('<!--START HERE S-->\n')
        lines.append('\t\t\t\t\t\t<table id="tableS" class="display">\n')
        lines.append('\t\t\t\t\t\t\t<thead>\n')
        lines.append('\t\t\t\t\t\t\t\t<tr class="table100-head">\n')
        column = 1
        for name in column_names:
            if column < 4:
                lines.append(f'\t\t\t\t\t\t\t\t\t<th class="column{column}">{name}</th>\n')
                column = column + 1
            else:
                lines.append(f'\t\t\t\t\t\t\t\t\t<th class="column{column + 1}">{name}</th>\n')
                column = column + 1
        lines.append('\t\t\t\t\t\t\t\t</tr>\n')
        lines.append('\t\t\t\t\t\t\t</thead>\n')
        lines.append('\t\t\t\t\t\t<tbody>\n')
        for link in links:
            nombre, universidad, author_id, citas, indiceh, documentos = Scholar.GetInfoS(link)

            print(nombre, universidad, author_id, citas, indiceh, documentos)
            # f.writerow([nombre, citas, indiceh, documentos])
            lines.append('\t\t\t\t\t\t\t\t<tr>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column1">{nombre}</td>\n')

            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column2">{universidad}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column3">{author_id}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column5">{citas}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column6">{indiceh}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column7">{documentos}</td>\n')
            lines.append('\t\t\t\t\t\t\t\t</tr>\n')

        lines.append('\t\t\t\t\t\t\t</tbody>\n')
        lines.append('\t\t\t\t\t\t</table>\n')
        lines.append('\t\t\t\t\t<!--END HERE S-->')

        return ''.join(lines)