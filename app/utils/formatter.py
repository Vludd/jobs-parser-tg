from app.core.dto import Vacancy
from app.utils.types import ParseMode

import logging

class MessageFormatter:
    def _format_html(self, vacancy: Vacancy) -> str:
        formatted = f'<a href="{vacancy.source}">НАЙДЕНА ВАКАНСИЯ</a>' if vacancy.source else "НАЙДЕНА ВАКАНСИЯ"
        formatted += f'\n#{" #".join(vacancy.tags)}\n' if vacancy.tags else "\n"
        formatted += f'\n<b>👨‍💻 Позиция:</b> {vacancy.position or "-"}'
        formatted += f'\n<b>🛠 Стек:</b> {", ".join(vacancy.stack) if vacancy.stack else "-"}'
        formatted += f'\n<b>💻 Трудоустройство:</b> {vacancy.employment or "-"}'
        formatted += f'\n<b>💰 Зарплата:</b> {vacancy.salary or "-"}'
        formatted += f'\n<b>🏙 Город:</b> {vacancy.city or "-"}'
        formatted += f'\n<b>🏢 Компания:</b> {vacancy.company or "-"}'
        formatted += f'\n<b>📞 Контакты:</b> {vacancy.contacts or "-"}'
        formatted += f'\n<b>🔗 URL:</b> {vacancy.url or "-"}'
        
        return formatted
    
    def _format_md(self, vacancy: Vacancy) -> str:
        formatted = f'**[НАЙДЕНА ВАКАНСИЯ]({vacancy.source})**' if vacancy.source else "**НАЙДЕНА ВАКАНСИЯ**"
        formatted += f'\n#{" #".join(vacancy.tags)}\n' if vacancy.tags else "\n"
        formatted += f'\n**👨‍💻 Позиция:** {vacancy.position or "-"}'
        formatted += f'\n**🛠 Стек:** `{", ".join(vacancy.stack) if vacancy.stack else "-"}`'
        formatted += f'\n**💻 Трудоустройство:** {vacancy.employment or "-"}'
        formatted += f'\n**💰 Зарплата:** {vacancy.salary or "-"}'
        formatted += f'\n**🏙 Город:** {vacancy.city or "-"}'
        formatted += f'\n**🏢 Компания:** {vacancy.company or "-"}'
        formatted += f'\n**📞 Контакты:** {vacancy.contacts or "-"}'
        formatted += f'\n**🔗 URL:** {vacancy.url or "-"}'
        
        return formatted

    def format(self, vacancy: Vacancy, parse_mode: ParseMode = ParseMode.HTML) -> str:
        logging.info(f"Parsing with mode: {parse_mode.value}")
        if parse_mode in [ParseMode.MARKDOWN, ParseMode.MD]:
            return self._format_md(vacancy) 
        else:
            return self._format_html(vacancy)
