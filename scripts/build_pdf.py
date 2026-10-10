"""Build the explanatory note from its Markdown source with ReportLab."""

from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "papers" / "anaghs-law-note.md"
OUTPUT = ROOT / "output" / "pdf" / "anaghs-law-note.pdf"


def inline(text):
    """Convert the limited inline Markdown used in this note."""
    text = escape(text.replace("–", "-").replace("—", "-"))
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(
        r"https://[^\s<]+",
        lambda m: '<link href="' + m.group(0) + '" color="#0000bb">' + m.group(0) + "</link>",
        text,
    )
    return text


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 9)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(22 * mm, 14 * mm, "Anagh's Law | Original Formulation | 10 October 2026")
    canvas.drawRightString(A4[0] - 22 * mm, 14 * mm, str(doc.page))
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    body = ParagraphStyle("NoteBody", fontName="Times-Roman", fontSize=11, leading=14.4, spaceAfter=8)
    title = ParagraphStyle("NoteTitle", parent=body, fontName="Times-Bold", fontSize=23, leading=27, alignment=TA_CENTER, spaceAfter=9)
    subtitle = ParagraphStyle("NoteSubtitle", parent=body, fontSize=13, leading=16, alignment=TA_CENTER, spaceAfter=9)
    meta = ParagraphStyle("NoteMeta", parent=body, fontSize=10, alignment=TA_CENTER, spaceAfter=11)
    heading = ParagraphStyle("NoteHeading", parent=body, fontName="Times-Bold", fontSize=12.5, leading=16, spaceBefore=8, spaceAfter=5, keepWithNext=True)
    quote = ParagraphStyle("NoteQuote", parent=body, leftIndent=12, rightIndent=8, spaceBefore=3, spaceAfter=9)
    ref = ParagraphStyle("NoteReference", parent=body, fontSize=10, leading=13, splitLongWords=True)
    story = []
    for block in SOURCE.read_text().split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block == "<!-- pagebreak -->":
            story.append(PageBreak())
        elif block.startswith("# "):
            story.append(Paragraph(inline(block[2:]), title))
        elif block.startswith("## A Named"):
            story.append(Paragraph(inline(block[3:]), subtitle))
        elif block.startswith("## "):
            story.append(Paragraph(inline(block[3:]), heading))
        elif block.startswith("Anagh Kanungo |") or block == "*Clear the maximum, clear the rest.*":
            story.append(Paragraph(inline(block), meta))
        elif block.startswith("> "):
            story.append(Paragraph(inline(block[2:]), quote))
        elif re.match(r"\[\d+\] ", block):
            story.append(Paragraph(inline(block), ref))
        else:
            story.append(Paragraph(inline(block.replace("\n", " ")), body))
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=22 * mm, leftMargin=22 * mm,
                            topMargin=18 * mm, bottomMargin=23 * mm,
                            title="Anagh's Law: A Named Heuristic for Monotonic Feasibility Under Geometric Containment",
                            author="Anagh Kanungo", subject="Original Formulation, version 1.0.0; author-prepared explanatory note")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    main()
