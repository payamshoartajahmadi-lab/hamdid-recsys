# مشارکت در هم‌دید

## پیش از شروع فاز

مقصد پروژه مخزن **عمومی** `hamdid-recsys` است. کاربر در ۲۰۲۶-۱۱-۲۳ صریحاً ایجاد آن با حساب واردشدهٔ مرورگر، کامیت اولیهٔ README، شاخهٔ پیش‌فرض `main` و شاخهٔ `dev` از همان کامیت را مجاز کرد. این bootstrap یک‌باره استثنای پیش‌نیاز مخزن خصوصیِ آماده در سند اصلی است؛ نسخهٔ اصلی سند تغییر نمی‌کند. ایجاد PR فاز به `dev` مجاز است و ادغام آن در این تحویل انجام نمی‌شود.

برای ادامهٔ مشارکت، دسترسی همکاری و آدرس remote، Python 3.12، `uv 0.13.9` و هویت نویسندهٔ Git را بررسی کنید. در نبود پیش‌نیاز یا سند لازم، گزارش `BLOCKED` بدهید؛ ایجاد دوبارهٔ مخزن یا شاخه‌های پایه مشمول استثنای bootstrap نیست.

در clone تازه و پیش از شروع اولین فاز، تأیید کنید هر دو SHA زیر همان کامیت bootstrap هستند. مالک مخزن `payamshoartajahmadi-lab` است.

```bash
git clone https://github.com/payamshoartajahmadi-lab/hamdid-recsys.git
cd hamdid-recsys
git remote -v
git fetch origin --prune
git branch -r
git status --short
git rev-parse origin/main origin/dev
git switch --no-track -c chore/01-repository-foundation origin/dev
```

در صورت مغایرت remote، نبود شاخه یا کار قبلی چیزی را حذف یا reset نکنید. اگر شاخهٔ فاز از قبل وجود دارد، برای ادامه با سرپرست هماهنگ کنید. پس از bootstrap، push مستقیم به `main` یا `dev` ممنوع است؛ force-push در تمام مراحل ممنوع است.

## نام‌گذاری و PR

شاخهٔ این فاز `chore/01-repository-foundation` و عنوان PR آن `chore(repo): establish project foundation and CI` است. کامیت‌های کوچک و قابل بازبینی با عنوان انگلیسی و الگوی `type(scope): description` بنویسید؛ برای نمونه:

```text
build(python): configure locked development environment
test(cli): verify package entry point
```

فقط شاخهٔ فاز را push کنید و PR را با **base = `dev`** و **compare = `chore/01-repository-foundation`** بسازید:

```bash
git push -u origin chore/01-repository-foundation
```

[قالب PR](.github/pull_request_template.md) را با نتیجهٔ واقعی پر کنید و سرپرست را برای بازبینی درخواست کنید. گزارش باید آخرین SHA، لینک CI، فرمان‌ها و تعداد تست، نصب پاک، ریسک و روش بازگشت را داشته باشد. در نبود PR یا CI مقدار ناموجود را صریح بنویسید؛ آن را موفق گزارش نکنید.

## بازتولید کنترل‌های CI

قفل با resolver و دستور `uv lock` ساخته یا عمداً به‌روزرسانی می‌شود. بررسی‌ها قفل را تغییر نمی‌دهند:

```bash
uv sync --locked --group dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked pytest -q
uv run --locked python -m hamdid --version
git diff --check
```

برای PR فاز، پس از fetch کردن مقصد، whitespace تغییرات واقعی را هم بررسی کنید؛ diff خالی یک checkout پاک کافی نیست:

```bash
git fetch origin dev
git diff --check origin/dev...HEAD
git diff --cached --check
git diff --cached --name-only
git check-ignore .venv/probe .env .env.local kaggle.json data/raw/probe data/processed/probe artifacts/probe reports/local/probe runtime.sqlite3
```

مسیرهای ممنوع باید ignored باشند و یک نمونهٔ کوچک ساختگی نظیر `tests/fixtures/example.json` نباید ignored باشد. وجود داده یا اسرار واقعی را پیش از stage کردن بررسی کنید. در CI فرمت و lint فقط بررسی می‌کنند و فایل را اصلاح نمی‌کنند. workflow روی PRهای مقصد `dev` یا `main` و push به این دو شاخه اجرا می‌شود و job مورد انتظار آن `quality` است.

پس از آخرین کامیت، در مسیر تازه‌ای خارج از checkout کاری یک worktree بسازید و کنترل‌های بالا را دوباره اجرا کنید. `CLEAN_PATH` در نمونه مسیر جدید و دلخواه شماست:

```bash
git worktree add --detach CLEAN_PATH HEAD
cd CLEAN_PATH
uv sync --locked --group dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked pytest -q
uv run --locked python -m hamdid --version
git diff --check
```

## بازبینی، ادغام و بازگشت

کارآموز PR را merge نمی‌کند. سرپرست قابلیت نصب تازه، تست واقعی آرگومان نامعتبر، محدودهٔ فاز و نبود داده یا اسرار را بازبینی می‌کند. `quality` باید روی آخرین تغییرات PR اجرا شده و موفق باشد؛ نتیجهٔ pending، لغوشده یا اجرا‌نشده پذیرفته نیست. پس از تأیید، سرپرست PR فاز را با **Squash and merge** به `dev` می‌برد و لینک PR و SHA ادغام را ثبت می‌کند. `main` در فاز ۰۱ روی bootstrap می‌ماند.

ادغام فازها و انتشار دو عملیات جدا هستند. شاخهٔ هر فاز به `dev` squash می‌شود؛ در یک انتشار مجاز آینده، سرپرست PR جداگانهٔ `dev` به `main` را با merge commit ادغام می‌کند تا تاریخ شاخه‌های بلندمدت حفظ شود. شاخهٔ `dev` حذف نمی‌شود و فاز ۰۲ پیش از تأیید فاز ۰۱ آغاز نمی‌شود.

برای rollback، یک شاخهٔ اصلاحی از `dev` بسازید و کامیت squash ثبت‌شدهٔ همان PR را با `git revert MERGE_SHA` برگردانید. نتیجه از PR جدید، همان تست‌ها و بازبینی سرپرست عبور می‌کند؛ تاریخ را بازنویسی یا force-push نکنید. اگر بازگشت یک انتشار آینده لازم باشد، سرپرست PR بازگشت متناسب با merge commit انتشار را بررسی می‌کند.
