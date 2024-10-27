# Robot Project
Code for Cornell College Engineering Club's Robot Project (2024-2025)

## The Goal

Build a robot (in the spirit of FTC Robots) that can pick up and move some objects! The robot should be controlled using a Bluetooth controller, of some sort.

## Installation / Usage

* good luck have fun i havent written this yet

### Supported Controllers

* probably not a wiimote tbh

### Pairing a Controller

When running the installation script, it'll automatically launch into a pairing mode, complete with a printed guide. This can be accessed again by: `something lol`

## Controller Layout

There's two different control layouts!

### Layout 1 (Tank)

| **Button**       | **Function**                           |
|------------------|----------------------------------------|
| Left Stick (Y)   | Left Tank Tread                        |
| Right Stick (Y)  | Right Tank Tread                       |
| D-Pad Up/Down    | Arm Up/Down                            |
| D-Pad Left/Right | Manual Hand Close/Open                 |
| X                | Auto Grab                              |
| O                | Auto Drop                              |
| Triangle         | Switch Mode (Hold for 5s to Shutdown)  |
| L3 or R3         | Remote Stop (Hold for 5s to Disengage) |

### Layout 2 (Car)

| **Button**      | **Function**                           |
|-----------------|----------------------------------------|
| Left Stick      | Drive                                  |
| Right Stick (Y) | Arm Up/Down                            |
| Right Stick (X) | Manual Hand Close/Open                 |
| X               | Auto Grab                              |
| O               | Auto Drop                              |
| Triangle        | Switch Mode (Hold for 5s to Shutdown)  |
| L3 or R3        | Remote Stop (Hold for 5s to Disengage) |

### Controller Colors / Lights

| **Color**        | **Lights**        | **Meaning**        |
|------------------|-------------------|--------------------|
| Blue             | `X...`            | Layout 1           |
| Green            | `XX..`            | Layout 2           |
| Red (Solid)      | `XXXX` (Solid)    | Remote Stop Active |
| Amber            | `X.X.`            | Starting           |
| Amber (Flashing) | `XXXX` (Flashing) | Shutting Down      |
| Purple           | `.X.X`            | Errored            |

## Planning Details

There's 4 motors: 2 for tank treads, 1 for veritcal movement of arm, 1 for the gripper.
