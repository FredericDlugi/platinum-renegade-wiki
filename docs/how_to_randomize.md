# How to Randomize

Please note that you **cannot** randomize everything due to how the hack has changed things.

Trainer battles, gift Pokémon, TMs, field items and static encounters (legendaries) are off limits - you'll probably end up with crashes in places if you try to import these.

You will also be unable to carry any text changes the randomizer makes across, so you may have issues in some cases where the text change is near essential (e.g. starters, in-game trades).

This process requires the use of a computer (not a phone). This will work on Windows, I'm not sure about Mac or Linux (but if you can find an alternative to crystaltile2, that might work).

## Tools
You need the following things:

- A vanilla Platinum ROM
- A Renegade Platinum ROM
- The Universal Pokémon Randomizer (available here: https://pokehacks.dabomstew.com/randomizer/)
- crysatltile2 (available here: https://www.romhacking.net/utilities/818/)

## Steps

1. Randomize your Platinum ROM using the Universal Randomzier as normal and save it.

2. Open your now randomized Platinum ROM in crystaltile2.

3. Click the icon near the top that looks like a DS (two left of the ? button in the blue circle) to open up the file explorer for the ROM.

4. On any of these files, you are able to right click them and select "Export" to save the file to your PC.
At this point, you'll want to export the files corresponding to the elements you've randomized.
So again - find the relevant file in the list, right click it, select "Export" and save the file.
The files are as follows:











5. Next, open your Renegade Platinum ROM with crystaltile2. Again, hit the DS icon to bring up the file explorer for the ROM.

6. When right clicking the files, you should also see an "Import" button as well as the "Export" we used earlier. Simply right click on the files corresponding to the stuff you want to pull from the randomizer (the names are identical to the ones listed above), click "Import" and select the .narc you exported for that file, and that should insert it to the ROM.

7. After you've imported whatever you like, you should be able to just close crystaltile2. In my experience, it seems to save the ROM automatically, despite the message that pops up confirming shut down. Just close crystaltile2 and hit "Yes" to the prompt about being shut down.

8. Pop open the Renegade Platinum ROM you just edited in crystaltile2 in whatever emulator you use and your randomized changes should be active.

## Caveats
- As explained above, text changes will not carry across as Renegade Platinum adds a LOT of extra text strings as well as changing existing ones (move names, Pokémon names etc) so it isn't feasible to do so.

- If you've randomized the starters, you will find that the pictures when selecting them in Rowan's briefcase will not have changed - the randomizer doesn't know how to do this. It does normally change the cries and text, but as we retain the original text, it means you're reliant on the cries alone to figure out what the new starters are. Good luck!

- If you've randomized the requested Pokémon on the In-Game trades, then you'll probably have an extremely hard time figuring out what they want, as the text will still reflect what the trade originally was.

- If you've randomized wild Pokémon, the levels of the wild Pokémon will still be those of the original Platinum, instead of the boosted levels you get in Renegade Platinum. If this is a problem, you can instead use this AR code to get almost entirely random Pokémon on each wild encounter:

```
B2101D40 00000000
DA000000 000233EC
D4000000 00000001
D3000000 00000000
D7000000 02FFFD00
92FFFD00 000001ED
D5000000 00000001
D0000000 00000000
B2101D40 00000000
C0000000 0000000B
D7000000 000233EC
DC000000 00000006
D2000000 00000000
```

