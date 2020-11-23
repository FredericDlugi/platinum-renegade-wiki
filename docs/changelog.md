# Changelog

## v1.3.0 - 16/04/2019

#### Breaking Changes:
* The patching system for the hack has changed.
- There's now a base patch to change your Platinum into Renegade Platinum, one each for the 3541 numbered ROM and the 4997 numbered ROM.
- You can then apply smaller patches on top of Renegade Platinum, including the classic mode, more normal shiny rates and a speed up patch to make the game faster.

For details on applying these smaller patches, please see the README included in the folder with them.
The base Renegade Platinum that you get after the initial patch uses what was previously the Complete and Shiny Boosted version (i.e. all Pokémon changes are present and the shiny rate is 1/512).

#### New Features:
- You can now battle Steven when talking to him in Oreburgh City if you've defeated the Pokémon League.
- A Hidden Power teller NPC has been placed in the Jubilife Trainers' School. He can tell you the type of your Pokémon's Hidden Power (but not the power, sadly).
- The obedience check for traded Pokémon in battles has been disabled. This means all Pokémon - including those from the trades in the game - should listen to you at all times. Relevant dialogue has been modified to reflect this.
- Pokémon now have their encounter locations listed accurately inside the Pokédex. (Big thanks to Mikelan98 for this!)

#### Pokémon changes (both versions):
- Spheal now evolves into Sealeo at Level 24.
- Sealeo now evolves into Walrein at Level 40.
- Aron now evolves into Lairon at Level 24.
- Lairon now evolves into Aggron at Level 40.
- Sealeo's level up move levels have been adjusted.
- Walrein's level up move levels have been adjusted.
- Lairon's level up move levels have been adjusted.
- Aggron's level up move levels have been adjusted.
- Glalie can now learn Rock Tomb by TM.
- Zigzagoon, Linoone, Gligar and Gliscor can now learn Rock Climb by HM (they have access to the move in Gen V onwards).
- Oddish, Gloom and Vileplume have had their level up moves reshuffled and Oddish and Gloom now learn Sludge by level.

#### Changes:
- The man in Celestic Town that gives you various "glasses" items now gives you all items when spoken to instead of an item depending on the time.
- The boy who talks to you as you enter Oreburgh City now gives you an Oval Stone (helpful if you get Happiny from the Egg you receive in the school).
- The item changes document now lists the location of key items.

#### Bug Fixes:
- Modified Maylene's dialogue when entering Route 217 to avoid the text getting cut off if the player's name was long.
- The rock that appears on Fullmoon Island now uses the Moss Rock overworld, preventing the player from destroying it by using Rock Smash from the menu.
- Fixed an error where the encounters for fishing in the wild document didn't match what was in game.
- Fixed an error in the wild document listing Floatzel as a 30% encounter at night on Route 213.
- Fixed a couple Trainers that had "nd" in their name instead of an ampersand (&).
- Fixed a couple Trainers who didn't have their rematch teams properly edited.
- Fixed a bug where one of Lucian's Pokémon was the incorrect level.
- Fixed a bug where some Trainers in Victory Road had a Dusknoir and Banette incorrectly knowing Shadow Force.

## v1.2.1 - 18/01/2019

#### Pokémon changes (both versions):
- Glalie can now learn Rock Polish by TM.

#### Changes:
- The NPC who fixes saves from the earlier versions now doesn't affect the Celebi event. Instead, you should now be able to interact with the shrine in Celestic Town again after updating to v1.2.1 and then subsequently get the Celebi event working. This does mean that people who already caught Celebi can get a second Celebi!

#### Bug Fixes:
- Fixed a bug where the Celebi event failed to activate. If you previously collected the GS Ball from the shrine, the event should work now.

## v1.2.0 - 14/01/2019

#### New Features:
- A scientist in the Berry Master's house on Route 208 now sells you Berries normally unobtainable in Platinum (e.g. Liechi, Salac).
- The Moss Rock and the Ice Rock have returned. While they no longer have an effect on Eevee, they will give you a Leaf Stone and an Ice Stone respectively.
- Added a "Type Changes" document that lists a justification for each type change as well as the types that are changed for any Pokémon.
- Added a "Frequently Asked Questions" document that has answers to some of the more common questions received.

#### Pokémon changes (both versions):
- Chikorita, Bayleef and Meganium now learn Draining Kiss and Moonblast by level.
- Totodile, Croconaw and Feraligatr now learn Night Slash by level.
- Milotic now learns Moonblast by level.
- Glalie is now able to learn Rock Slide by level and TM, and Stone Edge, Rock Smash and Rock Climb by TM/HM.

#### Pokémon changes (Complete version only):
- Meganium is now Grass/Fairy type.
- Feraligatr is now Water/Dark type.
- Milotic is now Water/Fairy type.
- Glalie is now Ice/Rock type.

#### Bug Fixes:
- Fixed a bug where Ghost-type attacks were neutral effectiveness against Dark-type Pokémon.
- Fixed a bug where Ghost-type attacks were not very effective against Dragon-type Pokémon.
- Fixed a bug where the NPC that upgrades your save was sometimes making the Celebi event not work.
- Fixed a bug where the Deoxys event wouldn't work by modifying the event slightly. This should now work on save files where it didn't before (if the League has been beaten).
- Fixed a bug where a pair of Trainers in Wayward Cave didn't see far enough to force a double battle.
- Fixed a bug where Volkner incorrectly used two normal Rotom in his Battleground rematch instead of the Heat and Wash forms.
- Fixed a bug where you could battle the Snowpoint Temple guards with only one Pokémon, causing you to send out a glitch.
- Fixed a bug where an NPC in the Veilstone Department Store made a reference to giving you the Counter Pokétch app, which never happened in Renegade Platinum.
- Fixed a bug where Combusken and Blaziken learn Fire Blast instead of Flare Blitz.

## v1.1.2 - 02/01/2019

#### Bug Fixes:
- Fixed a bug where Stealth Rock was doing seemingly random amounts of damage.
- Fixed a bug where talking to the new NPCs in the Old Chateau would crash the game.
- Fixed a bug where the Eevee in the intro of the game reverted back into a Buneary.
- Fixed an error in the Pokémon Changes document listing Charizard with the wrong ability.

# v1.1.1 - 01/01/2019

#### Bug Fixes:
- Fixed a bug where the game would crash when interacting with the Galactic grunts that were harassing the Honey seller in Floaroma Meadow.

## v1.1.0 - 01/01/2019

#### Breaking Changes:
- The base ROM for the hack has changed from the 3541 numbered dump to the 4997 (4998 on some sites) numbered dump. This should match a dump from a genuine American Platinum cartridge (unless the cart was bought near initial release).

#### Breaking Bug Fixes:
- Trigger scripts (scripts that activate when you step in a certain place) have had their internal indexes changed to prevent potential bugs.
- The GS Ball now replaces the Loot Sack instead of the Shoal Shell. The Shell Bell item sprite is fixed as a result.

** IMPORTANT NOTE - TRIGGER FIXES **
If you're carrying a save file over from an older version, please *immediately* go to the Pokémon Center in Eterna, Hearthome, Veilstone or Jubilife. Talk to the NPC in the center of the room to synchronize the state of the trigger scripts between the old and new versions. Failure to do so means you may see certain roadblocks start blocking you again, or certain events repeating that had already been completed. There may be some small hiccups if you're in odd situations with some events (e.g. the Mira stuff is only half done) but it should work okay.

** NOTE - GS BALL **
Due to the GS Ball now replacing a different item, you may find that a GS Ball that was in your inventory from a previous save will now be a Shoal Shell. This does not affect the Celebi event as that doesn't actually check for the item itself and just that you've picked it up, but you will need to do the step described above.

#### New Features:
- Pokémon natures now also show the stat boost after the nature's name. (Thanks to @Bobtree1998 for the suggestion!)
- Remoraid is now able to be found in Route 208 (allowing an earlier Mantyke evolution if you get it from the Jubilife Egg).
- Rock Climb is now a Rock-type move, but has had its power reduced to 80.
- Rowan now gives you 10 Repels straight after giving you the Poké Radar.
- Sand Tomb has been replaced with the move Bulldoze from later generations and has been distributed accordingly.
- The big room in Iron Island now has a nurse who will heal your Pokémon.
- The in-game menu is now decapitalised.
- The Move Deleter is now found in a house in Oreburgh City.
- The National Pokédex now needs to be completed enough that you can view the diploma before you can obtain the Azure Flute to get Arceus.
- The Pokémon Center nurse's dialogue has been reduced.
- You no longer need to show Gardenia a Snover to enter Eterna's Gym. Instead, you will need to find Gardenia herself on Route 216 before you can enter Eterna's Gym.

#### Changes:
- Dawn and Lucas now use Seals on their starter in the later battles.
- Roark, Gardenia and Fantina have had their teams adjusted slightly.
- The dialogue concerning the new section after Celestic Town where you visit Pal Park has been updated to make your destination a lot more obvious.
- The maid in the Old Chateau now only gives you an Old Gateau if you don't already have one in your inventory. Additionally, her dialogue has been changed.
- Traynee now lists her stat training options in High, Medium and Low order instead of Low, Medium and High.
- Traynee's stat training teams now use Pokémon that will only use harmless moves and do not have status causing abilities.

#### Pokémon changes (both versions):
- Illumise now learns Draining Kiss and Moonblast by level, but no longer learns Charge Beam or Thunderbolt. (It still can learn Thunderbolt by TM!)
- Leafeon is now compatible with the Cut HM.
- Monferno, Infernape, Azumarill, Electivire and Dusknoir are now compatible with the Drain Punch TM.
- Mudkip, Marshtomp and Swampert now learn Aqua Tail slightly earlier.
- Ninetales is now compatible with the Psychic and Shadow Ball TMs.
- Roselia now learns Sludge and Sludge Bomb by level, but no longer learns Leaf Storm. (Roserade still does!)
- Shedinja is now compatible with the Swords Dance TM.
- Swablu and Altaria now learn Moonblast slightly earlier.
- Unown's catch rate has been boosted from 225 to 255.
- Venusaur now learns Earth Power by level.
- Wailmer and Wailord now learn Body Slam by level, but no longer learn Thrash.

#### Pokémon changes (Complete version only):
- Altaria is now Dragon/Fairy and has had its stats buffed slightly (again).
- Arbok has had a slight buff to its stats.
- Dusknoir now gets the Iron Fist ability instead of Frisk when evolved from a Dusclops with the Frisk ability. (This does not apply to Frisk Dusclops caught before the patch).
- Illumise is now Bug/Fairy and has had a buff to its stats (again).
- Sceptile is now Grass/Dragon and has had its stats adjusted slightly.
- Seviper is now Poison/Dark and has had its stats modified (again).
- Swablu is now Fairy/Flying and has had its stats buffed slightly (again).
- Typhlosion now gets the Adaptability ability and has had its stats modified (again).
- Vibrava and Flygon now get Compoundeyes when evolved from a Trapinch that has the Hyper Cutter ability.
- Volbeat has had a buff to its stats (again).

** NOTE - ABILITIES **
The new abilities will not retroactively apply to these Pokémon if you carry over a save file. They only get applied to either new Pokémon or when an existing one evolves.

#### Bugs fixed:
- All Trainers now correctly have dialogue shown after being defeated.
- Barry now has a Seal on his starter again in the battles from Pastoria City onwards.
- Charmander, Charmeleon and Blastoise now correctly learn Dragon Pulse by TM.
- Fairy-type now displays correctly in the Pokédex. (Massive thanks to Mikelan98 for this one!)
- Fixed a bug where Crasher Wake and the Gym guide that sat outside his gym would reappear.
- Fixed a bug where the game would sometimes crash in Wayward Cave if you tried to leave after Mira joins you.
- Fixed a bug where the Surf wild data was incorrect on Route 208.
- Fixed a bug where the temporary guard on Route 209 would allow you past after blocking you once.
- Fixed a bug where you could use Rock Climb to get up to the summit of Mt. Coronet earlier than intended.
- Fixed a bug where you sat on top of the Eevee Poké Ball if you got KOed early (the Poké Ball has been moved).
- The Dark and Normal type Trainers on the postgame island should now always be challengeable.
- The Eterna Forest trainer no longer says "My MEDITITE!".
- The hidden Heart Scale on Route 213 has been moved and is now accessible.
- The two new forced double battles in the game will now not allow you to progress if you only have one Pokémon in the party.

#### Bugs still remaining:
- Evolving a Wailmer into Wailord while in an area connecting to a Regi room will disable the warp into the Regi room until the map reloads.
- Gengar's mini sprite looks a bit strange on the Pokétch.
- Some Trainer names may appear a little odd (double battles or the actual Frontier Brain battles in the Battle Frontier).
- Some trainers in the game (notably Dawn/Lucas) give you $0 upon victory.
- The event with Rowan's briefcase in his lab might act a bit strangely if you do it just after the Distortion World is completed.

## v1.0.3 - 27/12/2018

#### Features:
- Bidoof and Bibarel now learn TM75, Swords Dance.
- Tropius now learns TM59, Dragon Pulse.
- Trapinch now appears in Oreburgh Mine at a 10% rate.
- Ampharos now learns Dragon Pulse at Level 30 and Thunder Punch at Level 1 instead.
- Traynee now heals you after any battle you have with her.
- Item Changes and Move Changes documents now outline exactly what was replaced.
- Wild Giratina now hold the Griseous Orb.
- Pichu, Cleffa, Igglybuff, Togepi, Azurill, Budew, Chingling and Happiny now have a base happiness of 180.
- Slowpoke, Slowbro and Slowking are now able to learn HM07, Waterfall.
- The Item Changes and Move Changes documents now explicitly state what each replaced item/move was turned into.

#### Bugfixes:
- Fixed Dunsparce and Purugly not appearing in Route 208 and Route 209 with the Poké Radar respectively.
- Slowbro now correctly learns TM55, Scald.
- Nidoking's level up moves now match the document.
- Fixed some typos in the documents.

## v1.0.2 - 23/12/2018

#### Documentation Fixes
- Fixed Maylene's Lucario having the wrong item listed.

#### Game Fixes
- Actually fixed some incorrect level up moves, including Wood Hammer Glaceon.
- Fixed Blastoise not being able to learn Dark Pulse via TM.
- Fixed Breloom not being able to learn False Swipe by TM.
- Fixed Wormadam's Sandy and Trash forms not having Battle Armor as an ability in the Complete version.

## v1.0.1 - 22/12/2018

Thank you to the community for reporting bugs with the game and documents.
Saves from v1.0.0 are fully compatible with this version.

#### Changes:
- Dratini, Dragonair and Dragonite now learn Aqua Jet by level.
- Heracross can now learn Bullet Seed by TM.
- Beldum, Metang and Metagross now have a catch rate of 45, up from 3.
- Added an Evolution Changes document.

#### Documentation Fixes:
- Fixed a bad description of Scald's new effect in the Move Changes document.
- Added unlisted gift Pokémon to the Special Events guide.
- Added unlisted NPCs to the NPC Changes guide.
- Fixed Mars' Purugly incorrectly listing Covet in its moveset in the Trainer Pokémon document.
- Added a note about minimal Egg Cycles in the Pokémon Changes document.
- Fixed Munchlax incorrectly being listed as a wild Pokémon in Route 203.
- Fixed Lasses Sarah and Samantha having each other's Pokémon listed in the Trainer

#### Game Fixes:
- Fixed Cubone not showing up in the wild on Route 203 outside of the morning.
- Fixed incorrect encounters on Route 228 in the day and night.
- Fixed Pachirisu's new stats not adding up to the expected total (+5 to Sp. Atk base).
- Fixed Scald being incorrectly coded as a contact move.
- Fixed an NPC stating there were Rock Smash rocks in Ravaged Path on Route 204.
- Fixed an overlap of NPC and item on Route 209.
- Fixed an issue where you could jump over a ledge on top of a youngster on Route 203.
- Fixed a bunch of incorrect level up moves, including Wood Hammer Glaceon. Big thanks to @BurnSombreroBrn for helping track those down.
- Fixed a bug where Dawn would incorrectly use Lucas' dialogue on Route 202.
- Fixed a bug where you were able to dismount your bike on Route 206 and potentially get stuck.
- Fixed a bug where you could walk through the Galactic grunt blockade on Route 205.
- Fixed a bug where Traynee, the trainer NPC, would only let you fight Lv. 35 Chansey after beating Crasher Wake instead of Maylene.
- Fixed dialogue referring to the Pokétch being available via coupons.
- Fixed dialogue referring to Secret Potion and Black Glasses as one word.
- Fixed dialogue where there was a typo in Cheryl's text in Eterna Forest.

#### Known Issues:
- Fairy-types are incorrectly listed as Ghost-types in the Pokédex.
- If you faint early in the game and reappear in your house, you stand on top of the Poké Ball on the cushion.
- A Psychic in Eterna Forest talks about their Meditite when they don't have one.
- The game will send out a glitch as your second Pokémon when entering scripted double battles with only one Pokémon in your party.
- Some trainers in the game (notably Dawn/Lucas) give you $0 upon victory.
- Some trainers in the game have no dialogue after being defeated.

## v1.0.0 - 21/12/2018
Initial release.

