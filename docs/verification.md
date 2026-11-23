# گزارش اجرای محلی HD-01

تاریخ بررسی: ۲۰۲۶-۱۱-۲۳. پیاده‌سازی فاز ۰۱ و بررسی‌های محلی انجام شده‌اند. وضعیت پذیرش کامل **BLOCKED** است، زیرا اصل مجموعهٔ اسناد کارآموزی کامل تحویل نشده است. نتیجهٔ اجرای GitHub Actions و SHA آخرین تغییرات در گزارش PR ثبت می‌شوند.

## نتایج واقعی

محیط: macOS ARM64، Python 3.12.16 و uv 0.13.9. ابزار uv برای این بررسی در محیط جداگانهٔ `/tmp/hamdid-foundation-tools` نصب و از مسیر `/tmp/hamdid-foundation-tools/bin/uv` اجرا شد؛ نصب سراسری یا تغییر PATH انجام نشده است.

| فرمان یا بررسی | نتیجه |
| --- | --- |
| `uv sync --locked --group dev` | موفق؛ بستهٔ پروژه واقعاً نصب شد |
| `uv run --locked ruff format --check .` | موفق |
| `uv run --locked ruff check .` | موفق |
| `uv run --locked pytest -q` | موفق؛ **۳ تست** واقعی subprocess |
| `uv run --locked python -m hamdid --version` | خروج صفر و خروجی دقیق `0.1.0.dev0` |
| `git diff --check` و `git diff --cached --check` | موفق |
| `git diff --cached --name-only` | بازبینی شد؛ فقط فایل‌های فاز ۰۱ |
| `git check-ignore` | محیط مجازی، کش‌ها، اسرار، داده، مدل، گزارش محلی و پایگاه زمان اجرا ignored؛ نمونه‌های `tests/fixtures/` مجاز |
| نصب و اجرای دوباره در clone پاک | موفق؛ محیط مجازی و کش uv تازه، همان ۳ تست، قفل بدون تغییر |
| ساخت sdist و wheel با `uv build` و نصب wheel در محیط جداگانه | موفق؛ import و فرمان نسخه خارج از ریشه و با `python -I` موفق |
| بررسی workflow با `actionlint 1.7.12` | موفق؛ بدون اتصال اختیاری ShellCheck/Pyflakes |
| منطق whitespace خود workflow در مخزن آزمایشی | ۶ حالت PR، push و push اولیه؛ حالت‌های پاک موفق و خطاهای commit‌شده همگی رد شدند |

در بررسی اولیه، از فایل‌های staged یک snapshot در مخزن موقت مستقل ثبت و clone شد. برای تحویل PR نیز نصب و کنترل‌ها باید از کامیت نهایی واقعی شاخهٔ فاز در worktree تازه اجرا شوند؛ SHA و نتیجهٔ این مرحله در بدنهٔ PR ثبت می‌شود. مخزن اصلی فقط یک کامیت bootstrap روی `main` و `dev` دارد و تغییرات فاز با PR به `dev` پیشنهاد می‌شوند.

## محدودیت‌های تحویل

- کاربر در ۲۰۲۶-۱۱-۲۳ صریحاً ساخت مخزن **عمومی** و bootstrap شاخه‌های `main` و `dev` را در حساب مرورگر مجاز کرد. [مخزن عمومی](https://github.com/payamshoartajahmadi-lab/hamdid-recsys) ساخته شد و هر دو شاخه در شروع روی کامیت `9ba613b2b0a09cfe453ff9c757513a438208a730` بودند. این دستور جدید جایگزین پیش‌شرط ساخت مخزن خصوصی توسط سرپرست است؛ سند اصلی فاز برای حفظ مرجع دست‌نخورده باقی مانده است.
- فقط سند فاز ۰۱ دریافت شده است. نقشهٔ راه، راهنمای کارآموز و باقی مجموعهٔ هفت‌سندی در دسترس نیستند؛ جزئیات در [نمایهٔ مستندات](README.md) ثبت شده است.
- لینک PR، SHA آخرین کامیت و نتیجهٔ `quality` باید در [PR فاز](https://github.com/payamshoartajahmadi-lab/hamdid-recsys/pulls) گزارش شوند. اعتبارسنجی محلی workflow جایگزین نتیجهٔ [GitHub Actions](https://github.com/payamshoartajahmadi-lab/hamdid-recsys/actions) نیست. حساب بازبین مستقل مشخص نشده است و نویسندهٔ PR نمی‌تواند از خودش درخواست review کند.
- PR ادغام نمی‌شود و SHA ادغام وجود ندارد. پذیرش کامل به دریافت اسناد رسمی، موفقیت `quality` روی آخرین تغییرات و بازبینی سرپرست وابسته است. `main` و `dev` تا تصمیم سرپرست روی bootstrap باقی می‌مانند.

## منابع نسخه‌های CI

SHAها از releaseهای رسمی تأیید شدند: [actions/checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1)، [astral-sh/setup-uv v10.4.0](https://github.com/astral-sh/setup-uv/releases/tag/v10.4.0) و [uv 0.13.9](https://github.com/astral-sh/uv/releases/tag/0.13.9). مقدار Python 3.12.16 در [metadata رسمی uv](https://raw.githubusercontent.com/astral-sh/uv/0.13.9/crates/uv-python-managed/download-metadata.json) نیز موجود است.
