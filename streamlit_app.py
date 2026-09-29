import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="The Seven Labours of Rostam",
    page_icon="⚔️",
    layout="centered",
)

BASE_DIR = Path(__file__).parent


def show_image(filename):
    """Display an image/GIF if it exists in the app folder."""
    path = BASE_DIR / filename

    if path.exists():
        st.image(str(path), width="stretch")
    else:
        st.warning(f"Missing image file: {filename}")


def set_scene(scene):
    """Move the player to a new scene."""
    st.session_state.scene = scene


def restart():
    """Restart the game from the title screen."""
    st.session_state.scene = "intro"


# Give every new player their own starting scene.
if "scene" not in st.session_state:
    st.session_state.scene = "intro"

scene = st.session_state.scene


# ---------- SIMPLE VISUAL STYLING ----------

st.markdown(
    """
    <style>
    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    .game-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: .04em;
    }

    .game-subtitle {
        text-align: center;
        opacity: .75;
        margin-top: -.5rem;
        margin-bottom: 1.5rem;
    }

    .scene-label {
        text-align: center;
        font-size: .9rem;
        letter-spacing: .18em;
        text-transform: uppercase;
        opacity: .65;
        margin-bottom: .4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def scene_header(number, title):
    """Heading and progress bar for each labour."""
    st.markdown(
        f'<div class="scene-label">Labour {number} of 7</div>',
        unsafe_allow_html=True,
    )
    st.header(title)
    st.progress(number / 7)


def game_over(message, image_filename):
    """Reusable Game Over screen."""
    st.error("☠️ GAME OVER")
    st.write(message)

    show_image(image_filename)
    show_image("GameOver.gif")

    st.button(
        "↻ Play again from the beginning",
        type="primary",
        width="stretch",
        on_click=restart,
        key=f"restart_{scene}",
    )


# ============================================================
# INTRO
# ============================================================

if scene == "intro":

    st.markdown(
        '<div class="game-title">THE SEVEN LABOURS OF ROSTAM</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="game-subtitle">A Choose Your Own Adventure Game</div>',
        unsafe_allow_html=True,
    )

    show_image("Hero_rides_toward_mountains_light.gif")

    st.subheader("Welcome, brave warrior!")

    st.write(
        "King Kay Kāvus and his army have been captured by the demons of "
        "Mazandaran. Their sight has been stolen, and their fate now rests "
        "in your hands."
    )

    st.write(
        "You are Rostam, the legendary Persian hero. Accompanied by your "
        "loyal horse, Rakhsh, you must journey through seven dangerous "
        "trials to rescue the king and defeat the terrifying White Demon."
    )

    st.write(
        "**Choose wisely.** Every decision can bring you closer to "
        "victory—or lead you to your doom."
    )

    with st.expander("How to play"):
        st.write(
            "Read each scene and click one of the two choices. "
            "A wrong decision can end your journey immediately. "
            "Survive all seven labours to win."
        )

    st.button(
        "⚔️ Begin the adventure",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour1",),
        key="begin",
    )


# ============================================================
# LABOUR 1 — THE LION
# ============================================================

elif scene == "labour1":

    scene_header(1, "The Lion")

    st.write(
        "After a long ride, you are resting with your horse. "
        "A fierce lion is approaching."
    )

    st.write("**What will you do?**")

    st.button(
        "💤 Keep sleeping",
        width="stretch",
        on_click=set_scene,
        args=("gameover_lion",),
        key="l1_sleep",
    )

    st.button(
        "⚔️ Wake up and investigate",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour1_win",),
        key="l1_wake",
    )


elif scene == "gameover_lion":

    game_over(
        "A fierce lion attacks! Rakhsh fights to protect you, "
        "but he fails. Your journey ends.",
        "Lion_attacks_sleeping_man_20260919120317.gif",
    )


elif scene == "labour1_win":

    st.success("You survived the First Labour!")

    st.write(
        "You spot the lion approaching and prepare to defend yourself "
        "and Rakhsh. You defeat the lion and live to continue your journey."
    )

    show_image("Rostam_confronting_lion.gif")

    st.button(
        "Continue to the Second Labour →",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour2",),
        key="to_l2",
    )


# ============================================================
# LABOUR 2 — THE DESERT
# ============================================================

elif scene == "labour2":

    scene_header(2, "The Scorching Desert")

    st.write(
        "After surviving the lion attack, you and Rakhsh continue through "
        "a scorching desert. The sun is burning, your water is gone, and "
        "both of you are becoming dangerously thirsty and exhausted."
    )

    st.write("**What will you do?**")

    st.button(
        "🐎 Keep riding and hope to find water",
        width="stretch",
        on_click=set_scene,
        args=("gameover_desert",),
        key="l2_ride",
    )

    st.button(
        "🙏 Stop, pray for help, and look for a sign of water",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour2_win",),
        key="l2_pray",
    )


elif scene == "gameover_desert":

    game_over(
        "You ignore your thirst and continue through the scorching desert. "
        "Exhausted and dehydrated, you collapse into the sand. "
        "Your journey ends.",
        "Warrior_riding_horse_across_desert_under_10MB_v2.gif",
    )


elif scene == "labour2_win":

    st.success("You survived the Second Labour!")

    st.write(
        "A mysterious wild ram appears and guides you to a hidden spring. "
        "You and Rakhsh drink, regain your strength, and continue your adventure!"
    )

    show_image("Rostam_and_horse_following_ram_under_10MB.gif")

    st.button(
        "Continue to the Third Labour →",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour3",),
        key="to_l3",
    )


# ============================================================
# LABOUR 3 — THE DRAGON
# ============================================================

elif scene == "labour3":

    scene_header(3, "The Dragon")

    st.write(
        "Night falls, and you stop to rest. Suddenly, Rakhsh wakes you "
        "in panic. A terrifying dragon is approaching from the darkness."
    )

    st.write("**What will you do?**")

    st.button(
        "💤 Ignore Rakhsh and go back to sleep",
        width="stretch",
        on_click=set_scene,
        args=("gameover_dragon",),
        key="l3_sleep",
    )

    st.button(
        "🗡️ Trust Rakhsh and prepare to fight",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour3_win",),
        key="l3_fight",
    )


elif scene == "gameover_dragon":

    game_over(
        "You ignore Rakhsh's warning. The dragon attacks and overwhelms "
        "you while you sleep. Your journey ends.",
        "Dragon_breathing_fire_20260919120319 (2).gif",
    )


elif scene == "labour3_win":

    st.success("You survived the Third Labour!")

    st.write(
        "You draw your weapon and fight alongside Rakhsh. Together, "
        "you defeat the dragon and survive another dangerous night!"
    )

    show_image("Dragonwin.gif")

    st.button(
        "Continue to the Fourth Labour →",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour4",),
        key="to_l4",
    )


# ============================================================
# LABOUR 4 — THE SORCERESS
# ============================================================

elif scene == "labour4":

    scene_header(4, "The Sorceress")

    st.write(
        "While traveling through the wilderness, you encounter a beautiful "
        "woman playing music. She invites you to share her food and wine, "
        "but something feels strange."
    )

    st.write("**What will you do?**")

    st.button(
        "🙏 Say a prayer before accepting anything",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour4_win",),
        key="l4_pray",
    )

    st.button(
        "🍷 Trust the woman and accept her invitation",
        width="stretch",
        on_click=set_scene,
        args=("gameover_sorceress",),
        key="l4_trust",
    )


elif scene == "gameover_sorceress":

    game_over(
        "You fall into the sorceress's trap! She casts a powerful spell, "
        "leaving you helpless. Your journey ends.",
        "Musician_casts_dark_magic_spell_under_10MB.gif",
    )


elif scene == "labour4_win":

    st.success("You survived the Fourth Labour!")

    st.write(
        "Your prayer reveals her true demonic form! "
        "You defeat the sorceress and escape her deadly trap."
    )

    show_image("sorceresswin.gif")

    st.button(
        "Continue to the Fifth Labour →",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour5",),
        key="to_l5",
    )


# ============================================================
# LABOUR 5 — OLAD
# ============================================================

elif scene == "labour5":

    scene_header(5, "Olad")

    st.write(
        "You encounter Olad, a powerful warrior of Mazandaran who knows "
        "the way to the demons. After a fierce battle, you manage to capture him."
    )

    st.write("**What will you do?**")

    st.button(
        "🤝 Spare Olad and demand that he guide you",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour5_win",),
        key="l5_spare",
    )

    st.button(
        "⚔️ Kill Olad and continue alone",
        width="stretch",
        on_click=set_scene,
        args=("gameover_olad",),
        key="l5_kill",
    )


elif scene == "gameover_olad":

    game_over(
        "Without Olad's guidance, you become lost in the dangerous "
        "mountains and fall into a demonic ambush. Your journey ends.",
        "oladlose.gif",
    )


elif scene == "labour5_win":

    st.success("You survived the Fifth Labour!")

    st.write(
        "Olad agrees to guide you through the mountains and reveals the "
        "location of the demons. You continue toward the imprisoned king!"
    )

    show_image("oladwin.gif")

    st.button(
        "Continue to the Sixth Labour →",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour6",),
        key="to_l6",
    )


# ============================================================
# LABOUR 6 — ARZHANG DIV
# ============================================================

elif scene == "labour6":

    scene_header(6, "Arzhang Div")

    st.write(
        "With Olad as your guide, you finally reach the demons' stronghold. "
        "Arzhang Div, the terrifying commander of the demons, guards the "
        "path to King Kay Kavus."
    )

    st.write("**What will you do?**")

    st.button(
        "🏰 Charge directly into the fortress",
        width="stretch",
        on_click=set_scene,
        args=("gameover_arzhang",),
        key="l6_charge",
    )

    st.button(
        "🥷 Approach carefully and surprise Arzhang Div",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour6_win",),
        key="l6_surprise",
    )


elif scene == "gameover_arzhang":

    game_over(
        "You rush into the fortress without a plan. Arzhang Div and his "
        "demons surround you and launch a devastating attack. "
        "Your journey ends.",
        "Demon_launches_brutal_ambush_attack_under_10MB.gif",
    )


elif scene == "labour6_win":

    st.success("You survived the Sixth Labour!")

    st.write(
        "You surprise Arzhang Div and defeat him! You finally reach "
        "King Kay Kavus, but his sight has not returned. To save him, "
        "you must defeat the White Demon."
    )

    show_image("arzhangwin_under_10MB.gif")

    st.button(
        "Enter the Seventh Labour →",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("labour7",),
        key="to_l7",
    )


# ============================================================
# LABOUR 7 — THE WHITE DEMON
# ============================================================

elif scene == "labour7":

    scene_header(7, "The White Demon")

    st.write(
        "You finally reach the dark cave of the White Demon. "
        "The terrifying creature waits inside, and the fate of King Kay "
        "Kavus and his army depends on you. This is your final battle."
    )

    st.write("**What will you do?**")

    st.button(
        "🕯️ Wait for the right moment and prepare a surprise attack",
        type="primary",
        width="stretch",
        on_click=set_scene,
        args=("victory",),
        key="l7_wait",
    )

    st.button(
        "⚔️ Rush blindly into the cave and attack",
        width="stretch",
        on_click=set_scene,
        args=("gameover_white_demon",),
        key="l7_rush",
    )


elif scene == "gameover_white_demon":

    game_over(
        "You charge into the darkness without a plan. "
        "The White Demon overpowers you with a devastating attack. "
        "Your journey ends.",
        "Whitedemonloose.gif",
    )


# ============================================================
# VICTORY
# ============================================================

elif scene == "victory":

    st.balloons()

    st.success("🏆 VICTORY!")

    st.header("You have conquered the Seven Labours of Rostam!")

    st.write(
        "You enter the cave at the right moment and attack the White Demon. "
        "After a fierce battle, you defeat him! His blood restores the sight "
        "of King Kay Kavus and the Iranian army."
    )

    show_image("rostamwins.gif")
    show_image("1.victory.png")

    st.button(
        "↻ Play again",
        type="primary",
        width="stretch",
        on_click=restart,
        key="victory_restart",
    )


# Safety fallback in case an invalid scene value somehow appears.
else:
    restart()
    st.rerun()
