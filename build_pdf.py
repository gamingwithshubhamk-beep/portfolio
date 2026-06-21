"""build_pdf.py — Compiles a professional PDF resume using reportlab based on Shubham's details."""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def build_resume_pdf():
    pdf_path = os.path.join(os.path.dirname(__file__), "resume.pdf")
    
    # 0.4 inch margins to fit on a single page perfectly
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=30,
        rightMargin=30,
        topMargin=25,
        bottomMargin=25
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    # Color palette
    primary_color = colors.HexColor("#0f172a") # Slate 900
    accent_color = colors.HexColor("#0284c7")  # Sky 600
    body_color = colors.HexColor("#334155")    # Slate 700
    
    name_style = ParagraphStyle(
        "NameStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=22,
        textColor=primary_color,
        alignment=1 # Center
    )
    
    tagline_style = ParagraphStyle(
        "TaglineStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=11,
        textColor=accent_color,
        alignment=1, # Center
        spaceBefore=3
    )
    
    contact_style = ParagraphStyle(
        "ContactStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=10,
        textColor=body_color,
        alignment=1, # Center
        spaceBefore=3
    )
    
    section_heading = ParagraphStyle(
        "SectionHeading",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=12,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=3
    )
    
    bold_body = ParagraphStyle(
        "BoldBody",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=primary_color
    )
    
    italic_body = ParagraphStyle(
        "ItalicBody",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8.5,
        leading=10.5,
        textColor=body_color
    )
    
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=body_color
    )
    
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=body_color,
        leftIndent=10,
        firstLineIndent=-6
    )

    story = []
    
    # 1. Header
    story.append(Paragraph("SHUBHAM KATHAVALE", name_style))
    story.append(Paragraph("COMPUTER SCIENCE ENGINEER &amp; AI SYSTEM DEVELOPER", tagline_style))
    
    contact_text = (
        "📍 Khopoli, Maharashtra, India  |  "
        "✉️ shubham18october@gmail.com  |  "
        "📞 +91 8055663307<br/>"
        "🔗 linkedin.com/in/shubham-kathavale-1b6a8b284  |  "
        "💻 github.com/ShubTriple7"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 4))
    
    # 2. Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=5))
    summary_text = (
        "Obsessed with bridging the gap between hardware automations and intelligent AI systems. "
        "Extensive hands-on experience building complex, event-driven desktop companions (J.A.R.V.I.S. Personal AI OS) "
        "and full-stack web applications. Passionate about AI integration, software engineering, and creating automated workflows. "
        "Looking for an internship or junior developer role where I can build production-grade software solutions."
    )
    story.append(Paragraph(summary_text, body))
    story.append(Spacer(1, 4))
    
    # 3. Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=5))
    
    skills_data = [
        [
            Paragraph("<b>Languages &amp; DBs:</b> Python, Java, JavaScript, HTML5, CSS3, SQL, MySQL, MongoDB, SQLite", body),
            Paragraph("<b>Frameworks &amp; Web:</b> React.js, Node.js, Express.js, Firebase, Tailwind CSS", body)
        ],
        [
            Paragraph("<b>AI &amp; Automation:</b> PySide6/Qt, RAG (FAISS), STT/TTS (Whisper), Subprocess, PyAutoGUI", body),
            Paragraph("<b>Domains:</b> AI &amp; Systems, Cloud Computing, Cyber Security, Software Engineering", body)
        ]
    ]
    skills_table = Table(skills_data, colWidths=[270, 270])
    skills_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))
    
    # 4. Projects
    story.append(Paragraph("PROJECTS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=5))
    
    # Jarvis
    story.append(Paragraph("<b>J.A.R.V.I.S. — Personal AI Operating System</b>", bold_body))
    story.append(Paragraph("<i>Stack: PySide6, Qt, QWebEngine, Groq API, SQLite, FAISS Vector DB, Next.js, Zustand, Framer Motion</i>", italic_body))
    story.append(Paragraph("• Developed an advanced voice-activated desktop assistant transitioning into a proactive operating system companion.", bullet_style))
    story.append(Paragraph("• Designed an <b>Event-Driven Multi-Agent Architecture</b> coordinating sub-units (Memory, Knowledge, Task, Desktop, Vision).", bullet_style))
    story.append(Paragraph("• Implemented <b>Cognitive Memory</b> using SQLite permanent store to track user context, facts, goals, and preferences.", bullet_style))
    story.append(Paragraph("• Integrated <b>Knowledge Intelligence</b> using RAG with FAISS vector indexing on local project files and documentation.", bullet_style))
    story.append(Paragraph("• Built the <b>V.A.U.L.T. HUD Dashboard</b> running on a PySide6 QWebEngineView window at 60 FPS.", bullet_style))
    # ARIA
    story.append(Paragraph("<b>ARIA — Agentic Reasoning &amp; Intelligence Assistant</b>", bold_body))
    story.append(Paragraph("<i>Stack: Python, WebSockets, Ollama (Qwen2.5:7b), Claude API, Playwright, HTML5/CSS3, Split Canvas</i>", italic_body))
    story.append(Paragraph("• Designed and built an autonomous agentic execution loop with real-time WebSocket thought streaming and action logging.", bullet_style))
    story.append(Paragraph("• Implemented a custom schema adapter translating Claude-style tool definitions to OpenAI/Ollama-compliant schemas.", bullet_style))
    story.append(Paragraph("• Developed a 7-tool system execution suite (web_search, read/write file, run_python, run_shell, call_api, Playwright browse).", bullet_style))
    story.append(Paragraph("• Engineered a futuristic glassmorphic split Canvas UI featuring a multi-file workspace selector and code/preview modes.", bullet_style))
    story.append(Spacer(1, 3))
    
    # SalonOS
    story.append(Paragraph("<b>SalonOS — Enterprise Salon Operating System</b>", bold_body))
    story.append(Paragraph("<i>Stack: Python 3.13, FastAPI, SQLite/PostgreSQL, SQLAlchemy, Role-Based Access Control, WebSockets, HTML5, Vanilla CSS3, WebGL, Chart.js</i>", italic_body))
    story.append(Paragraph("• Engineered a multi-tenant operating system backend isolating database records per tenant using foreign keys.", bullet_style))
    story.append(Paragraph("• Built a responsive client booking widget featuring an interactive WebGL canvas, before/after sliders, and a 7-step reservation wizard.", bullet_style))
    story.append(Paragraph("• Developed an administrative dashboard displaying today's business KPIs, polled live activity feeds, and channels simulator.", bullet_style))
    story.append(Paragraph("• Created a comprehensive integration test suite verifying JWT-based RBAC, stylist commissions, and checkout transaction logic.", bullet_style))
    story.append(Spacer(1, 3))

    # Evokn Fitness
    story.append(PageBreak())
    story.append(Paragraph("<b>Evokn Fitness — Full-Stack Fitness Tracker</b>", bold_body))
    story.append(Paragraph("<i>Stack: React.js, Node.js, Firebase, Tailwind CSS</i>", italic_body))
    story.append(Paragraph("• Designed and built a responsive full-stack fitness application to track calorie intake, macros, and workout sessions.", bullet_style))
    story.append(Paragraph("• Configured secure <b>Firebase Authentication</b> and managed a real-time Firestore database for user analytics.", bullet_style))
    story.append(Paragraph("• Integrated dynamic analytics charts using dashboard libraries to track weight loss progression and nutrient goals.", bullet_style))
    story.append(Paragraph("• Successfully debugged complex database synchronization issues and optimized client-side state management.", bullet_style))
    story.append(Spacer(1, 3))
    
    # Noisecity RP
    story.append(Paragraph("<b>Noisecity RP — GTA V FiveM Multiplayer Community</b>", bold_body))
    story.append(Paragraph("<i>Stack: FiveM API, LUA, SQL, QBCore framework</i>", italic_body))
    story.append(Paragraph("• Orchestrated and developed custom scripts for a GTA V Roleplay (RP) server serving a growing community.", bullet_style))
    story.append(Paragraph("• Managed database linkages via MySQL to track player assets, character vitals, and economy transactions.", bullet_style))
    story.append(Spacer(1, 4))
    
    # 5. Education
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=5))
    
    edu_data = [
        [
            Paragraph("<b>B.Tech in Computer Science &amp; Engineering</b> (Direct 2nd Yr / Lateral Entry)", bold_body),
            Paragraph("<b>Expected 2028</b>", ParagraphStyle("RightBold", parent=bold_body, alignment=2))
        ],
        [
            Paragraph("MIT World Peace University (MIT-WPU), Pune", italic_body),
            Paragraph("Pune, India", ParagraphStyle("RightItalic", parent=italic_body, alignment=2))
        ]
    ]
    edu_table = Table(edu_data, colWidths=[400, 140])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 3))
    
    dip_data = [
        [
            Paragraph("<b>Diploma in Computer Engineering</b>", bold_body),
            Paragraph("<b>Completed 2024</b>", ParagraphStyle("RightBold", parent=bold_body, alignment=2))
        ],
        [
            Paragraph("B.L. Patil Polytechnic | MSBTE Board (First Class with Distinction)", italic_body),
            Paragraph("Maharashtra, India", ParagraphStyle("RightItalic", parent=italic_body, alignment=2))
        ]
    ]
    dip_table = Table(dip_data, colWidths=[400, 140])
    dip_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(dip_table)
    story.append(Spacer(1, 4))
    
    # 6. Certifications & Courses
    story.append(Paragraph("LICENSES, CERTIFICATIONS &amp; COURSES", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=5))
    
    cert_text = (
        "• <b>Oracle Cloud Infrastructure 2025 Certified Foundations Associate</b> "
        "(Issued Aug 2025 · Expires Aug 2035  |  Credential ID: OC6817049)<br/>"
        "• <b>University Course: Bioscience Using Python Programming (BTU10010)</b> — MIT-WPU<br/>"
        "• <b>University Course: Business Analytics using Power BI (BBA20180)</b> — MIT-WPU"
    )
    story.append(Paragraph(cert_text, body))
    
    doc.build(story)
    print("PDF Resume generated successfully at:", pdf_path)

if __name__ == "__main__":
    build_resume_pdf()
