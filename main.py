import socket

import dns.resolver
from mcstatus import JavaServer


def try_server(ip_address):
    try:
        conncetion = JavaServer.lookup(ip_address)
    except (IOError, ValueError) as e:
        return e

    try:
        server = conncetion.status()
    except (IOError, ValueError, ConnectionError, ConnectionRefusedError, socket.timeout, socket.gaierror,
            dns.resolver.NoNameservers) as e:
        return "Error connecting to server: {}".format(e)
    return server


def test(player_count, player_max, server_motd, server_version):
    score = 0
    if player_count >= 40:
        score += 1
    if player_max == 50:
        score += 1
    if server_motd == "A Minecraft Server":
        score += 1
    if str(server_version).__contains__("1.19"):
        score += 1
    return score


do_output = input("Output files to external document?: ")
output_bool = False
if do_output.upper() == "TRUE" or do_output.upper() == "Y" or do_output.upper() == "YES":
    output_file = open("output.json", "w")
    output_bool = True
    print("Outputting all information to 'output.json'")

input_file = open(input("Name of file to read IP addresses from... "), "r")
for ip in input_file.readlines():
    server = try_server(ip)
    if not isinstance(server, str):
        player_count = server.players.online
        player_max = server.players.max
        server_motd = server.description
        server_version = server.version.name
        result = test(player_count, player_max, server_motd, server_version)
        result_dict = {
            'ip': ip.replace("\n", ""),
            'score': result,
            'player_count': player_count,
            'player_max': player_max,
            'server_motd': server_motd,
            'server_version': server_version
        }
        if output_bool:
            output_file.write(str(result_dict))
        else:
            print(str(result_dict))

input_file.close()
output_file.close()
