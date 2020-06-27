#!/usr/bin/env python3
import argparse
import csv
import time
import os

def study_deck(file):
	with open(file) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            print(f'Column names are {", ".join(row)}')
	            line_count += 1
	        else:
	        	print('Front: {}'.format(row[0]))
	        	inp = input('What is the correct translation? ')
	        	check, boolean = check_input(inp, row[1])
	        	print(check)
	        	print()
	        	line_count += 1
	        clear()
	print(f'Finished {line_count - 1} cards in deck.')

def check_input(inp, back_of_card):
	if inp.strip().lower() == back_of_card.strip().lower():
		phrase = 'CORRECT'
		boolean = True
	else:
		phrase = 'WRONG. The correct answer is {}'.format(back_of_card)
		boolean = False
	return phrase, boolean
  
def clear():
	time.sleep(1)
	# for windows
	if os.name == 'nt':
		_ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
	else:
		_ = os.system('clear')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='to print')
    subparsers = parser.add_subparsers(dest='action', 
                                       help='the action to be taken')

    parser_study = subparsers.add_parser('study_deck', help='print card deck')
    parser_study.add_argument('csv', metavar='CSV', help='The deck of cards you would like to study')


    args = parser.parse_args()

    if args.action == 'study_deck':
        study_deck(args.csv)

    else:
        parser.print_help()


