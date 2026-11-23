# هم‌دید | فاز ۰۱: پایهٔ پایتون و کنترل کیفیت

**مسئول اجرا:** کارآموز • **بازبین و مسئول ادغام:** سرپرست • **شناسه:** HD-01 • **نسخه:** کارآموزی 1.1

**هدف:** از مخزن موجود یک بستهٔ پایتون قابل نصب بساز. یک توسعه‌دهندهٔ دیگر باید بتواند آن را در یک محیط تازه نصب کند، فرمان نسخه را اجرا کند و همان بررسی‌های GitHub Actions را بگذراند. فاز اول عمداً کاری با داده یا مدل ندارد.

## ۱. نقطهٔ شروع و مرز مسئولیت

سرپرست مخزن خصوصی `hamdid-recsys`، کامیت اولیهٔ README، شاخهٔ پیش‌فرض `main`، شاخهٔ `dev` از همان کامیت، و دعوت همکاری را آماده می‌کند. **کارآموز مخزن یا این دو شاخه را نمی‌سازد**، تنظیمات دسترسی یا حفاظت را تغییر نمی‌دهد و با حساب سرپرست وارد نمی‌شود. در نبود هر پیش‌نیاز گزارش بده. مقصد این فاز `dev` است؛ `main` تغییر نمی‌کند. دانلود داده، مدل، API، UI و انتشار خارج از محدوده‌اند.

## ۲. شروع کار روی شاخهٔ فاز

با حساب خودت دعوت را بپذیر. Git و `uv`، دسترسی به Python 3.12 و هویت نویسندهٔ Git را بررسی کن. دستورات زیر برای **clone تازه** هستند. به‌جای `OWNER` نام مالک را بگذار. در صورت مغایرت remote، نبود شاخه یا وجود کار قبلی، چیزی را حذف، بازنشانی یا force-push نکن. اگر شاخهٔ این فاز از قبل وجود دارد، ادامهٔ همان کار را با سرپرست هماهنگ کن.

```bash
git clone https://github.com/OWNER/hamdid-recsys.git
cd hamdid-recsys
git remote -v
git fetch origin --prune
git branch -r
git status --short
git rev-parse origin/main origin/dev
# First handoff: confirm both branch tips match the owner's bootstrap commit.
git switch --no-track -c chore/01-repository-foundation origin/dev
```

## ۳. خروجی‌های این PR


| مسیر | قرارداد قابل آزمون |
|---|---|
| `README.md` | تعریف محصول و وضعیت فعلی، پیش‌نیازها، دستور نصب و تست از clone تازه، نقشهٔ فازها و جریان شاخه‌ها. برای CLI یا UI آینده ادعای آماده‌بودن نکن. |
| `AGENTS.md` | فقط فاز مأموریت، ممنوعیت push مستقیم و force-push، تست‌های اجباری، سیاست داده و اسرار، گزارش کارآموز در PR و ثبت نتیجهٔ ادغام توسط سرپرست، امکان توقف به دلیل blocker. |
| `CONTRIBUTING.md` | نام‌گذاری شاخه/کامیت/PR، تفاوت squash شاخهٔ فاز و merge انتشار، روش بازتولید CI، بازبینی سرپرست پیش از ادغام و rollback با revert PR. |
| `.gitignore` | `.venv/`، کش‌ها، `.env` و نسخه‌های محلی آن، `kaggle.json`، `data/raw/`، `data/processed/`، `artifacts/`، `reports/local/` و پایگاه دادهٔ زمان اجرا. نمونهٔ ساختگی کوچک زیر `tests/fixtures/` مجاز بماند. |
| `.python-version`, `pyproject.toml`, `uv.lock` | Python 3.12؛ نام توزیع `hamdid-recsys`، نام import برابر `hamdid`، نسخهٔ ابتدایی `0.1.0.dev0`. وابستگی‌های توسعه از runtime جدا؛ با build backend مناسب، بستهٔ `src/hamdid` واقعاً نصب شود. |
| `src/hamdid/__init__.py`, `src/hamdid/__main__.py` | `python -m hamdid --version` دقیقاً نسخهٔ metadata بسته را چاپ کند؛ `--help` با خروج صفر؛ آرگومان نامعتبر با خروج غیرصفر. منبع نسخه دوتا نباشد. |
| `tests/test_cli.py` | subprocess واقعی در دایرکتوری موقت خارج از ریشه اجرا شود؛ سه رفتار فوق را بررسی کند. تستی از جنس `assert True` قابل قبول نیست. |
| `.github/workflows/ci.yml` | روی `pull_request` با مقصد `dev` یا `main` و `push` به این دو اجرا شود. job با نام ثابت `quality`، دسترسی `contents: read`، زمان‌سنج؛ checkout، راه‌اندازی نسخهٔ مشخص uv/Python، نصب قفل‌شده و کنترل‌های بخش ۵. هیچ secret یا دیتاست لازم نیست. از action رسمی و release معتبر با SHA کامل و کامنت نسخه استفاده کن؛ SHA حدسی ننویس. |
| `.github/pull_request_template.md` | مسئله، تغییرات، خارج از محدوده، تست واقعی، اثر بر داده، ریسک، روش بازگشت، معیار پذیرش، base branch. |
| `docs/` | شرح مأموریت و هفت سند همین بستهٔ کارآموزی را در مسیرهای خودشان ثبت کن. وجود فازهای بعدی به معنی اجرای آن‌ها نیست. ZIP یا نسخهٔ قدیمی مخصوص Codex را وارد مخزن نکن. |

`uv.lock` را با resolver تولید و commit کن. دادهٔ واقعی، مدل، پوشهٔ مجازی، رمز، فایل ZIP تحویل یا تصویر ساختگیِ داشبورد را به مخزن اضافه نکن. SQL، API، Docker، notebook، React و دانلود دیتاست در این PR جایی ندارند. مجوز متن‌باز از جانب مالک انتخاب نکن.

## ۵. کنترل کیفیت و پذیرش محلی

از محیطی پاک که قبلاً بسته را نصب نکرده اجرا کن. CI باید همان کنترل‌ها را اجرا کند. `uv lock` برای ساخت یا به‌روزرسانی قفل است؛ مرحلهٔ بررسی نباید قفل را به‌روزرسانی کند.

```bash
uv sync --locked --group dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked pytest -q
uv run --locked python -m hamdid --version
git diff --check
```

همچنین با `git check-ignore` مسیرهای ممنوع و با `git diff --cached --name-only` فهرست فایل‌های staged را بررسی کن. یک بار با checkout تازه یا worktree موقت از commit نهایی، نصب و تست را بازاجرا کن. در workflow برای کنترل whitespace دامنهٔ diff واقعی PR را بررسی کن؛ `git diff --check` روی checkout تمیز به تنهایی آن را نمی‌آزماید. فرمت و lint نباید در CI فایل را اصلاح کنند.

## ۶. تحویل کارآموز: PR آمادهٔ بازبینی

کامیت‌ها را در واحدهای قابل بررسی و با عنوان انگلیسی بنویس. مثال: `build(python): configure locked development environment` و `test(cli): verify package entry point`. فقط شاخهٔ فاز را push کن:

```bash
git push -u origin chore/01-repository-foundation
```

در GitHub، **base = `dev`** و **compare = `chore/01-repository-foundation`** را انتخاب کن. عنوان: `chore(repo): establish project foundation and CI`. در بدنهٔ PR هدف، فایل‌های مهم، خارج از محدوده، فرمان‌های اجرا، نتیجهٔ واقعی، لینک CI، ریسک و روش بازگشت را بنویس. سرپرست را برای بازبینی دعوت کن. `quality` باید روی آخرین تغییرات PR اجرا و موفق شود. کنترل اجرا‌نشده، ردشده یا لغوشده را موفق تلقی نکن. اگر `quality` شکست خورد، روی همین شاخه اصلاح کن و دوباره نتیجه بگیر. PR را خودت merge نکن و قبل از تأیید فاز ۰۲ را شروع نکن.

**گزارش تو:** `READY_FOR_REVIEW` یا `BLOCKED`، لینک PR، SHA آخرین کامیت، لینک اجرای GitHub Actions، فرمان‌ها و تعداد تست واقعی، نتیجهٔ نصب در محیط تمیز و محدودیت حل‌نشده. قبل از ادغام، SHA ادغام وجود ندارد.

## ۷. پذیرش سرپرست

سرپرست تغییرات را بازبینی می‌کند: آیا از یک clone تازه قابل اجراست؟ آیا تست گزینهٔ نامعتبر واقعاً شکست دستور را می‌سنجد؟ آیا هیچ فایل واقعی، کلید یا قابلیت فاز بعدی اضافه نشده؟ بعد از اطمینان از موفقیت `quality` روی آخرین کامیت و تأیید تغییرات، فقط همین PR را با **Squash and merge** در `dev` ادغام می‌کند. سپس لینک PR و SHA ادغام را ثبت می‌کند و مطمئن می‌شود `main` همان کامیت اولیه مانده است. امکان الزام PR و check به پلن مخزن بستگی دارد؛ نبود امکان اعمال قانون سیستمی مجوز کنار گذاشتن بازبینی یا CI نیست. ادغام فازها به `main` و حذف `dev` ممنوع است.

**مرجع قرارداد:** [نقشهٔ راه](00-roadmap.md) و [راهنمای کارآموز](../INTERN-BRIEF.md). **مراجع ابزار:** [CI و کنترل‌های PR](https://cli.github.com/manual/gh_pr_checks)، [قفل وابستگی‌های uv](https://docs.astral.sh/uv/concepts/projects/sync/)، [حفاظت شاخه در GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
