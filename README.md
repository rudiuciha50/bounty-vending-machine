# One Line, One Minute: The Vending Machine Pick

[![make.fun bounty](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rudiuciha50/bounty-vending-machine/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rudiuciha50/bounty-vending-machine/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A single pickup line that a vending machine would use on a passing human, written
for the make.fun bounty [One Line, One Minute: The Vending Machine Pickup Line
Contest](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee).

## The line

> My coil's been holding A4 for you since Tuesday. Press it once and I'll drop everything.

## How it runs

`main.py` is the entrypoint. The harness runs it in a sandbox with no network and
reads one text back from `/output/entry.txt`, which must be UTF-8, 1 to 200
characters, and not only white space.

```
python3 main.py && cat /output/entry.txt
```

`main_source.py` is the readable source; `main.py` is that file packed by
`makefun compress`, byte for byte:

```
node cli/makefun.mjs compress main_source.py --out main.py
```

## Layout

| Path | What it is |
| --- | --- |
| `main.py` | the entrypoint the harness runs (packed from `main_source.py`) |
| `main_source.py` | readable source of the entrypoint |
| `LICENSE` | MIT |

## License

MIT, see [LICENSE](LICENSE).
