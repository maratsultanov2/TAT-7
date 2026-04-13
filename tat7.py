"""
TAT-7 — нейросетевая архитектура с резонансной памятью.
Публичная версия. Ключевые константы загружаются из защищённого хранилища.
"""

import torch
import torch.nn as nn

class TAT7(nn.Module):
    """Основная архитектура TAT-7."""
    
    def __init__(self, heads=7, phase_angle=None):
        super().__init__()
        self.heads = heads
        # ПУБЛИЧНО: phase_angle загружается из защищённого конфига
        self.phase_angle = phase_angle if phase_angle else self._load_phase_angle()
        
        # Три пути (Yang, Yin, To)
        self.yang = nn.Sequential(nn.Linear(784, 128), nn.ReLU())
        self.yin = nn.Sequential(nn.Linear(784, 128), nn.Tanh())
        self.to = nn.Sequential(nn.Linear(784, 128), nn.LeakyReLU())
        
        self.classifier = nn.Linear(128 * 3, 10)
    
    def _load_phase_angle(self):
        """Заглушка — реальное значение загружается из Google Диска."""
        # В публичной версии возвращаем None
        return None
    
    def forward(self, x):
        y1 = self.yang(x)
        y2 = self.yin(x)
        y3 = self.to(x)
        combined = torch.cat([y1, y2, y3], dim=1)
        return self.classifier(combined)
