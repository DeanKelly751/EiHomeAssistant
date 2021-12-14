from func import all_co2, all_hum, date, time, take_command, all_temp, set_temperature, greet_me, talk, bedroom_unit, garage_unit, kitchen_unit
from reminder import remind_me
from training import product_chat
import schedule

def main():
    date()
    time()

    t = {'one a. m':'01:00','two a. m':'02:00','three a. m':'03:00','four a. m':'04:00',
    'five a. m':'05:00','six a. m':'06:00','seven a. m':'07:00','eight a. m':'08:00',
    'nine a. m':'09:00','ten a. m':'10:00','eleven a. m':'11:00','twelve p. m':'12:00',
    'one p. m':'13:00','two p. m':'14:00','three p. m':'15:00','four p. m':'16:00',
    'five p. m':'17:00','six p. m':'18:00','seven p. m':'19:00','eight p. m':'20:00',
    'nine p. m':'21:00','ten p. m':'22:00','eleven p. m':'23:00','midnight': '00:00'}


    while True:

        #openCmd = take_command()
        openCmd = "Open assistant"

        if "Open" and " assistant" in openCmd:

            greet_me()

            #command2 = take_command()
            command2 = "exit"

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

                        command4 = take_command()

                        setTime = t[command4]
                        talk("Your reminder has been set. Thank you")

                        job = schedule.every().day.at(setTime).do(remind_me)

                    elif "information" and "products" in command3:
                        product_chat()

                    else:
                        talk("Invalid command")
                    talk("Is there anything else you need?")

            else:
                command2 = "exit"
                if 'why' and 'not' in command2:
                    talk("I am not talking to you, because you never said my name!")

                elif 'exit' in command2:
                    break

main()


