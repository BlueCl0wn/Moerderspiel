from reportlab.lib import colors
import reportlab.pdfgen.canvas as canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate


def print_text(_data: list[str], URI, n: tuple, border=cm):
    c = SimpleDocTemplate(URI, pagesize=A4, rightMargin=border, leftMargin=border, topMargin=0.8 * border,
                          bottomMargin=0.8 * border)
    c.build(_data)


def print_page(_data: list[str], URI, n: tuple, border, dim: tuple):
    """
    Saves a pdf with a table filled with the 2-dimensional list parsed. This table fills the whole page.

    :param dim:
    :param border:
    :param n:
    :param URI:
    :param _data: 2-dimensional list[str]
    :return: None
    """

    # create template
    c = SimpleDocTemplate(URI, pagesize=A4, rightMargin=border, leftMargin=border, topMargin=0.8 * border,
                          bottomMargin=0.8 * border)

    # Create table
    t = Table(_data, colWidths=n[0] * [dim[0]], rowHeights=len(_data[-1]) * [dim[1]])

    # Set table and font styles
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                           ]))

    # Build page
    c.build([t])


def print_pdf(data, URI: str, n: tuple = (6, 12), border=cm) -> None:
    """

    :param data:
    :param URI:
    :param n: n[1] > 5
    :param border:
    :return:
    """

    # the math ain't mathin'
    width_x = int((A4[0] - 2 * border) / n[0])
    height_y = int((A4[1] - 2 * border) / n[1])

    print_page(data, URI, n=n, border=border, dim=(width_x, height_y))


if __name__ == "__main__":
    pass
