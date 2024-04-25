from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import os

def create_game_compatibility_report(game_title, os_requirements, cpu_requirements, gpu_requirements, ram_requirements, storage_requirements, additional_notes):
    # Create a new PDF document
    c = canvas.Canvas("game_compatibility_report.pdf", pagesize=letter)

    # Title
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, 700, f"Game Compatibility Report: {game_title}")

    # OS Requirements
    c.setFont("Helvetica", 14)
    c.drawString(50, 660, "Operating System Requirements:")
    for i, os_requirement in enumerate(os_requirements):
        c.drawString(70, 640 - i*20, f"- {os_requirement}")

    # CPU Requirements
    c.drawString(50, 580, "CPU Requirements:")
    c.drawString(70, 560, f"- {cpu_requirements}")

    # GPU Requirements
    c.drawString(50, 540, "GPU Requirements:")
    c.drawString(70, 520, f"- {gpu_requirements}")

    # RAM Requirements
    c.drawString(50, 500, "RAM Requirements:")
    c.drawString(70, 480, f"- {ram_requirements}")

    # Storage Requirements
    c.drawString(50, 460, "Storage Requirements:")
    c.drawString(70, 440, f"- {storage_requirements}")

    # Additional Notes
    c.drawString(50, 400, "Additional Notes:")
    for i, note in enumerate(additional_notes):
        c.drawString(70, 380 - i*20, f"- {note}")

    # Save the PDF
    c.save()

if __name__ == "__main__":
    # Example usage
    game_title = "Example Game"
    os_requirements = ["Windows 10", "macOS 10.15"]
    cpu_requirements = "Intel Core i5 or equivalent"
    gpu_requirements = "NVIDIA GTX 1060 or AMD Radeon RX 580"
    ram_requirements = "8 GB RAM"
    storage_requirements = "50 GB available space"
    additional_notes = ["Internet connection required for multiplayer", "DirectX 11 compatible"]

    create_game_compatibility_report(game_title, os_requirements, cpu_requirements, gpu_requirements, ram_requirements, storage_requirements, additional_notes)
