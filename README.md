# Alien Invasion (Enhanced Edition) — v1.0

A feature-rich 2D arcade space shooter built with Python and Pygame. Starting from the foundation of the classic *Python Crash Course* project, this version expands the game with 4-directional ship movement, speed boosting, multi-mode weapon mechanics, weapon overheating/cooling, dynamic environmental hazards, persistent JSON-based high scores, and a data-driven 5-stage progression system with center-screen announcements.

---

## Key Features

### 1. Dynamic 4-Directional Movement & Swift Boost
- Full 4-way navigation (**Up**, **Down**, **Left**, **Right**) with screen boundary clamping.
- Dual control schemes: Navigate with **WASD** or **Arrow Keys**.
- **Swift Mode**: Hold `Left Shift` to engage afterburners and navigate at high speed (`swift_speed`).

### 2. Multi-Mode Weaponry & Thermal Management
Switch combat modes dynamically during battle:
- **Mode 1 — Single Cannon (`1`)**: Fires a single centered shot (`BulletM`). Balanced cooldown and lowest heat generation.
- **Mode 2 — Dual Wing Cannons (`2`)**: Twin synchronized shots (`BulletL` and `BulletR`) from ship wings.
- **Mode 3 — Tri-Cannon Spread (`3`)**: Maximum firepower firing all three cannons simultaneously.
- **Overheat System**: Continuous firing builds up thermal heat (`bullet_heat`). Exceeding `bullet_maxheat` triggers an emergency weapon lockout until the cooling system vents heat back down to zero.

### 3. Environmental Hazards & Enemies
- **Alien Assault**: Aliens spawn with randomized horizontal trajectories, descending with increasing aggression.
- **Asteroid Hazards**: Destructive space debris fly through the sector at varying speeds and frequencies. Asteroids destroy player ships on contact but can be blasted apart by cannons.

### 4. Data-Driven 5-Stage Progression
Progression scales seamlessly through a clean data-driven configuration without bloated conditional checks:

| Stage | Name | Score Target | Alien Speed | Spawn Delay | Hazard Density | Points/Kill |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | **Scout Patrol** | 120 | 2.5 | 1100 ms | Light Asteroids | 20 pts |
| **2** | **Asteroid Sector** | 300 | 3.2 | 900 ms | Heavy Asteroid Belt | 35 pts |
| **3** | **Vanguard Assault**| 600 | 4.0 | 700 ms | Fast Reinforcements | 50 pts |
| **4** | **Deep Space Swarm** | 1000 | 5.0 | 500 ms | Swarm Influx | 75 pts |
| **5** | **Final Invasion** | Endless | 6.2 | 380 ms | Relentless Climax | 100 pts |

### 5. UI, Stage Banners & Scoreboard
- **Live HUD**: Displays current score, active stage indicator, and persistent high score.
- **Stage Banners**: Prominent center-screen golden banner announces stage transitions for 2 seconds.
- **Interactive UI**: Custom `Buttons` class powers the start and game-over restart loop.

### 6. Persistent High Score Tracking
- High scores are saved to and loaded from `highscore.json` using Python's `json` and `pathlib` modules.
- Tracks and preserves player personal bests across sessions.

---

## Controls

| Action | Keybinding |
|---|---|
| **Move Up / Down / Left / Right** | `W` `A` `S` `D` or `↑` `↓` `←` `→` |
| **Swift Boost** | Hold `Left Shift` |
| **Fire Weapons** | `Spacebar` (Hold for continuous auto-fire) |
| **Single Cannon Mode** | `1` |
| **Dual Cannon Mode** | `2` |
| **Tri-Cannon Mode** | `3` |
| **Start / Restart Game** | Click **Play** Button |
| **Quit Game** | `Q` or Window Close |

> **Hardware Tip:** Some membrane keyboards experience matrix ghosting when pressing multiple arrow keys plus the spacebar. For the most responsive multi-key control (e.g. moving diagonally while firing), **WASD + Spacebar** is recommended.

---

## Project Structure

```text
alienInvasion/
├── alien_invasion.py     # Main loop, event routing, collisions, and stage management
├── settings.py           # Game parameters, weapon specs, assets, and stage definitions
├── game_stats.py         # Player lives, score, and JSON high score persistence
├── scoreboard.py         # HUD rendering (score, highscore, current stage, banners)
├── ship.py               # Player ship movement, boundary constraints, and blit logic
├── aliens.py             # Alien sprite behaviors and vertical update mechanics
├── bullets.py            # Projectile classes (BulletM, BulletL, BulletR)
├── backgroun_assets.py   # Falling celestial background and destructive asteroid sprites
├── button.py             # Custom interactive UI button implementation
├── highscore.json        # Persistent JSON high score storage
└── images/               # BMP game art assets (ship, aliens, planets, stars, asteroids)
```

---

## Installation & Setup

### Prerequisites
- Python 3.8+ (Supports up through Python 3.14)
- Pygame or Pygame-ce

### Installation
Clone the repository and install Pygame:

```bash
# Recommended for modern Python versions:
pip install pygame-ce

# Or standard pygame:
pip install pygame
```

### Running the Game
Launch the game directly from the project directory:

```bash
python alien_invasion.py
```