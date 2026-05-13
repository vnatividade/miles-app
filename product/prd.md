# PRD — miles-app MVP

## Objective

Construir um sistema capaz de monitorar automaticamente disponibilidade e promoções de passagens emitidas com milhas.

O sistema permitirá que usuários configurem alertas personalizados e recebam notificações quando oportunidades relevantes forem encontradas.

---

# Problem

Usuários de programas de milhas precisam monitorar manualmente múltiplos sites e datas para encontrar boas emissões.

As melhores oportunidades:
- desaparecem rapidamente
- exigem monitoramento constante
- possuem grande variabilidade de preço

---

# MVP Goal

Validar se usuários possuem interesse recorrente em monitoramento automatizado de emissões com milhas.

---

# MVP Scope

## Included

- cadastro de alertas
- scraping periódico
- normalização de resultados
- matching de oportunidades
- notificações por e-mail
- histórico de resultados

## Excluded

- aplicativo mobile
- pagamento
- emissão automática
- integração com conta de milhas
- IA generativa
- dashboard avançado

---

# Initial Programs

Priority 1:
- Smiles
- Azul

Priority 2:
- LATAM Pass

---

# Main Entities

## User

Usuário do sistema.

## Alert

Configuração de monitoramento.

## SearchResult

Resultado capturado pelos scrapers.

## Notification

Histórico de alertas enviados.

---

# Success Metric

Usuários mantêm alertas ativos continuamente porque percebem valor no monitoramento automatizado.
