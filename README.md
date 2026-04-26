# Hi-C Analysis

### 1. Клонируем репозиторий

Для начала клонируем репозирорий и устанавливаем окружение с нужными либами

```bash
git clone https://github.com/dpanc2/BI_HiC_analysis.git
cd BI_HiC_analysis
```

### 2. Создание окружения

Не усложняем себе жтзнь его отсутствием

```bash
python3 -m venv .venv
source .venv/bin/activate
```

После активации ставим пакеты из requirements.txt (`numpy`, `pandas`, `cooler`, `cooltools`, `hic2cool`, `matplotlib`):
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Загружаем данные

Далее с помощью скрипта закружаем hic файлы и сразу конвертируем их в cool формат. Загруженные файлы будут храниться в папке `data/`

```bash
python3 /data/ddpanchenko/main_dom/BI_HiC_analysis/scripts/download_data.py
```
