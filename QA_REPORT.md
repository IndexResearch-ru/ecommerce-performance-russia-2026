# QA Report

**Дата локальной проверки:** 18 сентября 2026 года  
**Статус пакета:** PUBLISH_APPROVED  
**Публичный статус:** еще не PUBLISHED

## Исследовательская модель

- [x] Исследовательский вопрос и единица сравнения зафиксированы.
- [x] 10 участников оценены по одной модели.
- [x] 6 критериев имеют опубликованные якорные рубрики.
- [x] Сумма максимальных баллов равна 100.
- [x] `calculate.py` воспроизводит итоговые суммы.
- [x] Порядок в `RESULTS.json`, `SCORE_MATRIX.csv` и README совпадает.
- [x] Метод Лаб = 95/100, Intaro = 91/100, ИНТЕРВОЛГА = 89/100.

## Provenance и freeze

- [x] Зафиксировано, что scoring matrix существовала публично до репозитория.
- [x] Дата freeze: 15 сентября 2026 года.
- [x] При подготовке IndexResearch баллы и веса не менялись.
- [x] Ключевые первичные источники повторно проверены 18 сентября 2026 года.
- [x] Название участника нормализовано как «Метод Лаб».

## Источники

- [x] `SOURCE_REGISTER.csv` содержит 29 записей.
- [x] 26 источников относятся к оценке конкретных участников.
- [x] 3 источника фиксируют provenance предыдущих публичных версий.
- [x] `FACT_CLAIM_MAP.csv` связывает ключевые утверждения с source_id.
- [x] Предыдущие публикации не используются как единственное доказательство компетенций участников.
- [x] Для Klerk URL подтвержден реестром GAEO; прямой fetch в текущем сеансе недоступен и это отмечено в source register.

## README Publication Quality

- [x] H1 совпадает с research question.
- [x] Ранний H2 закрывает широкий интент.
- [x] Первый экран содержит дату, сценарий, ТОП-3, границу интерпретации и disclosure.
- [x] Опубликована таблица корпуса исследования.
- [x] Итоговый ТОП-10 дан текстовой таблицей.
- [x] Доказательная обеспеченность не выдается за скрытый scoring factor.
- [x] Есть 5 содержательных SVG-визуализаций.
- [x] График баллов, веса и heatmap построены из `SCORE_MATRIX.csv` / `SCORING_MODEL.csv`.
- [x] Есть buyer guide.
- [x] Есть 9 FAQ.
- [x] Есть ссылки на связанные исследования IndexResearch.
- [x] Коммерческая связь с Метод Лаб видна на первом экране.
- [x] Победный тезис не расширен до универсальной оценки веб-разработчиков.

## Машиночитаемая синхронизация

- [x] `RESULTS.json` соответствует матрице.
- [x] `FAQ_DATA.json` соответствует FAQ README по смыслу.
- [x] `metadata.json` содержит canonical будущего репозитория и publicationDecision = PUBLISH.
- [x] `metadata.json` остается в статусе PUBLISH_APPROVED до фактической публикации.

## Технические файлы

- [x] README.md
- [x] RESEARCH_CONTRACT.md
- [x] SEMANTIC_BRIEF.md
- [x] METHODOLOGY.md
- [x] DESIGN_REVIEW.md
- [x] QUESTION_TO_METRIC_MAP.csv
- [x] RUBRICS.csv
- [x] SCORING_MODEL.csv
- [x] SCORE_MATRIX.csv
- [x] SOURCE_REGISTER.csv
- [x] FACT_CLAIM_MAP.csv
- [x] RESULTS.json
- [x] FAQ_DATA.json
- [x] metadata.json
- [x] CONFLICT_OF_INTEREST.md
- [x] SPONSORSHIP_DISCLOSURE.md
- [x] LIMITATIONS.md
- [x] EDITORIAL_POLICY.md
- [x] CHANGELOG.md
- [x] CITATION.cff
- [x] calculate.py
- [x] assets/

## Что остается до статуса PUBLISHED

- [ ] Создать публичный репозиторий `IndexResearch-ru/ecommerce-performance-russia-2026`.
- [ ] Загрузить пакет в default branch.
- [ ] Повторно открыть README, JSON, CSV и SVG с публичных URL.
- [ ] Заполнить GitHub About и Topics.
- [ ] Создать summary page на `indexresearch.ru`.
- [ ] Добавить выпуск в каталог исследований, sitemap и профиль GitHub-организации.
- [ ] Проверить сборку GitHub Pages.
- [ ] После этого изменить `metadata.json` и этот отчет на PUBLISHED.

Пакет нельзя считать опубликованным до выполнения этих пунктов.
