=====  Drazards Dungeon  =====

This is a small text based adventure i am working on. It is pretty simple at the moment.

there are a few main commands to utilize while you navigate the castle:



move around the map using

'n' North

's' South

'e' East

'w' West



During an encounter you may use:

'a' Attack an enemy

'h' Heal (if below 100 hp)



At any time within the game you may use these functions:

'c' Character information

'i' Inventory

-----
Current bugs: My damage modifier only loops once because it is called via __init__. i'm not sure how to fix this.. each time you attack should be weapon.damage - [1-10] however it only works on the first attack. so if your first attcks rolls 2 damage. every attack until that monster is dead will be 2.
------



Features to be added:

More advanced combat system.
Ability to restart the game.
Description of all items and weapons.
Mini quests.
NPC characters.
Trader NPC to buy / sell gold.
Weapon upgrades.
Larger map.
More variety of enemy types and rooms.
Loot drops from enemies.
Boss monsters, rooms and loot.
Scoring feature with highscores.
Upgraded UI.
Custom map making ability.

...And more.
