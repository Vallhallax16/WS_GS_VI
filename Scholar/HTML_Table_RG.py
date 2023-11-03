import GetLinks
import Scholar

class HTML_Table_RG:
    def htmlTableRG(self):
        links = list()

        links = GetLinks.getLinksRG()

        column_names = ['Nombre', 'Universidad', 'Posición', 'Citas','Lecturas','Investigaciones']

        lines = []
        lines.append('<!--START HERE RG-->\n')
        lines.append('\t\t\t\t\t\t<table id="tableRG" class="display">\n')
        lines.append('\t\t\t\t\t\t\t<thead>\n')
        lines.append('\t\t\t\t\t\t\t\t<tr class="table100-head">\n')
        column = 1
        for name in column_names:
            if column==3:
                column = column + 1
            else:
                lines.append(f'\t\t\t\t\t\t\t\t\t<th class="column{column}">{name}</th>\n')
                column = column + 1
        lines.append('\t\t\t\t\t\t\t\t</tr>\n')
        lines.append('\t\t\t\t\t\t\t</thead>\n')
        lines.append('\t\t\t\t\t\t<tbody>\n')
        for link in links:
            nombre,universidad,posicion,citas,lecturas,investigaciones = Scholar.GetInfoRG(link)

            lines.append('\t\t\t\t\t\t\t\t<tr>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column1">{nombre}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column2">{universidad}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column4">{posicion}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column5">{citas}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column6">{lecturas}</td>\n')
            lines.append(f'\t\t\t\t\t\t\t\t\t<td class="column7">{investigaciones}</td>\n')
            lines.append('\t\t\t\t\t\t\t\t</tr>\n')

        lines.append('\t\t\t\t\t\t\t</tbody>\n')
        lines.append('\t\t\t\t\t\t</table>\n')
        lines.append('\t\t\t\t\t<!--END HERE RG-->')

        return ''.join(lines)