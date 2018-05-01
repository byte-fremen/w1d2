#!/usr/bin/env python3

print('\nUmbrella Bot, Version 0.1.1   +{(0) _(0)}+\n\n')

my_answer = input('\n Is it raining?')

bring_umbrella_conditions        =['y','yes']
do_not_bring_umbrella_conditions =['n','no']

if my_answer.lower() in bring_umbrella_conditions:
    print('\nBring yout umbrella!\n')
elif  my_answer.lower() not in do_not_bring_umbrella_conditions:
    print('\nI\'m not sure about that, but I\'m always learning.')

else:

    print('\nYou probably don\'t need to bring an umbrella, today\n')

