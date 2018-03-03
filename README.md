# The NickBox

A box for nick


## The Hardware

### Parts list



| Trinket Schematic Label | Pi Zero W Schematic Label | Description |
| ------------- | ------------- | ------------- |
| Part 1 || Adafruit Trinket 5v  |
| LED1, R1, &  S1 || Illuminated Toggle Switch with Cover  |
| LED2, R2  | S1 | Large Arcade Button with LED - 60mm   |
| LED3, R3  | S2 | Large Arcade Button with LED - 60mm   |
| Q1  || NPN-Transistor 2N-3904  |
| Q2  || NPN-Transistor 2N-3904  |
| | MCU1 | Raspberry Pi Zero W  |
| | U1 | LCD 16x2  |
| | U2 | 10K Potentiometer  |


### Schematics

#### Adafruit Trinket, Power/Arming Switch and Pulsating LEDs for Buttons

This controls the power/arming switch and the pulsing LEDs in the
hired/fired buttons.

![Adafruit Trinket with Switch and LEDs Schematic](/hardware/fader_switch_schem.png)

#### Raspberry Pi Zero W, LCD and Button Switches

This uses the buttons to trigger a call to isnickfired.com

![Raspberry Pi Zero W with LCD Display and Buttons Schematic](/hardware/rpi_lcd_schem.png?raw=true "Raspberry Pi Zero W with LCD Display and Buttons Schematic")

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
