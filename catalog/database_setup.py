from catalog_app import db
from catalog_app.models import Class, Player, Toon
from datetime import datetime


# populate the database with data
dh = Class(class_name='Demon Hunter',
            class_info='Forgoing heavy armor, Demon Hunters capitalize on speed, closing the distance quickly to strike enemies with one-handed weapons. However, Illidari must also use their agility defensively to ensure that battles end favorably.')
db.session.add(dh)

druid = Class(class_name='Druid',
            class_info="Druids are versatile combatants, in that they can fulfill nearly every role - healing, tanking, and damage dealing. It's critical that druids tailor the form they choose to the situation, as each form bears a specific purpose.")
db.session.add(druid)

monk = Class(class_name='Monk',
            class_info='Whatever their combat role, monks rely mainly on their hands and feet to do the talking, and on strong connection with their inner chi to power their abilities. Abilities such as Expel Harm and Chi Wave both heal their allies while at the same time damaging their enemies.')
db.session.add(monk)

warlock = Class(class_name='Warlock',
                class_info='Warlocks burn and destroy weakened foes with a combination of crippling illnesses and dark magic. While their demon pets protect and enhance them, warlocks strike at their enemies from a distance. As physically weak spellcasters bereft of heavy armor, cunning warlocks allow their minions to take the brunt of enemy attacks in order to save their own skin.')
db.session.add(warlock)

mage = Class(class_name='Mage',
            class_info='Mages demolish their foes with arcane incantations. Although they wield powerful offensive spells, mages are fragile and lightly armored, making them particularly vulnerable to close-range attacks. Wise mages make careful use of their spells to keep their foes at a distance or hold them in place.')
db.session.add(mage)

shaman = Class(class_name='Shaman',
            class_info="During combat, shaman place damaging and controlling totems on the ground to maximize their effectiveness while hindering their enemies. Shaman are versatile enough to battle foes up close or at range, but wise shaman choose their avenue of attack based on their enemies' strengths and weaknesses.")
db.session.add(shaman)

dk = Class(class_name='Death Knight',
            class_info='Death Knights engage their foes up-close, supplementing swings of their weapons with dark magic that renders enemies vulnerable or damages them with unholy power. They drag foes into one-on-one conflicts, compelling them to focus their attacks away from weaker companions. To prevent their enemies from fleeing their grasp, death knights must remain mindful of the power they call forth from runes, and pace their attacks appropriately.')
db.session.add(dk)

priest = Class(class_name='Priest',
                class_info='Priests use powerful healing magic to fortify themselves and their allies. They also wield powerful offensive spells from a distance, but can be overwhelmed by enemies due to their physical frailty and minimal armor. Experienced priests carefully balance the use of their offensive powers when tasked with keeping their party alive.')
db.session.add(priest)

rogue = Class(class_name='Rogue',
            class_info='Rogues often initiate combat with a surprise attack from the shadows, leading with vicious melee strikes. When in protracted battles, they utilize a successive combination of carefully chosen attacks to soften the enemy up for a killing blow. Rogues must take special care when selecting targets so that their combo attacks are not wasted, and they must be conscious of when to hide or flee if a battle turns against them.')
db.session.add(rogue)

hunter = Class(class_name='Hunter',
            class_info='Hunters battle their foes at a distance, commanding their pets to attack while they nock their arrows and fire their guns. Though their missile weapons are effective at short and long ranges, hunters are also highly mobile. They can evade or restrain their foes to control the arena of battle.')
db.session.add(hunter)

paladin = Class(class_name='Paladin',
            class_info='Paladins stand directly in front of their enemies, relying on heavy armor and healing in order to survive incoming attacks. Whether with massive shields or crushing two-handed weapons, Paladins are able to keep claws and swords from their weaker fellows - or they use healing magic to ensure that they remain on their feet.')
db.session.add(paladin)

warrior = Class(class_name='Warrior',
            class_info="Warriors equip themselves carefully for combat and engage their enemies head-on, letting attacks glance off their heavy armor. They use diverse combat tactics and a wide variety of weapon types to protect their more vulnerable allies. Warriors must carefully master their rage - the power behind their strongest attacks - in order to maximize their effectiveness in combat.")
db.session.add(warrior)

db.session.commit()