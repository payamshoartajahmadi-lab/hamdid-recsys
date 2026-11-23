# بررسی‌های فنی پایهٔ پروژه

محیط بررسی محلی: Python 3.12.16 و uv 0.13.9.

```bash
uv sync --locked --group dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked pytest -q
uv run --locked python -m hamdid --version
git diff --check
git diff --check origin/dev...HEAD
```

بسته در محیط پاک نصب شد؛ هر سه تست واقعی subprocess برای نسخه، راهنما و آرگومان نامعتبر موفق بودند. خروجی نسخه دقیقاً `0.1.0.dev0` است. فرمت، lint و whitespace موفق بودند و قفل تغییر نکرد. ساخت sdist و wheel و نصب wheel خارج از ریشه نیز بررسی شد.

workflow با actionlint و منطق whitespace آن در شش حالت PR، push و push اولیه بررسی شد. اولین اجرای دوردست [quality](https://github.com/payamshoartajahmadi-lab/hamdid-recsys/actions/runs/45173196748) روی کامیت `cffaf6d4a7f6b20804231a22e7ad1e2bb56dccd3` موفق بود. وضعیت آخرین تغییرات و لینک اجرای مربوط به آن در [PR شمارهٔ ۱](https://github.com/payamshoartajahmadi-lab/hamdid-recsys/pull/1) دیده می‌شود.

جریان همکاری مطابق [CONTRIBUTING.md](../CONTRIBUTING.md) است: هر کارآموز روی شاخهٔ خودش کار می‌کند و پس از تکمیل کار و موفقیت CI می‌تواند PR خودش را به `dev` ادغام کند.
