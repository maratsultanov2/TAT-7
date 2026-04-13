# 🧠 TAT-7

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

*Tempus, Angulus, Tactus — una resonantia.*  
*Время, Угол, Касание — единый резонанс.*  
*时间，角度，触感 — 共振一体。*

**TAT-7** — нейросетевая архитектура с резонансной памятью для непрерывного обучения (Continual Learning).  
**TAT-7** is a neural network architecture with resonant memory for continual learning.  
**TAT-7** 是一种具有共振记忆的神经网络架构，用于持续学习。

Работает на CPU, в 20 раз меньше параметров, чем типичные CNN.  
Runs on CPU, 20x fewer parameters than typical CNNs.  
在CPU上运行，参数量比典型CNN少20倍。

---

### 🏆 Результаты | Results | 结果

| Бенчмарк | Результат | Рейтинг | Дата |
|:---|:---|:---|:---|
| REBUS | 19.40% | Топ-5 мира | 18.03.2026 |
| MNIST | 97.82% | Топ-10 мира | 19.03.2026 |
| CIFAR-10 (CL) | 91.7% | 10 задач | 2025 |
| TinyImageNet (CL) | 39.9% | 20 задач | 10.03.2026 |

---



---

### 🧠 Теоретический фундамент

**1. Multi-Head с простыми числами**
Эксперименты показали: нечётные простые числа голов (3, 5, 7) дают лучшую сходимость. Оптимум — 7 голов.

**2. Фазовые переходы (Кух-формализм)**
Плавные переходы между слоями: `W_k = w_k * e^(i * θ_k)`. Оптимальный фазовый сдвиг определён экспериментально.

**3. Резонансное восстановление памяти (RMR)**
Память о ранних задачах восстанавливается скачком при столкновении с семантически близкой задачей. Подтверждено на TinyImageNet: 5.4% → 14.0% (задача 19).

**4. Голографическое сжатие (HC)**
Состояние системы сжимается в хеш-слепок. Потеря до 90% данных не разрушает ключевую структуру.

**5. Ритмическая синхронизация (RS)**
Компоненты синхронизируются через общий ритм (автоцикл), а не через постоянную связь.

*Связь с известными концепциями: принцип Ландауэра, теория интегрированной информации (IIT), фазовые переходы в статистической физике.*


### ⚡ Быстрый старт | Quick Start | 快速开始

git clone https://github.com/maratsultanov2/TAT-7.git
cd TAT-7
python train.py --config ideal_config.json

---

### 📖 Пример использования | Usage Example | 使用示例

from tat import TAT7

model = TAT7(heads=7, phase_angle=1.987)
output = model.forward(input_tensor)

---

### 📅 История проекта | Project History | 项目历史

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

### 🔗 Экосистема TAT | TAT Ecosystem | TAT 生态系统

| Проект | Описание |
|:---|:---|
| [TreeAngleTap](https://github.com/maratsultanov2/TreeAngleTap) | Экспериментальная площадка |
| [TAT Agent Helper](https://github.com/maratsultanov2/TAT_agent_helper) | Автономный агент для лидогенерации |
| [Triplenet](https://github.com/maratsultanov2/Triplenet) | Предшественник |

---

### 👤 Автор | Author | 作者

**Марат Султанов | Marat Sultanov**  
[GitHub](https://github.com/maratsultanov2) | [Telegram](https://t.me/Marat_Sultanow)

---

### 📄 Лицензия | License | 许可证

MIT License. Ключевые параметры архитектуры являются интеллектуальной собственностью автора.  
Key architectural parameters are the intellectual property of the author.  
关键架构参数为作者的知识产权。
