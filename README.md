# هم‌دید | Hamdid

[هم‌دید](https://github.com/payamshoartajahmadi-lab/hamdid-recsys) یک پروژهٔ عمومی برای توسعهٔ سامانهٔ توصیه‌گر است. نسخهٔ فعلی پایهٔ پایتون، تست و CI را فراهم می‌کند. نام توزیع `hamdid-recsys`، نام import برابر `hamdid` و نسخه `0.1.0.dev0` است. داده، مدل، API و رابط کاربری هنوز پیاده‌سازی نشده‌اند؛ ورودی خط فرمان فعلی نسخه و راهنما را نمایش می‌دهد.

## نصب و بررسی

Git، Python 3.12 و `uv 0.13.9` لازم است. تغییرات پایه فعلاً روی شاخهٔ `chore/01-repository-foundation` قرار دارند؛ پس از ادغام PR می‌توان به‌جای آن `dev` را checkout کرد.

```bash
git clone https://github.com/payamshoartajahmadi-lab/hamdid-recsys.git
cd hamdid-recsys
git switch chore/01-repository-foundation
uv sync --locked --group dev
uv run --locked python -m hamdid --version
uv run --locked python -m hamdid --help
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked pytest -q
git diff --check
```

دستور نسخه دقیقاً `0.1.0.dev0` را چاپ می‌کند. تست‌ها نسخه، راهنما و خروج غیرصفر آرگومان نامعتبر را با subprocess واقعی در دایرکتوری موقت خارج از ریشه بررسی می‌کنند. وابستگی runtime وجود ندارد؛ ابزارهای توسعه در گروه `dev` و نسخه‌های حل‌شده در `uv.lock` ثبت شده‌اند.

## کار کارآموز

مالک مخزن باید کارآموز را با دسترسی **Write** به همکاران مخزن اضافه کند. کارآموز از `dev` یک شاخهٔ شخصی مانند `feature/add-ranking` یا `fix/cli-help` می‌سازد، روی آن کار می‌کند و PR را با مقصد `dev` باز می‌کند. پس از تکمیل کار و موفقیت بررسی `quality` روی آخرین تغییرات، می‌تواند PR خودش را در `dev` ادغام کند؛ تأیید سرپرست اجباری نیست.

دستورهای عملی در [CONTRIBUTING.md](CONTRIBUTING.md) و قواعد کار روی پروژه در [AGENTS.md](AGENTS.md) آمده است. اسناد اولیه در [docs](docs/README.md) صرفاً سابقهٔ پروژه‌اند؛ جریان کاری جاری همین راهنمای ساده است.
