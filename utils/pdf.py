from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_ticket(path, username, uid, tournament):

    doc = SimpleDocTemplate(path)

    style = getSampleStyleSheet()["Normal"]

    doc.build([
        Paragraph("FF Tournament Ticket", style),
        Paragraph(f"Player: {username}", style),
        Paragraph(f"UID: {uid}", style),
        Paragraph(f"Tournament: {tournament}", style),
    ])
