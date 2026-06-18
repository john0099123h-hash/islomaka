"""
Konfiguratsiya fayli - Bot sozlamalari
"""
import os
from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    """Telegram bot sozlamalari"""
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    """Umumiy konfiguratsiya"""
    tg_bot: TgBot

def load_config(path: str = None) -> Config:
    """
    .env faylidan konfiguratsiyani yuklash
    """
    env = Env()
    env.read_env(path)
    
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMIN_IDS")))
        )
    )
