# ROTARY X1 — The Catalogue Photo of an Impossible Gadget

[![make.fun](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/yayass-crypto/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/yayass-crypto/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)

Entry for the make.fun competition
[The Catalogue Photo of an Impossible Gadget](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341).

## What the image shows

A photorealistic studio catalogue photograph of the **ROTARY X1** — a sleek
matte-black smartphone with a polished brass rotary telephone dial mounted
on its screen. A human finger is caught mid-dial, turning the dial to call
up an app. The single accessory is a coiled vintage black telephone cord,
lying beside the phone. Soft studio light, seamless pale-grey background,
product hero centred. The only text is product text: the brand
"ROTARY X1", a price tag reading "$1,897", and the spec line
"DIALS APPS · 0G · NO SIGNAL, EVER".

## Why it works

The joke reads at a glance, with no caption: a phone you dial like a
1950s telephone. The brass dial is mounted on the screen where the apps
would be, the finger is caught mid-turn, and the coiled cord — the one
accessory — is the only thing that could ever connect it to anything.
The styling stays straight catalogue: soft studio light, honest shadow,
manufactured materials, a price tag. Nothing in the picture explains the
joke; the product text is only the brand, the price, and the spec line.

## Run

```sh
python3 main.py
```

Writes `entry.png` (1024×1024, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR`
(default `/output`). Python 3.13 standard library only, no network.
The program copies the committed photograph verbatim and gates it first
(PNG signature, size and dimensions), so repeated runs are byte-identical.
