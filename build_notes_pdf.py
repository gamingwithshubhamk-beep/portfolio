"""build_notes_pdf.py — Compiles a professional PDF of interview notes using reportlab."""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor("#64748b")) # Slate 500
    
    # Page number
    page_num = canvas.getPageNumber()
    canvas.drawRightString(doc.pagesize[0] - 54, 30, f"Page {page_num}")
    
    # Header/Footer separator line
    canvas.setStrokeColor(colors.HexColor("#cbd5e1"))
    canvas.setLineWidth(0.5)
    canvas.line(54, 42, doc.pagesize[0] - 54, 42)
    
    # Left description
    canvas.drawString(54, 30, "Shubham Kathavale — Interview Preparation Notes & Resume Guide")
    canvas.restoreState()

def build_notes_pdf():
    pdf_path = os.path.join(os.path.dirname(__file__), "interview_prep_notes.pdf")
    
    # Standard 0.75-inch margins
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom palette
    primary_color = colors.HexColor("#0f172a") # Slate 900
    accent_color = colors.HexColor("#0284c7")  # Sky 600
    body_color = colors.HexColor("#334155")    # Slate 700
    
    title_style = ParagraphStyle(
        "NotesTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        "NotesSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=accent_color,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        "Heading1",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        "Heading2",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=accent_color,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        "BodyText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=body_color,
        spaceAfter=8
    )
    
    bullet_style = ParagraphStyle(
        "BulletText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=body_color,
        leftIndent=15,
        firstLineIndent=-8,
        spaceAfter=5
    )
    
    story = []
    
    # Title Header
    story.append(Paragraph("Shubham Kathavale", title_style))
    story.append(Paragraph("<b>INTERVIEW PREPARATION & RESUME CHEAT SHEET</b>", subtitle_style))
    
    # 1. Elevator Pitch
    story.append(Paragraph("1. The 90-Second Elevator Pitch (Self-Introduction)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10, spaceBefore=2))
    
    story.append(Paragraph(
        "When an interviewer opens with <i>\"Tell me about yourself,\"</i> use this structured template to establish your core technical and personal traits:",
        body_style
    ))
    
    story.append(Paragraph(
        "• <b>Hook (Present):</b> \"I am a Computer Science & Engineering student at MIT-WPU, Pune, specializing in system automation, multi-agent AI environments, and full-stack development. My main focus is bridging the gap between intelligence engines and robust developer tools.\"",
        bullet_style
    ))
    
    story.append(Paragraph(
        "• <b>Background (Past):</b> \"I completed my Diploma in Computer Engineering with First Class Distinction from B.L. Patil Polytechnic, MSBTE. This built my core computing and database foundations. Following my diploma, I secured direct second-year entry into MIT-WPU where I've continued to build systems from the ground up.\"",
        bullet_style
    ))
    
    story.append(Paragraph(
        "• <b>Key Projects (Proof):</b> \"Most notably, I built J.A.R.V.I.S.—a proactive Personal AI Operating System using a PySide6 Qt GUI, a glassmorphic Next.js dashboard, and a local agentic brain with vector RAG search (using FAISS) and SQLite cognitive memory graphs. I’ve also built Evokn Fitness, a full-stack macro tracker, and developed custom multiplayer scripts on MySQL backend for GTA V servers.\"",
        bullet_style
    ))
    
    story.append(Paragraph(
        "• <b>Behavioral Edge (Discipline):</b> \"What truly defines my execution style is consistency and self-discipline. I lost 30 kg during a dedicated fitness phase—a challenge that built high standards of planning, metrics tracking, and commitment that I bring directly into my engineering and code quality.\"",
        bullet_style
    ))
    
    story.append(Paragraph(
        "• <b>The Goal (Conclusion):</b> \"I am looking for an internship or junior developer role where I can solve database scale issues, coordinate system pipelines, and contribute to production-ready products.\"",
        bullet_style
    ))
    
    story.append(Spacer(1, 10))
    
    # 2. Project Deep-Dives
    story.append(Paragraph("2. Project Deep-Dives (STAR Method)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10, spaceBefore=2))
    
    # Jarvis
    story.append(Paragraph("A. J.A.R.V.I.S. — Personal AI Operating System", h2_style))
    story.append(Paragraph(
        "<b>Situation:</b> Needed to evolve a standard reactive voice assistant into a proactive desktop operating companion that understands user files, goals, and habits.<br/>"
        "<b>Task:</b> Create an event-driven system coordinating specialized agents (Task, Knowledge, Memory, Vision, Desktop) concurrently, managing RAG and local permanent state.<br/>"
        "<b>Action:</b> Built a PySide6 loop hosting Next.js QWebEngineView at 60 FPS. Configured RAG using local FAISS vector databases on repository codebase directories. Created permanent cognitive context using SQLite.<br/>"
        "<i>Key Challenge:</i> Headless coordination of agents without infinite loop callbacks.<br/>"
        "<i>Solution:</i> Implemented a central orchestrator pattern routing events asynchronously via local loop callbacks.<br/>"
        "<b>Result:</b> Under 5% CPU idle load and under 300ms local RAG retrieval latency.",
        body_style
    ))
    
    # Evokn Fitness
    story.append(Paragraph("B. Evokn Fitness — Full-Stack Fitness Tracker", h2_style))
    story.append(Paragraph(
        "<b>Situation:</b> Needed an intuitive application to log workout analytics, calories, and weight targets.<br/>"
        "<b>Task:</b> Develop a responsive full-stack platform with dashboard charts, macro logs, and secure user profiles.<br/>"
        "<b>Action:</b> Programmed frontend in React.js/Tailwind. Handled storage and profiles via Firebase Firestore and Authentication.<br/>"
        "<i>Key Challenge:</i> Firestore state synchronization conflicts on rapid consecutive macronutrient inputs.<br/>"
        "<i>Solution:</i> Implemented client-side optimistic updates and debounced database write operations.<br/>"
        "<b>Result:</b> Eliminated state thrashing; achieved sub-second client latency and smooth mobile responsiveness.",
        body_style
    ))
    
    story.append(PageBreak()) # Clean page break for second section
    
    # Noisecity RP
    story.append(Paragraph("C. Noisecity RP — GTA V FiveM Server Scripting", h2_style))
    story.append(Paragraph(
        "<b>Situation:</b> Managed custom roleplay gameplay features and economy transactions for an active multiplayer community.<br/>"
        "<b>Task:</b> Store and link player assets and vitals dynamically without introducing game thread latency.<br/>"
        "<b>Action:</b> Wrote game logic using Lua and FiveM APIs. Integrated server endpoints with a remote MySQL database.<br/>"
        "<i>Key Challenge:</i> High-frequency transactional writes from 100+ concurrent players causing locks.<br/>"
        "<i>Solution:</i> Cached player vitals in server memory and implemented structured bulk commits every 5 minutes.<br/>"
        "<b>Result:</b> Reduced database connection overhead by 80%, maintaining server tick rates at a smooth 60 FPS.",
        body_style
    ))
    
    story.append(Spacer(1, 10))
    
    # 3. Core Academic Cheat Sheet
    story.append(Paragraph("3. Core Academic Concepts (Syllabus Prep)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10, spaceBefore=2))
    
    story.append(Paragraph(
        "MIT-WPU exams prefer structured answers: <b>Definition, Example, Working/Key Points, Applications, Conclusion, Memory Trick</b>. Use these structures during technical questions:",
        body_style
    ))
    
    # DAA
    story.append(Paragraph("A. Design & Analysis of Algorithms (DAA)", h2_style))
    story.append(Paragraph(
        "• <b>Dynamic Programming (DP):</b> Breaks problems into overlapping subproblems, solves each once, and stores results (Memoization/Tabulation) to avoid duplicate computation. (e.g. Fibonacci, 0/1 Knapsack, Floyd-Warshall).<br/>"
        "<i>Memory Trick:</i> <b>DP = Divide and Preserve</b> (Store sub-answers).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Greedy Algorithms:</b> Makes the locally optimal choice at each step to find a global optimum. Fast but doesn't guarantee a global optimum. (e.g. Dijkstra, Fractional Knapsack, Prim's).<br/>"
        "<i>Memory Trick:</i> <b>Greedy = Grab Immediately</b> (Short-sighted but fast).",
        bullet_style
    ))
    
    # DBMS
    story.append(Paragraph("B. Database Management Systems (DBMS)", h2_style))
    story.append(Paragraph(
        "• <b>ACID Properties:</b><br/>"
        "  - <i>Atomicity:</i> Transactions are all-or-nothing.<br/>"
        "  - <i>Consistency:</i> Keeps database schema valid from start to end.<br/>"
        "  - <i>Isolation:</i> Concurrent transactions do not overwrite or conflict.<br/>"
        "  - <i>Durability:</i> Once committed, data is safe from crashes.<br/>"
        "<i>Memory Trick:</i> <b>ACID = Atomic, Consistent, Isolated, Durable</b>.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Normalization Levels:</b><br/>"
        "  - <i>1NF:</i> Atomic column values (no nested array arrays/repeating groups).<br/>"
        "  - <i>2NF:</i> 1NF + no partial dependency (every attribute depends on the entire candidate key).<br/>"
        "  - <i>3NF:</i> 2NF + no transitive dependency (non-keys rely only on keys, not other non-keys).",
        bullet_style
    ))
    
    # Data Structures & MMA
    story.append(Paragraph("C. Data Structures & Microprocessors", h2_style))
    story.append(Paragraph(
        "• <b>Hash Tables:</b> Achieves average $O(1)$ search and insertion. Collision resolution is handled via Chaining (linked lists) or Open Addressing (probing).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Microprocessor registers (MMA):</b> Small, high-speed storage locations within the CPU. Work with instruction pipelines, memory fetch phases, and hardware interrupts.",
        bullet_style
    ))
    
    story.append(Spacer(1, 10))
    
    # 4. Behavioral Questions
    story.append(Paragraph("4. Behavioral Questions & Personal Discipline", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10, spaceBefore=2))
    
    story.append(Paragraph(
        "• <b>How do you manage deadlines and focus?</b><br/>"
        "\"My 30 kg weight loss journey required strict self-tracking, consistent execution, and objective goal-setting. I translate this exact strategy into software engineering by breaking goals down into sprints, using issue trackers, and logging systems metrics.\"",
        bullet_style
    ))
    
    story.append(Paragraph(
        "• <b>How do you learn new technologies?</b><br/>"
        "\"I completed my Diploma with distinction while simultaneously self-studying Web/AI systems. For JARVIS OS, I learned PySide6 Qt bindings, asynchronous event queues, and vector index RAG architectures. I learn by researching documentation, compiling prototypes, and debugging implementation limits.\"",
        bullet_style
    ))
    
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print("Interview Notes PDF generated successfully at:", pdf_path)

if __name__ == "__main__":
    build_notes_pdf()
