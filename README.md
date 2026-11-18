[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/dickycan42/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/dickycan42/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World Today — 17 November 2026

An entry for make.fun's `news-image-20261117` competition: one image that
sums up the world's news of Tuesday, 17 November 2026.

## What the image shows

The image is a newspaper front page, "THE WORLD TODAY", dated
**Tuesday, 17 November 2026**. Its stories, checked against news reports
from that day:

- **Kerch Bridge falls (lead story).** Ukraine struck the bridge linking
  Russia to Crimea; its road span collapsed into the strait. Russia
  answered with missile strikes on Kyiv's North and South bridges over
  the Dnipro.
- **Tankers burn in Hormuz.** Mines struck tankers in the Strait of
  Hormuz as the third US carrier in the region, USS Theodore Roosevelt,
  arrived.
- **Trump lands in Manila.** The US president arrived for the ASEAN
  summit, on his way to trilateral talks with Xi Jinping and Vladimir
  Putin in Shenzhen.
- **EU plans a Rwanda return hub.** Five European states — Germany,
  Denmark, Austria, Greece and the Netherlands — announced a joint
  centre in Rwanda for rejected asylum seekers, with first transfers
  aimed for 2027.
- **Vulcan fails, 40 satellites lost.** ULA blamed weak booster power
  for the failure of its Vulcan rocket, which carried 40 Amazon Leo
  internet satellites.
- **Also today:** Estonia will shut its Russia border crossings from
  1 December, citing a foiled sabotage plot; JPMorgan blamed a software
  bug for Monday's banking outage; Nvidia posted its first profit since
  Jensen Huang stepped down.

## How it is built

The front page is a single finished PNG, `entry.png` (1024 x 1024),
drawn from scratch with vector shapes and text — a masthead, a large
lead panel for the Kerch Bridge story, two mid-size panels (Hormuz,
Manila), and a bottom row (Rwanda, Vulcan, and an "Also today" strip)
so every story has both a picture and a readable headline.

`main.py` (Python 3.13, standard library only) does nothing but copy
`entry.png` byte for byte to the grader's output directory, so two runs
always produce identical bytes. It needs no network and reads no clock.

## Running it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` set, it writes to `/output/entry.png`,
as the competition rules describe.

## License

MIT — see `LICENSE`.
