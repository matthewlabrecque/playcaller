# Development Roadmap of Playcaller

## Overview
The goal is to have a working beta by the time of the University of New Hampshire Spring 2026 CS Poster Symposium.

## What is the planned use flow of Playcaller?
1. Select the target package manager (options currently supported are `apt`, `dnf`, `pacman`, and `brew`)
2. Select package/package libraries that you want added to your Playbook (this list will be semi-dynamically updated in that packages that are incompatible won't be allowed, such as you can't add KDE Neon to a brew Playbook)
3. If you have a Linux package manager selected, you will be prompted if you want to add Flatpak support via Flathub. On Arch systems, you will also be prompted to add the yay AUR helper.
4. If a package you select for installation allows custom configurations (such as BASH, ZSH, Neovim) it will offer to import your file and save it to the directory that will be created for deployment via GNU Stow.

## Objectives for Playcaller to be declared an Alpha build
- Basic functionality must be met
- Host a server from repology which everyday pulls the current package list for the managers and returns an API
- Ability to create Ansible playbook without custom configuration

## Objectives for Playcaller to be declared a Beta build
- Add in a feature to "Audible" a Playcall file to a different package manager
- Addition of custom configuration deployment with GNU Stow
- Support for script placement

## Objectives for Playcaller to be declared a full release
- Ability to import existing Playcalls for adjustment/tuning
