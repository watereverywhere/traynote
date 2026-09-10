# Traynote

[![traynote](https://snapcraft.io/traynote/badge.svg)](https://snapcraft.io/traynote)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Quick temporary notepad in system tray for instant notes on the fly.**

> **IMPORTANT:** This is NOT a regular notepad. Traynote does NOT save data after closing. Each instance is a temporary session that lives only while its tray icon exists.

## Install

From Snap Store (recommended):

    sudo snap install traynote

Or search for **Traynote** in Ubuntu Software Center.

## How it works

- **Single left-click** on the tray icon - notepad opens instantly
- **Click on any other window** - notepad collapses to tray, keeping the text for the current session
- **Launch multiple Traynote instances** - each one is independent with its own notes
- **Right-click the tray icon -> Quit** - notepad closes permanently and all its data is discarded

Perfect for quick scratch notes, copying text between windows, and fast reminders - without opening heavy apps.

## Features

- Instant access from system tray
- Beige "paper" background
- Ctrl+Z / Ctrl+Y (works with any keyboard layout)
- Word wrap
- Strict confinement - no network, no telemetry
- English UI

## Requirements

- Ubuntu 22.04 or newer (or any distro with snapd)
- GTK 3 (bundled inside the snap)

## Build from source

    git clone https://github.com/watereverywhere/tray-notepad.git
    cd tray-notepad
    snapcraft clean && snapcraft
    sudo snap install traynote_*.snap --dangerous

## License

MIT (c) 2026 dss
