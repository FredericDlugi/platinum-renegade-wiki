# Frequently Asked Questions

## Why is the patching not working?

- Make sure you're using the correct patch for the Platinum ROM you've obtained.
- If using a dump made from your own American cartridge, copies purchased near Platinum's original release should use the 3541 patch. Otherwise, the 4997 patch should hopefully do the job.
- Make sure you're trying to apply the patch to an .nds file (that should be 128 MB). It should not still be compressed in a .zip or .7z, and it definitely should not be an .exe!
- The patch to turn Platinum into Renegade Platinum should work without needing to uncheck the "Checksum validation" option. If you do this to force it through, it'll likely freeze in battles.
- If you are on Mac, consider using a program called MultiPatch instead (easy to find on Google). The Delta Patcher Lite tool will probably not work for you.
- Patching is a bit unreliable on mobile phones. I can't really help with problems there. You can search for prepatched ROMs online or use a PC then transfer the patched ROM to your phone.

## Why has my game frozen when trying to start the first rival battle?
- This means you've likely used the wrong ROM base. Try the patch for the other ROM base.
- If you try to force the patch through by unchecking "checksum validation" in Delta Patcher Lite, you will probably also end up with this issue.
- If you have the correct ROM base, you won't need to uncheck the "checksum validation".

##  How can I update my Renegade Platinum to a newer version?
- Renegade Platinum save files are compatible between each version, so this should be possible.
- Most emulators link the ROM name and the save file together, e.g. RenegadePlatinum.nds would have a corresponding save file RenegadePlatinum.sav.
- Please note I am referring to battery (normal) saves here done by the save menu in game. ** Save states will NOT work if you change the ROM version! **
- First, get an .nds copy of the newest Renegade Platinum. The patches must always be applied to a vanilla Platinum ROM.

### Export / Import Battery Saves (DeSmuME)

- If using DeSmuME, you can export your current battery save by going to File -> Export Backup Memory in DeSmuME to produce a .sav file. Do this while playing the old Renegade Platinum with your current save file loaded.
- Open the new ROM, then do File -> Import Backup Memory and select the .sav you just exported. Your save file should now be active.

### The Filename Switch Method

- Rename the new version of the Renegade Platinum ROM have the same filename as whatever your now old version file is.
- For example, if you were playing RenegadePlatinumX.nds on your emulator, and your new version is now RenegadePlatinumY.nds, you could rename that newer version from RenegadePlatinumY.nds -> RenegadePlatinumX.nds.
- Replace your old ROM with the new ROM.
- Boot up the new ROM on the emulator and hopefully your save file should be there.

- Please note that if you are updating from v1.0.0, v1.0.1, v1.0.2 or v1.0.3 to any newer version while keeping your save file, you will need to talk to the NPC found in any of the Pokémon Centers in Jubilife, Eterna, Hearthome or Veilstone to get everything in place in your save.

## Can I randomise Renegade Platinum?

- No, this is not possible via the Universal Pokémon Randomizer.
- Expanded files mean the internal file locations are different to normal, and the Universal Pokémon Randomizer is unable to handle this.
- This is impossible to add support for.
- You can however do it manually by transplanting files across from a randomised ordinary Platinum. Please see the [How to randomize](how_to_randomize.md) document for instructions.

## Does the boost to the shiny rate affect the Poké Radar shiny patches?

- No, the Poké Radar works off its own RNG system that will force a shiny patch when it rolls the correct number. The shiny rate change in this game doesn't affect this.

## Can I get <Pokémon name here> as a shiny?

- Yes, all Pokémon are available as shiny at whatever rate the version you're playing has (1/512 with shiny boost, 1/8192 if not).
- You need to soft reset to try to get shinies for static encounters; save states don't reroll the RNG so you'll get the same Pokémon every time.

## I'm seeing graphical distortion when walking in grass sometimes. Is this a bug?

- This is a bug, but not with the hack; it's a problem with the emulator (specifically DeSmuME that I know of).
- The graphical distortion is harmless and will go away when the screen is refreshed.
- This problem also happens with the original Platinum.

## I finished the Galactic events in Eterna City and am now stuck. What do I do?

- Go to the Bike Shop in Eterna City and talk to the owner. After this, you should be able to progress past Route 206.

## Why can't I get into Canalave City? Where am I meant to go?

- You must now visit Pal Park before you can continue into Canalave City.
- Be sure to talk to all of the NPCs at Pal Park. You're after a specific item to get past the guard blocking you!

## Where can I find the ROM base for Renegade Platinum?
- Can't give you a link here, unfortunately. But they do exist on the Internet.