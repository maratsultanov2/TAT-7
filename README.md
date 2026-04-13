# 🧠 TAT-7

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

*Tempus, Angulus, Tactus — una resonantia.*  
*Время, Угол, Касание — единый резонанс.*

**TAT-7** — нейросетевая архитектура с резонансной памятью для непрерывного обучения (Continual Learning).  
Работает на CPU, в 20 раз меньше параметров, чем типичные CNN.

---

### 🏆 Результаты

| Бенчмарк | Результат | Рейтинг | Дата |
|:---|:---|:---|:---|
| REBUS | 19.40% | Топ-5 мира | 18.03.2026 |
| MNIST | 97.82% | Топ-10 мира | 19.03.2026 |
| CIFAR-10 (CL) | 91.7% | 10 задач | 2025 |
| TinyImageNet (CL) | 39.9% | 20 задач | 10.03.2026 |

---

### ⚡ Быстрый старт

git clone https://github.com/maratsultanov2/TAT-7.git
cd TAT-7
python train.py --config ideal_config.json

---

### 📖 Пример использования

from tat import TAT7

model = TAT7(heads=7, phase_angle=1.987)
output = model.forward(input_tensor)

---

### 📅 История проекта

**2025**
- **Янв–Апр:** исследование CNN, ResNet, проблем градиентов
- **Май:** формирование концепции Multi-Head, создание **Triplenet**
- **Июн–Авг:** проверка Triplenet, анализ границ масштабирования
- **Сен–Дек:** проектирование архитектуры **TAT**

**2026**
- **17.03:** рождение **TAT-7**
- **18.03:** **19.40% на REBUS** — Топ-5 мира
- **19.03:** открытие **7 голов** как оптимального числа
- **19.03:** **97.82% на MNIST** — Топ-10 мира

---

### 🔗 Экосистема TAT

| Проект | Описание |
|:---|:---|
| [TreeAngleTap](https://github.com/maratsultanov2/TreeAngleTap) | Экспериментальная площадка |
| [TAT Agent Helper](https://github.com/maratsultanov2/TAT_agent_helper) | Автономный агент для лидогенерации |
| [Triplenet](https://github.com/maratsultanov2/Triplenet) | Предшественник |

---

### 👤 Автор

**Марат Султанов**  
[GitHub](https://github.com/maratsultanov2) | [Telegram](https://t.me/Marat_Sultanow)

---

### 📄 Лицензия

MIT License. Ключевые параметры архитектуры являются интеллектуальной собственностью автора.
