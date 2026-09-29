from flask import Flask, render_template_string

app = Flask(__name__)

whatsapp_number = "9647762729235" 

html_template = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>شركة كودكس | Codex Digital</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #f8fafc; color: #0f172a; display: flex; flex-direction: column; min-height: 100vh; line-height: 1.6; }
        header { background: #0f172a; color: #fff; padding: 18px 20px; text-align: center; border-bottom: 3px solid #2563eb; }
        header h2 { font-size: 22px; letter-spacing: 1px; color: #38bdf8; }
        .hero { text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #1e293b, #0f172a); color: white; }
        .hero h1 { font-size: 26px; margin-bottom: 12px; color: #f8fafc; }
        .hero p { font-size: 15px; color: #94a3b8; max-width: 600px; margin: 0 auto; }
        .container { max-width: 1050px; margin: 30px auto; padding: 0 15px; flex: 1; }
        .section-title { text-align: center; margin: 30px 0 20px; color: #0f172a; font-size: 22px; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; transition: transform 0.2s; }
        .card-body { padding: 20px; display: flex; flex-direction: column; height: 100%; }
        .card-icon { font-size: 32px; margin-bottom: 10px; }
        .card-title { font-size: 19px; margin-bottom: 10px; color: #1e293b; }
        .card-desc { font-size: 14px; color: #64748b; margin-bottom: 20px; flex-grow: 1; }
        .btn { display: inline-block; width: 100%; padding: 12px; background: #25D366; color: white; text-align: center; border-radius: 8px; text-decoration: none; font-weight: bold; }
        footer { background: #0f172a; color: #94a3b8; text-align: center; padding: 35px 20px; margin-top: 50px; font-size: 14px; }
        footer h3 { color: #f8fafc; font-size: 18px; margin-bottom: 10px; }
        footer p { max-width: 650px; margin: 0 auto 15px; color: #94a3b8; line-height: 1.7; }
        .copyright { font-size: 13px; color: #64748b; border-top: 1px solid #334155; padding-top: 15px; margin-top: 20px; }
    </style>
</head>
<body>

    <header>
        <h2>⚡ شركة كودكس | CODEX DIGITAL</h2>
    </header>

    <section class="hero">
        <h1>حلول برمجية متكاملة وتطوير ألعاب ومواقع</h1>
        <p>نحن في شركة كودكس (Codex Digital) نقدم أفضل الخدمات التقنية وتطوير التطبيقات والمواقع وألعاب الموبايل بأعلى جودة واحترافية.</p>
    </section>

    <div class="container">
        <h2 class="section-title">خدمات شركة كودكس</h2>
        
        <div class="services-grid">
            <div class="card">
                <div class="card-body">
                    <div class="card-icon">🌐</div>
                    <h3 class="card-title">تصميم وتطوير المواقع</h3>
                    <p class="card-desc">بناء مواقع إلكترونية ومتاجر احترافية وسريعة جداً متوافقة مع كافة الشاشات والأجهزة.</p>
                    <a href="https://wa.me/{{ phone }}?text=مرحباً%20فريق%20كودكس،%20أرغب%20في%20طلب%20تطوير%20موقع" target="_blank" class="btn">تواصل مع فريق كودكس 💬</a>
                </div>
            </div>

            <div class="card">
                <div class="card-body">
                    <div class="card-icon">📱</div>
                    <h3 class="card-title">تطوير تطبيقات الموبايل</h3>
                    <p class="card-desc">برمجة وتصميم تطبيقات أندرويد و iOS مخصصة للشركات والمشاريع التجارية.</p>
                    <a href="https://wa.me/{{ phone }}?text=مرحباً%20فريق%20كودكس،%20أرغب%20في%20استشارة%20لتطبيق%20موبايل" target="_blank" class="btn">اطلب استشارة برمجية 💬</a>
                </div>
            </div>

            <div class="card">
                <div class="card-body">
                    <div class="card-icon">🎮</div>
                    <h3 class="card-title">تطوير وبرمجة الألعاب</h3>
                    <p class="card-desc">استوديو متخصص في بناء وتصميم ألعاب الموبايل والكمبيوتر بأحدث المحركات التقنية.</p>
                    <a href="https://wa.me/{{ phone }}?text=مرحباً%20فريق%20كودكس،%20أرغب%20في%20مناقشة%20مشروع%20لعبة" target="_blank" class="btn">ناقش مشروع لعبتك 💬</a>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <h3>شركة كودكس - Codex Digital</h3>
        <p>فريق برمجي متكامل لتطوير البرمجيات والحلول الرقمية لدعم رواد الأعمال وأصحاب المشاريع لبناء حضور رقمي قوي.</p>
        <div class="copyright">جميع الحقوق محفوظة © 2026 - شركة كودكس / Codex Digital</div>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, phone=whatsapp_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
