# Splash

Splash is serverless messaging bot that supports group payments over time and provides intelligent travel recommendations. 

## The Problem

When going on road trips with our friends, we almost inevitably need to make multiple payments over the course of the the trip. Traditionally, managing who pays for what is a rather messy and decentralized process, with people usually resorting to a spreadsheet or note tab on their phone. If we don't want to go through the rigmorale of setting any of those things up, we'll just end up splitting each payment over Venmo as we go along. But that also introduces a lot of friction over the course of a trip. 

There must be a better way.

## How Splash Addresses This Problem

Splash takes care of keeping track of payments and balances for us via an interactive messaging bot. Start by asking Splash to create a group. Engage in basic conversation with Splash to alleviate any boredom or let Splash know whenever you have a new charge. When you do, make sure to specify who pays what and Splash will automatically remember that information so you don't have to!

Feel free to also ask Splash about any fun recommendations along your trip. And when your trip has finished, let Splash know and the proper Venmo charges will be then carried out accordingly.

## Technologies Used

Splash was built with Python but also relied heavily on:
* **Twilio**, powering the entire automated messaging framework
* **Venmo API**
* **Firebase**
* and **Google Cloud Platform**
