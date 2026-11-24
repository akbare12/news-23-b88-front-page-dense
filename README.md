# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b88-front-page-dense/rank.svg)](https://make.fun/leaderboard/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b88-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image summing up 23 November 2026's world news: the AI rout that hit Asia
(Kospi −3.3%), the UN chief's call to regulate AI before it's too late, and the
US lead over China falling to a record low — plus 28 more stories, a world map
with numbered pins, and a DATE CHECK box that keeps other days' news out.

## How it is built

`draw.py` (PIL) renders `entry.png` (1024×1024, ≤1 MiB). `main.py` is
stdlib-only: it validates the PNG header and chunks, then copies `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png` — never next to itself, so it also runs
from a read-only copy.

Run it:

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Stories (31)

**Heroes:** AI rout hits Asia · Guterres: regulate AI before it's too late ·
US lead over China at record low. **10 cards:** Bessent demands Nvidia
answers · FBI probes NCIC hack · Trump: Iran strikes may resume in New Year ·
Nasdaq futures +3% · Skubal's $450M Mets deal · Tom Jackson dies at 75 ·
States sue SpaceX over AI safety claims · Anthropic IPO $107.3B · Poland:
3 missiles crossed airspace (CLAIM) · Russian nuclear satellite (CLAIM).
**Also on Monday (18):** Paris 2% billionaire tax · Manchester 12,000 cleared ·
Zelenskyy: 165 Russian missiles in a week · COP31: the day after Antalya pact
rejected · Benghazi probe (CLAIM) · Israel unity talks · Gaza strike ·
West Bank settler attacks · Iran war: no deal in sight · Lebanon 264 kg
explosives · Bahrain plant strike · Sudan drones (CLAIM) · DRC Ebola teams ·
Bangladesh: Hasina jailed if she returns · Seoul exam chaos · SK Telecom
−7.3% · China margin rules · Seoul 10T-won fund.

## Sources

Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN ·
Lowy Institute (Asia Power Index 2026). All times UTC. Figures as reported
23 Nov 2026. Scenes are drawn illustrations, not photographs.
