from func import all_co2, all_hum, create_reminder, date, time, take_command, all_temp, set_temperature, greet_me, talk, bedroom_unit, garage_unit, kitchen_unit
from reminder import remind_me

def main():
    date()
    time()

    while True:

        #openCmd = take_command()
        openCmd = "Open assistant"

        if "Open" and " assistant" in openCmd:

            greet_me()

            #command2 = take_command()
            command2 = "electron"

            if 'electron' in command2:

                talk("Yes, I am listening")

                while True:

                    command3 = take_command()
                    #command3 = " what is the temperature in the bedroom unit "
                    if 'exit' in command3:
                        break


                    if ('bedroom' in command3) or (command3 == 'bedroom'):
                        bedroom_unit(command3)


                    elif 'kitchen' and 'readings' in command3:
                        kitchen_unit(command3)


                    elif 'garage' and 'readings' in command3:
                        garage_unit(command3)


                    elif 'can i set my temperature alarm values' in command3:
                        set_temperature()


                    elif 'what are my homes temperature values' in command3:
                        all_temp(command3)


                    elif 'what are my homes temperature values' in command3:
                        all_hum(command3)


                    elif 'what are my homes temperature values' in command3:
                        all_co2(command3)

                    elif 'set a sensor reminder' in command3:

                        talk("No problem.What time would you like to set it for?")

                        timeCmd = take_command()
                        timing = int(timeCmd)

                        remind_me(timing)

                    else:
                        talk("Invalid command")
                    talk("Is there anything else you need?")

            else:
                command2 = take_command()
                if 'why' and 'not' in command2:
                    talk("I am not talking to you, because you never said my name!")


main()
