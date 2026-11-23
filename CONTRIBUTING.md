# مشارکت در هم‌دید

مالک مخزن کارآموز را با سطح **Write** به همکاران [hamdid-recsys](https://github.com/payamshoartajahmadi-lab/hamdid-recsys) اضافه می‌کند. کارآموز دعوت را با حساب خودش می‌پذیرد و Git، هویت نویسنده، Python 3.12 و `uv 0.13.9` را آماده می‌کند.

## شاخهٔ شخصی و PR

هر کار از آخرین `dev` شروع می‌شود. برای قابلیت از `feature/<short-name>` و برای اصلاح از `fix/<short-name>` استفاده کنید؛ نام شاخهٔ زیر یک نمونه است:

```bash
git clone https://github.com/payamshoartajahmadi-lab/hamdid-recsys.git
cd hamdid-recsys
git fetch origin --prune
git switch --no-track -c feature/my-task origin/dev
```

در clone موجود، قبل از ساخت شاخه وضعیت کار را با `git status` بررسی کنید و تغییرات قبلی را حفظ کنید. کار مستقیم روی `main` و force-push مجاز نیست؛ تغییرات `dev` با PR وارد می‌شوند.

کامیت‌ها را کوتاه و روشن بنویسید؛ برای نمونه `feat(ranking): add candidate scoring` یا `fix(cli): clarify help output`. سپس شاخهٔ خودتان را push کنید:

```bash
git push -u origin feature/my-task
```

PR را با **base = `dev`** و **compare = شاخهٔ خودتان** بسازید. [قالب PR](.github/pull_request_template.md) را با شرح تغییرات و نتیجهٔ واقعی بررسی‌ها پر کنید. پس از تکمیل کار و موفقیت job `quality` روی آخرین تغییرات، کارآموز می‌تواند PR خودش را در `dev` ادغام کند؛ بازبینی یا تأیید اجباری سرپرست لازم نیست. بررسی pending، اجرا‌نشده، ناموفق یا لغوشده مجوز ادغام نیست.

## بررسی پیش از ادغام

```bash
uv sync --locked --group dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked pytest -q
uv run --locked python -m hamdid --version
git diff --check
git fetch origin dev
git diff --check origin/dev...HEAD
```

برای تغییر عمدی وابستگی‌ها، `uv lock` را اجرا و تغییر قفل را commit کنید؛ بررسی‌های عادی با `--locked` قفل را به‌روزرسانی نمی‌کنند. CI همین کنترل‌ها را در job ثابت `quality` اجرا می‌کند و فرمت یا lint فایل‌ها را اصلاح نمی‌کند.

پیش از commit فهرست فایل‌ها را با `git diff --cached --name-only` کنترل کنید. دادهٔ واقعی، مدل، اسرار، فایل‌های محیطی و خروجی اجرا نباید وارد مخزن شوند؛ `.gitignore` این مسیرها را مشخص می‌کند. نمونهٔ کوچک ساختگی زیر `tests/fixtures/` مجاز است.

اگر تغییر ادغام‌شده مشکل داشت، روی شاخهٔ جدید از `dev` با `git revert` آن را برگردانید و PR اصلاحی بسازید؛ تاریخ را بازنویسی نکنید. اسناد اولیهٔ پروژه سابقه‌اند و دریافت بقیهٔ آن‌ها شرط مشارکت نیست.
