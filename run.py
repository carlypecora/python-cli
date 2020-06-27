#!/usr/bin/env python3
import argparse


cards = [
	{
		'front': 'Hello',
		'back': 'Hola'
	},
	{
		'front': 'World',
		'back': 'Mundo'
	},
	{
		'front': 'Food',
		'back': 'Comida'
	}
]

def print_cards():
	for card in cards:
		print('{}. Front: {}'.format(cards.index(card), card['front']))
		inp = input('What is the correct translation? ')
		print(check(inp, card['back']))

def check(inp, back_of_card):
	if inp.lower() == back_of_card.lower():
		return '{} is the correct answer'.format(inp.title())
	return '{} is the wrong answer. The correct answer is {}'.format(inp.title(), back_of_card)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='to print')

    subparsers = parser.add_subparsers(dest='action', 
                                       help='the action to be taken')

    parser_print = subparsers.add_parser('print_cards', help='print card deck')


    args = parser.parse_args()

    if args.action == 'print_cards':
        print_cards()

    else:
        parser.print_help()


