""" Plugin entry point for helga """
from helga.db import db
from helga.plugins import command, random_ack
from elo import rate_1vs1 as rating


_HELP_TEXT = """Please refer to README for usage: https://github.com/narfman0/helga-elo#examples"""
DEFAULT_ELO = 800


@command('elo', help=_HELP_TEXT, shlex=True)
def elo(client, channel, nick, message, cmg, args):
    if args[0] == 'add' and len(args) == 4:
        game_name = args[1]
        winner_name = args[2]
        loser_name = args[3]
        winner_elo, loser_elo = add_result(game_name, winner_name, loser_name)
        return '{} now has {} elo, {} now has {} elo'.format(winner_name, winner_elo, loser_name, loser_elo)
    elif args[0] == 'list' and len(args) == 3:
        game_name = args[1]
        player_name = args[2]
        player_elo = get_player_elo(game_name, player_name)
        return '{} has {} elo for {}'.format(player_name, player_elo, game_name)
    elif args[0] == 'drop' and len(args) == 2:
        drop_game(args[1])
        return random_ack()
    return "I don't understand args %s" % str(args)


def add_result(game_name, winner_name, loser_name):
    """ Add the result of a game between winner_name and loser_name """
    winner_elo = get_player_elo(game_name, winner_name)
    loser_elo = get_player_elo(game_name, loser_name)
    winner_elo, loser_elo = rating(winner_elo, loser_elo)
    set_player_elo(game_name, winner_name, winner_elo)
    set_player_elo(game_name, loser_name, loser_elo)
    return (winner_elo, loser_elo)


def set_player_elo(game_name, player_name, elo):
    """ Set the elo of a player_name in a game_name """
    db.elo[game_name].update_one({'name': player_name}, {'$set': {'elo': elo}}, upsert=True)
    return elo


def get_player_elo(game_name, player_name):
    """ Retrieve the elo of a player_name in a game_name """
    player = db.elo[game_name].find_one({'name': player_name})
    if player is not None:
        return player['elo']
    return DEFAULT_ELO


def drop_game(game_name):
    """ Remove all results from a game_name """
    db.elo[game_name].drop()
