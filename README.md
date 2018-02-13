# Telegram-Bot

This is a telegram bot to control my fan.
An arduino nano controls my fan through relay. That arduino itself is controlled by a raspberry pi,
which hosts this telegram bot. Communication of both devices uses serial communication.
Stupid, I know.

Hardware:
- Arduino Nano AT328P, port D8 for relay 
- Raspberry Pi 3
- A table fan, of course
- A relay
Arduino connected to Raspberry via USB.
