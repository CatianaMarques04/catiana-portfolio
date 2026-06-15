import flet as ft
import os, shutil, json
from datetime import datetime

BG    = "#0A0A0A"
CARD  = "#111111"
CARD2 = "#1A1A1A"
BDR   = "#2A2A2A"
GOLD  = "#C9A84C"
GOLDL = "#E2C47A"
TEXT  = "#F0F0F0"
SUBS  = "#888888"
RED   = "#C0392B"

BASE  = os.path.dirname(os.path.abspath(__file__))
UPL   = os.path.join(BASE, "uploads")
MDIR  = os.path.join(UPL, "matlab_certificates")
BDIR  = os.path.join(UPL, "blog_videos")
GDIR  = os.path.join(UPL, "github_evidence")
DFILE = os.path.join(UPL, "data.json")

for d in [MDIR, BDIR, GDIR]:
    os.makedirs(d, exist_ok=True)

def load():
    try:
        with open(DFILE) as f: return json.load(f)
    except: return {"matlab":[], "blog":[], "github":[]}

def save(db):
    with open(DFILE,"w") as f: json.dump(db,f,indent=2)

def cp(src, dst):
    n = datetime.now().strftime("%Y%m%d_%H%M%S_") + os.path.basename(src)
    d = os.path.join(dst, n); shutil.copy2(src,d); return d

def bdr(w=1, c=None):
    c = c or BDR
    s = ft.BorderSide(w, c)
    return ft.Border(top=s, bottom=s, left=s, right=s)

def main(page: ft.Page):
    page.title   = "Catiana Marques | Portfolio"
    page.bgcolor = BG
    page.padding = 0
    db = load()

    # ── WIDGETS ────────────────────────────────────────
    def div():
        return ft.Container(height=2, bgcolor=GOLD, border_radius=1, margin=8)

    def h(t):
        return ft.Text(t, size=20, weight=ft.FontWeight.BOLD, color=GOLD)

    def sub(t):
        return ft.Text(t, size=12, color=SUBS)

    def tag(t):
        return ft.Container(
            content=ft.Text(t, size=11, color=GOLD),
            bgcolor=CARD2, border_radius=20, padding=ft.Padding(12,5,12,5),
            border=bdr(1, GOLD))

    def card(ctrl, padding=16):
        return ft.Container(
            content=ctrl, bgcolor=CARD, border_radius=12,
            padding=padding, margin=12,
            border=bdr())

    def gbtn(lbl, fn, ico=None):
        row = [ft.Text(lbl, color="#000000", weight=ft.FontWeight.W_600, size=13)]
        if ico: row.insert(0, ft.Icon(ico, color="#000000", size=15))
        return ft.ElevatedButton(
            content=ft.Row(row, tight=True, spacing=6),
            bgcolor=GOLD, on_click=fn,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)))

    def obtn(lbl, fn, ico=None):
        row = [ft.Text(lbl, color=GOLD, size=13)]
        if ico: row.insert(0, ft.Icon(ico, color=GOLD, size=15))
        return ft.OutlinedButton(
            content=ft.Row(row, tight=True, spacing=6),
            on_click=fn,
            style=ft.ButtonStyle(
                side=ft.BorderSide(1, GOLD),
                shape=ft.RoundedRectangleBorder(radius=8)))

    def dbtn(fn):
        return ft.IconButton(ft.icons.DELETE_OUTLINE, icon_color=RED, on_click=fn)

    def stat_box(value, label):
        return ft.Container(
            content=ft.Column([
                ft.Text(value, size=22, weight=ft.FontWeight.BOLD, color=GOLD,
                        text_align=ft.TextAlign.CENTER),
                ft.Text(label, size=10, color=SUBS, text_align=ft.TextAlign.CENTER),
            ], spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=CARD2, border_radius=10, padding=14, expand=True,
            border=bdr())

    # ── ABOUT ──────────────────────────────────────────
    def build_about():
        # Try jpg first, then png
        photo_jpg = os.path.join(BASE, "assets", "my_photo.jpg")
        photo_png = os.path.join(BASE, "assets", "my_photo.png")
        if os.path.exists(photo_jpg):
            photo_src = photo_jpg
            has_photo = True
        elif os.path.exists(photo_png):
            photo_src = photo_png
            has_photo = True
        else:
            has_photo = False

        av = ft.Container(
            content=ft.Image(src=photo_src, width=110, height=110,
                             fit=ft.ImageFit.COVER, border_radius=55)
                    if has_photo else
                    ft.Text("CM", size=40, weight=ft.FontWeight.BOLD, color=GOLD,
                            text_align=ft.TextAlign.CENTER),
            width=110, height=110, border_radius=55,
            border=bdr(3, GOLD),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            bgcolor=CARD2,
            alignment=ft.Alignment(0, 0))

        matlab_count = len(db["matlab"])
        blog_count   = len(db["blog"])
        github_count = len(db["github"])

        return ft.Column([
            ft.Container(height=10),
            # Hero banner
            ft.Container(
                content=ft.Column([
                    ft.Container(height=24),
                    ft.Row([av], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(height=14),
                    ft.Text("Catiana Marques", size=28, weight=ft.FontWeight.BOLD,
                            color=TEXT, text_align=ft.TextAlign.CENTER),
                    ft.Text("Electronics & Computer Engineering  ·  Year 2",
                            size=13, color=GOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text("Passionate about technology and innovation",
                            size=12, color=SUBS, text_align=ft.TextAlign.CENTER,
                            italic=True),
                    ft.Container(height=16),
                    ft.Row([
                        tag("Python"), tag("MATLAB"), tag("Electronics"),
                        tag("GitHub"), tag("Flet"),
                    ], alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=8),
                    ft.Container(height=24),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=CARD, border_radius=16,
                border=bdr(1, GOLD),
                margin=12),

            # Stats row
            ft.Row([
                stat_box(f"{matlab_count}/10", "Certificates"),
                ft.Container(width=10),
                stat_box(str(blog_count),   "Blog Posts"),
                ft.Container(width=10),
                stat_box(str(github_count), "Commits"),
            ]),

            ft.Container(height=4),
            card(ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.PERSON_OUTLINE, color=GOLD, size=20),
                    ft.Container(width=8),
                    h("About Me"),
                ]),
                ft.Container(height=8),
                ft.Text(
                    "Hi! I'm Catiana Marques, a second-year Electronics and "
                    "Computer Engineering student at university, driven by a "
                    "passion for technology and innovation. I enjoy building "
                    "software, exploring electronics, and solving real-world "
                    "engineering problems. This portfolio documents my individual "
                    "contributions to our semester group project, my MATLAB "
                    "certifications, and my journey as a programmer.",
                    size=14, color=TEXT),
            ])),

            card(ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.SCHOOL_OUTLINED, color=GOLD, size=20),
                    ft.Container(width=8),
                    h("Education"),
                ]),
                ft.Container(height=10),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("🎓 Degree", size=11, color=SUBS),
                            ft.Text("B.Eng Electronics & Computer Engineering",
                                    size=13, color=TEXT, weight=ft.FontWeight.W_500),
                        ], spacing=3),
                        expand=True),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("📅 Year", size=11, color=SUBS),
                            ft.Text("2nd Year  ·  2026", size=13, color=TEXT,
                                    weight=ft.FontWeight.W_500),
                        ], spacing=3),
                        expand=True),
                ]),
                ft.Container(height=8),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("💻 Course", size=11, color=SUBS),
                            ft.Text("Computer Programming I", size=13, color=TEXT,
                                    weight=ft.FontWeight.W_500),
                        ], spacing=3),
                        expand=True),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("⚙️ Specialisation", size=11, color=SUBS),
                            ft.Text("Metallurgical / Mining / Civil Modules",
                                    size=13, color=TEXT, weight=ft.FontWeight.W_500),
                        ], spacing=3),
                        expand=True),
                ]),
            ])),

            card(ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.TIMELINE, color=GOLD, size=20),
                    ft.Container(width=8),
                    h("Project Timeline"),
                ]),
                ft.Container(height=8),
                ft.Text("Weekly log of my contributions to the group project:",
                        size=12, color=SUBS),
                ft.Container(height=8),
                *[ft.Container(
                    content=ft.Row([
                        ft.Container(
                            content=ft.Text(f"Week {w}", size=11,
                                            color="#000000", weight=ft.FontWeight.BOLD),
                            bgcolor=GOLD, border_radius=6,
                            padding=ft.Padding(8,4,8,4),
                            width=70),
                        ft.Container(width=10),
                        ft.Text(task, size=12, color=TEXT, expand=True),
                    ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=CARD2, border_radius=8, padding=10,
                    margin=6, border=bdr())
                  for w, task in [
                    (1,  "Project setup, repository creation and folder structure"),
                    (2,  "Developed Metallurgical cost input module"),
                    (3,  "Implemented data validation and error handling"),
                    (4,  "GitHub pull requests, code reviews and merges"),
                    (5,  "Technical blog writing and MATLAB course completion"),
                    (6,  "Final testing, documentation and portfolio deployment"),
                ]],
            ])),
        ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)

    # ── MATLAB ─────────────────────────────────────────
    mcol  = ft.Column(spacing=0)
    mcnt  = ft.Text(f"{len(db['matlab'])} / 10 uploaded", color=SUBS, size=13)
    mname = ft.TextField(
        label="Certificate Name  (e.g. MATLAB Onramp)",
        bgcolor=CARD2, border_color=BDR, focused_border_color=GOLD,
        color=TEXT, label_style=ft.TextStyle(color=SUBS), border_radius=8)

    def rmx():
        mcol.controls.clear()
        for i, e in enumerate(db["matlab"]):
            idx = i
            num = ft.Container(
                content=ft.Text(str(i+1), size=12,
                                color="#000000", weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER),
                bgcolor=GOLD, border_radius=20, width=28, height=28,
                alignment=ft.Alignment(0, 0))
            mcol.controls.append(ft.Container(
                content=ft.Row([
                    num,
                    ft.Container(width=6),
                    ft.Icon(ft.icons.WORKSPACE_PREMIUM, color=GOLD, size=22),
                    ft.Column([
                        ft.Text(e["name"], size=13, weight=ft.FontWeight.W_600, color=TEXT),
                        ft.Text(e["date"]+" · "+e["file"], size=11, color=SUBS),
                    ], expand=True, spacing=2),
                    dbtn(lambda ev, i=idx: [db["matlab"].pop(i), save(db), rmx(), page.update()]),
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
                bgcolor=CARD2, border_radius=10, padding=12,
                border=bdr(), margin=8))
        c = len(db["matlab"])
        mcnt.value = f"{c} / 10 certificates uploaded"
        mcnt.color = GOLD if c >= 10 else SUBS
        page.update()

    def on_mp(e):
        if not e.files: return
        f = e.files[0]
        name = mname.value.strip() or f.name
        # web mode: path may be empty, store name only
        stored = ""
        if f.path:
            try: stored = cp(f.path, MDIR)
            except: stored = f.name
        else:
            stored = f.name
        db["matlab"].append({"name": name, "file": f.name,
                             "path": stored,
                             "date": datetime.now().strftime("%d %b %Y")})
        save(db); mname.value = ""; rmx()

    mpick = ft.FilePicker()
    mpick.on_result = on_mp
    page.overlay.append(mpick)

    def build_matlab():
        return ft.Column([
            ft.Container(height=10),
            ft.Row([ft.Icon(ft.icons.SCHOOL, color=GOLD, size=22),
                    ft.Container(width=8), h("📐 MATLAB Achievement Hub")]),
            sub("Upload your MathWorks Learning Center completion certificates."),
            ft.Container(height=6),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.icons.INFO_OUTLINE, color=GOLD, size=16),
                    ft.Container(width=6),
                    mcnt,
                ]),
                bgcolor=CARD2, border_radius=8, padding=10, border=bdr(1, GOLD)),
            ft.Container(height=8),
            div(),
            card(ft.Column([
                ft.Text("Upload New Certificate", size=14,
                        weight=ft.FontWeight.W_600, color=GOLD),
                sub("Accepted formats: PDF, PNG, JPG"),
                ft.Container(height=10), mname, ft.Container(height=10),
                gbtn("Choose Certificate File",
                     lambda _: mpick.pick_files(
                         allowed_extensions=["pdf","png","jpg","jpeg"]),
                     ft.icons.UPLOAD_FILE),
            ])),
            ft.Container(height=4),
            ft.Text("Uploaded Certificates", size=13, color=SUBS),
            ft.Container(height=6),
            mcol,
        ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)

    # ── BLOG ───────────────────────────────────────────
    bcol   = ft.Column(spacing=0)
    btitle = ft.TextField(
        label="Post Title", bgcolor=CARD2, border_color=BDR,
        focused_border_color=GOLD, color=TEXT,
        label_style=ft.TextStyle(color=SUBS), border_radius=8)
    bdesc  = ft.TextField(
        label="Technical Explanation / Confidence in Concepts",
        bgcolor=CARD2, border_color=BDR, focused_border_color=GOLD,
        color=TEXT, label_style=ft.TextStyle(color=SUBS),
        border_radius=8, multiline=True, min_lines=5, max_lines=10)
    bvlbl  = ft.Text("No video selected", size=12, color=SUBS, italic=True)
    bvp    = {"v": None, "n": None}

    def rbx():
        bcol.controls.clear()
        for i, e in enumerate(db["blog"]):
            idx = i
            bcol.controls.append(ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            content=ft.Icon(ft.icons.PLAY_CIRCLE_FILL,
                                            color="#000000", size=18),
                            bgcolor=GOLD, border_radius=8, padding=6),
                        ft.Container(width=8),
                        ft.Column([
                            ft.Text(e["title"], size=14,
                                    weight=ft.FontWeight.W_600, color=TEXT),
                            ft.Text(e["date"], size=11, color=SUBS),
                        ], expand=True, spacing=2),
                        dbtn(lambda ev, i=idx: [db["blog"].pop(i), save(db), rbx(), page.update()]),
                    ], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Text(e["desc"], size=12, color=TEXT),
                        bgcolor=CARD2, border_radius=8, padding=12, border=bdr()),
                    ft.Container(height=6),
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.icons.VIDEO_FILE, color=GOLD, size=14),
                            ft.Container(width=4),
                            ft.Text(e["file"], size=11, color=GOLD, italic=True),
                        ]),
                        bgcolor=CARD2, border_radius=6, padding=8),
                ]),
                bgcolor=CARD, border_radius=12, padding=14,
                border=bdr(1, GOLD), margin=10))
        page.update()

    def on_bp(e):
        if not e.files: return
        f = e.files[0]
        bvp["v"] = f.path if f.path else f.name
        bvp["n"] = f.name
        bvlbl.value = f"✅  {f.name}"; bvlbl.color = GOLD
        page.update()

    def save_blog(_):
        if not btitle.value.strip():
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Enter a post title."), bgcolor=RED)
            page.snack_bar.open = True; page.update(); return
        if not bvp["v"]:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Please select a video file."), bgcolor=RED)
            page.snack_bar.open = True; page.update(); return
        stored = ""
        try:
            if bvp["v"] and os.path.exists(bvp["v"]): stored = cp(bvp["v"], BDIR)
            else: stored = bvp["n"]
        except: stored = bvp["n"]
        db["blog"].append({
            "title": btitle.value.strip(), "desc": bdesc.value.strip(),
            "file": bvp["n"], "path": stored,
            "date": datetime.now().strftime("%d %b %Y")})
        save(db); btitle.value = ""; bdesc.value = ""
        bvp["v"] = None; bvp["n"] = None
        bvlbl.value = "No video selected"; bvlbl.color = SUBS; rbx()

    bpick = ft.FilePicker()
    bpick.on_result = on_bp
    page.overlay.append(bpick)

    def build_blog():
        return ft.Column([
            ft.Container(height=10),
            ft.Row([ft.Icon(ft.icons.VIDEO_LIBRARY, color=GOLD, size=22),
                    ft.Container(width=8), h("🎬 Technical Blog")]),
            sub("Upload videos explaining your contributions and core programming concepts."),
            ft.Container(height=8), div(),
            card(ft.Column([
                ft.Text("✍️  New Blog Post", size=14,
                        weight=ft.FontWeight.W_600, color=GOLD),
                ft.Container(height=10), btitle,
                ft.Container(height=8), bdesc,
                ft.Container(height=10),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Mathematical Notation Example:",
                                size=11, color=SUBS),
                        ft.Container(height=4),
                        ft.Text("Total Cost = Σᵢ₌₁ⁿ (Qᵢ × Pᵢ) + Overheads",
                                size=14, color=GOLD, weight=ft.FontWeight.W_500),
                    ]),
                    bgcolor=CARD2, border_radius=8, padding=12, border=bdr(1, GOLD)),
                ft.Container(height=12),
                ft.Row([
                    obtn("📹  Choose Video File",
                         lambda _: bpick.pick_files(
                             allowed_extensions=["mp4","mov","avi","mkv","webm"]),
                         ft.icons.VIDEO_CAMERA_BACK),
                    ft.Container(width=10),
                    bvlbl,
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=12),
                gbtn("💾  Save Blog Post", save_blog, ft.icons.SAVE),
            ])),
            ft.Text("Published Posts", size=13, color=SUBS),
            ft.Container(height=6),
            bcol,
        ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)

    # ── GITHUB ─────────────────────────────────────────
    gcol  = ft.Column(spacing=0)
    gcomm = ft.TextField(
        label="Commit / PR Title", bgcolor=CARD2, border_color=BDR,
        focused_border_color=GOLD, color=TEXT,
        label_style=ft.TextStyle(color=SUBS), border_radius=8)
    gimp  = ft.TextField(
        label="Impact Summary — how did your code solve a problem?",
        bgcolor=CARD2, border_color=BDR, focused_border_color=GOLD,
        color=TEXT, label_style=ft.TextStyle(color=SUBS),
        border_radius=8, multiline=True, min_lines=3, max_lines=6)
    gilbl = ft.Text("No screenshot selected", size=12, color=SUBS, italic=True)
    gip   = {"v": None, "n": None}

    def rgx():
        gcol.controls.clear()
        for i, e in enumerate(db["github"]):
            idx = i
            gcol.controls.append(ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            content=ft.Icon(ft.icons.COMMIT, color="#000000", size=16),
                            bgcolor=GOLD, border_radius=8, padding=6),
                        ft.Container(width=8),
                        ft.Column([
                            ft.Text(e["commit"], size=13,
                                    weight=ft.FontWeight.W_600, color=TEXT),
                            ft.Text(e["date"], size=11, color=SUBS),
                        ], expand=True, spacing=2),
                        dbtn(lambda ev, i=idx: [db["github"].pop(i), save(db), rgx(), page.update()]),
                    ], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Impact", size=10, color=GOLD,
                                    weight=ft.FontWeight.BOLD),
                            ft.Container(height=3),
                            ft.Text(e["impact"], size=12, color=TEXT),
                        ]),
                        bgcolor=CARD2, border_radius=8, padding=12, border=bdr()),
                    ft.Container(height=6),
                    ft.Row([
                        ft.Icon(ft.icons.IMAGE_OUTLINED, color=SUBS, size=14),
                        ft.Container(width=4),
                        ft.Text(e["file"], size=11, color=SUBS, italic=True),
                    ]),
                ]),
                bgcolor=CARD, border_radius=12, padding=14,
                border=bdr(1, GOLD), margin=10))
        page.update()

    def on_gp(e):
        if not e.files: return
        f = e.files[0]
        gip["v"] = f.path if f.path else f.name
        gip["n"] = f.name
        gilbl.value = f"✅  {f.name}"; gilbl.color = GOLD
        page.update()

    def save_git(_):
        if not gcomm.value.strip():
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Enter a commit title."), bgcolor=RED)
            page.snack_bar.open = True; page.update(); return
        dest = ""; fname = "No screenshot"
        if gip["v"]:
            try:
                if os.path.exists(gip["v"]): dest = cp(gip["v"], GDIR)
                else: dest = gip["n"]
            except: dest = gip["n"]
            fname = gip["n"]
        db["github"].append({
            "commit": gcomm.value.strip(), "impact": gimp.value.strip(),
            "file": fname, "path": dest,
            "date": datetime.now().strftime("%d %b %Y")})
        save(db); gcomm.value = ""; gimp.value = ""
        gip["v"] = None; gip["n"] = None
        gilbl.value = "No screenshot selected"; gilbl.color = SUBS; rgx()

    gpick = ft.FilePicker()
    gpick.on_result = on_gp
    page.overlay.append(gpick)

    def build_github():
        return ft.Column([
            ft.Container(height=10),
            ft.Row([ft.Icon(ft.icons.CODE, color=GOLD, size=22),
                    ft.Container(width=8), h("🔗 GitHub Evidence")]),
            sub("Document your individual commits, pull requests and engineering impact."),
            ft.Container(height=8), div(),
            card(ft.Column([
                ft.Text("➕  Add Commit / PR Evidence", size=14,
                        weight=ft.FontWeight.W_600, color=GOLD),
                ft.Container(height=10), gcomm,
                ft.Container(height=8), gimp,
                ft.Container(height=10),
                ft.Row([
                    obtn("📸  Upload Screenshot",
                         lambda _: gpick.pick_files(
                             allowed_extensions=["png","jpg","jpeg","webp"]),
                         ft.icons.SCREENSHOT_MONITOR),
                    ft.Container(width=10),
                    gilbl,
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=12),
                gbtn("💾  Save Evidence", save_git, ft.icons.SAVE),
            ])),
            ft.Text("Saved Evidence", size=13, color=SUBS),
            ft.Container(height=6),
            gcol,
        ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)

    # ── NAVIGATION ─────────────────────────────────────
    content = ft.Container(expand=True, bgcolor=BG, padding=20)
    TABS    = [
        ("🏠", "About",   build_about),
        ("📐", "MATLAB",  build_matlab),
        ("🎬", "Blog",    build_blog),
        ("🔗", "GitHub",  build_github),
    ]
    nbtns = []

    def sw(idx):
        for i, b in enumerate(nbtns):
            b.bgcolor = GOLD if i == idx else CARD2
            b.color   = "#000000" if i == idx else SUBS
        content.content = TABS[idx][2]()
        if idx == 1: rmx()
        if idx == 2: rbx()
        if idx == 3: rgx()
        page.update()

    for i, (ico, lbl, _) in enumerate(TABS):
        b = ft.ElevatedButton(
            content=ft.Column([
                ft.Text(ico, size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(lbl, size=10, color="#000000" if i==0 else SUBS,
                        text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_500),
            ], spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=GOLD if i == 0 else CARD2,
            on_click=lambda e, i=i: sw(i),
            width=120,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
        nbtns.append(b)

    # Photo for sidebar
    photo_jpg = os.path.join(BASE, "assets", "my_photo.jpg")
    photo_png = os.path.join(BASE, "assets", "my_photo.png")
    if os.path.exists(photo_jpg):
        p_src = photo_jpg; has_p = True
    elif os.path.exists(photo_png):
        p_src = photo_png; has_p = True
    else:
        has_p = False

    sav = ft.Container(
        content=ft.Image(src=p_src, width=54, height=54,
                         fit=ft.ImageFit.COVER, border_radius=27)
                if has_p else
                ft.Text("CM", size=20, weight=ft.FontWeight.BOLD, color=GOLD,
                        text_align=ft.TextAlign.CENTER),
        width=54, height=54, border_radius=27,
        border=bdr(2, GOLD),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor=CARD2, alignment=ft.Alignment(0, 0))

    sidebar = ft.Container(
        content=ft.Column([
            ft.Container(height=20),
            sav,
            ft.Container(height=6),
            ft.Text("Catiana", size=12, color=TEXT,
                    weight=ft.FontWeight.W_600,
                    text_align=ft.TextAlign.CENTER),
            ft.Text("EEE · Yr 2", size=10, color=SUBS,
                    text_align=ft.TextAlign.CENTER),
            ft.Container(height=16),
            ft.Container(height=1, bgcolor=BDR),
            ft.Container(height=12),
            *nbtns,
            ft.Container(expand=True),
            ft.Container(height=1, bgcolor=BDR),
            ft.Container(height=8),
            ft.Text("CP1 · 2026", size=9, color=SUBS,
                    text_align=ft.TextAlign.CENTER),
            ft.Container(height=12),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
        width=148, bgcolor=CARD,
        border=ft.Border(right=ft.BorderSide(1, BDR)),
        padding=8)

    content.content = build_about()
    page.add(ft.Row([sidebar, content], expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START))
    rmx(); rbx(); rgx()

ft.app(main, assets_dir="assets")
