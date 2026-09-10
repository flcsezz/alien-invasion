# Alien Invasion (Enhanced Edition)

A 2D arcade space shooter built with Python and Pygame. While initially following the *Python Crash Course (3rd Edition)*, this version introduces advanced custom mechanics, including 4-directional ship movement, multiple switchable weapon modes, distinct projectile types, fire-rate balancing, and an active weapon overheating/cooling system.

---

## Features

### 1. Full 4-Directional Movement
- Unlike the classic left/right-only movement, the ship can navigate freely in all four directions (**Up**, **Down**, **Left**, **Right**) with boundary clamping to keep the ship within the screen.
- Dual control support: navigate seamlessly using either **WASD** or the **Arrow Keys**.

### 2. Multi-Mode Weapon System
Switch between three distinct combat modes on the fly using number keys:
- **Mode 1 - Single Cannon (`Key 1`)**: Fires a single projectile from the center of the ship (`BulletM`). Low heat generation and balanced fire delay.
- **Mode 2 - Dual Cannon (`Key 2`)**: Fires twin projectiles simultaneously from the left and right wings (`BulletL` and `BulletR`).
- **Mode 3 - Tri-Cannon (`Key 3`)**: Fires three bullets at once across the left, center, and right cannons. Maximum firepower at the cost of higher heat and cooldown.

### 3. Overheat & Thermal Management
- Firing weapons continuously generates **heat** (`bullet_heat`).
- If heat reaches the critical threshold (`bullet_maxheat = 400`), the weapons **overheat** and will lock out firing.
- Letting go of the trigger or waiting through an overheat engages the active cooling system (`bullet_coolingrate = 2.3`), venting heat back to zero before weapons can fire again.

### 4. Continuous Fire & Cooldown Delays
- Hold **Spacebar** to sustain continuous fire.
- Each firing mode has an independent cooldown delay between bursts to balance rapid fire vs. high-spread firepower:
  - **Single Mode**: 450 ms delay | +10 Heat/burst
  - **Dual Cannon Mode**: 600 ms delay | +25 Heat/burst
  - **Tri-Cannon Mode**: 800 ms delay | +40 Heat/burst

### 5. Memory & Sprite Management
- Bullets that travel past the top of the screen are automatically culled from sprite groups to maintain high performance.

---

## Controls

| Action | Controls |
|---|---|
| **Move Up / Down / Left / Right** | `W` `A` `S` `D` or `↑` `↓` `←` `→` |
| **Fire Bullets** | `Spacebar` (Hold for continuous fire) |
| **Single Cannon Mode** | `1` |
| **Dual Cannon Mode** | `2` |
| **Tri-Cannon Mode** | `3` |
| **Quit Game** | `Q` or Close Window |

> **Note on Keyboard Ghosting:** When using arrow keys + spacebar on some standard/membrane keyboards, the hardware matrix may block simultaneous 3-key presses (e.g. moving diagonally while firing). For optimal responsiveness across all directions and shooting, **WASD + Spacebar** is recommended.

---

## Project Structure

- **[alien_invasion.py](alien_invasion.py)** - Main game loop, event handling, firing logic, heat management, and screen rendering.
- **[ship.py](ship.py)** - Player ship class handling 4-way positional movement, boundary checks, and blitting.
- **[bullets.py](bullets.py)** - Dedicated bullet classes (`BulletM`, `BulletL`, `BulletR`) managing individual cannon offsets and trajectory.
- **[settings.py](settings.py)** - Global configurations for screen dimensions, ship speeds, weapon heat rates, and mode delays.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Pygame

```bash
pip install pygame
```

### Running the Game
Run the main game script from the project root:

```bash
python alien_invasion.py
```