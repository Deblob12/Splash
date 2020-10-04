# Splash

Splash is **serverless messaging bot** supporting group payments over time and providing intelligent travel recommendations. 

## The Problem

When embarking on a road trip with our friends, we almost inevitably make multiple payments over the course of our trip. Traditionally, managing who pays for what is a rather messy and decentralized process, with people usually resorting to a spreadsheet or note tab on their phone. And if we don't want to go through the rigmorale of setting any of those things up, we'll just end up splitting each payment over Venmo as we go along. But that also introduces a lot of friction and potential confusion over the course of our trip. 

*There must be a better way.*

## How Splash Addresses This Problem

Splash serves as a modernized solution to this by keeping track of our payments and balances for us via an interactive messaging bot. Start by asking Splash to create a group. Engage in basic conversation with Splash to alleviate any boredom or let Splash know whenever you have a new charge. When you do, make sure to specify who pays what and Splash will automatically remember that information so you don't have to!

Feel free to also ask Splash about any fun recommendations along your trip. And when your trip has finished, let Splash know and the proper Venmo charges will be then carried out accordingly.

## Technologies Used

Splash is built with Python but also relies largely on:
* **Twilio API**, powering the entire automated messaging framework
* **Venmo API**, allowing Splash to complete the automated transaction flow
* **Firebase Realtime Database**
* and **Google Cloud Platform**

## Authors
* Jeffrey Chiu
* Jeremy Hsu

Created for IvyHacks, October 2020.
