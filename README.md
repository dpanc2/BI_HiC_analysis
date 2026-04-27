# Hi-C Analysis

## Структура репозитория

```text
BI_HiC_analysis/
├── notebooks/          # Jupyter notebooks
├── scripts/            # Скрипт для загрузки и подготовки данных
├── data/               # Данные, создаётся после запуска download_data.py
├── requirements.txt    # Python-зависимости
└── README.md
```

### 1. Подготовка
Для начала клонируем репозирорий и устанавливаем окружение с нужными пакетами.

```bash
git clone https://github.com/dpanc2/BI_HiC_analysis.git
cd BI_HiC_analysis
```

### 2. Создание окружения

Не усложняем себе жизнь его отсутствием :)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

После активации ставим пакеты из requirements.txt (`numpy`, `pandas`, `cooler`, `cooltools`, `hic2cool`, `matplotlib`):
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Основные библиотеки, которые используются в проекте:

- `cooler` — работа с `.cool` и `.mcool` файлами
- `cooltools` — анализ Hi-C матриц
- `hic2cool` — конвертация `.hic` в `.cool/.mcool`
- `matplotlib`, `seaborn` — визуализация
- `numpy`, `pandas` — работа с таблицами и массивами
- 

### 3. Загружаем данные

Далее с помощью скрипта закружаем hic файлы и сразу конвертируем их в cool формат. Загруженные файлы будут храниться в папке `data/`

```bash
python3 /data/ddpanchenko/main_dom/BI_HiC_analysis/scripts/download_data.py
```
После выполнения скрипта ожидаемая структура данных примерно такая:

```text
data/
├── Control_inter_30.hic
├── Treated_inter_30.hic
├── Prime_inter_30.hic
├── Control_inter_30.mcool
├── Treated_inter_30.mcool
└── Prime_inter_30.mcool
```

# Визуализация
Если вы собираетесь много работать с `.hic` файлами и смотреть на них глазами, лучше всего установить приложение **Juicebox** локально:

https://github.com/aidenlab/Juicebox/wiki/Download

В нём есть много удобных функций для визуальной проверки Hi-C карт.  
Для учебного проекта хватит веб-версии:

https://www.aidenlab.org/juicebox/

# Блокноты 
Папка `notebooks/` с блокнотами для визуализации hic карт, Contacts vs distance, Compartments & Saddleplots и Insulation & boundaries анализы

# Полезные команды для командной строки и быстрой проверки файлов

Посмотреть информацию о `.mcool` файле:

```bash
cooler info data/Control_inter_30.mcool::/resolutions/1000000
```

Посмотреть доступные разрешения:

```bash
cooler ls data/Control_inter_30.mcool
```

Проверить таблицу bins:

```bash
cooler dump --table bins data/Control_inter_30.mcool::/resolutions/1000000 | head
```

Проверить пиксели матрицы:

```bash
cooler dump --table pixels data/Control_inter_30.mcool::/resolutions/1000000 | head
```
