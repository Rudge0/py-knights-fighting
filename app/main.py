from app.KNIGHTS.KnightsInfo import KNIGHTS
from app.KNIGHTS.ReformattingInfo import making_knight


def battle(knights_config: dict) -> dict:
    # Reformatting info about the Knights

    knights = {
        name: making_knight(knight)
        for name, knight in knights_config.items()
    }

# BATTLE------------------------------------------------

    # 1 Lancelot vs Mordred:

    knights["lancelot"].fight(knights["mordred"])

    # 2 Arthur vs Red Knight:

    knights["arthur"].fight(knights["red_knight"])

    # check if someone fell in battle

    for knight in knights.values():
        if knight.hp <= 0:
            knight.hp = 0

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


print(battle(KNIGHTS))
