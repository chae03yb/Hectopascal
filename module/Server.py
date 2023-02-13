import nextcord
from nextcord.ext import commands

import pathlib
from xml.etree import ElementTree

class Server(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client

    def _read_save_data(self, save_location: str) -> dict:
        root = ElementTree.parse(
            pathlib.Path(save_location).joinpath("/working_server", "scene.xml")
        ).getroot()
        game_data = root.find(".game_data")
        diff_sett = game_data.find("difficulty_settings")
        game_sett = game_data.find("game_mode_settings")

        playlists = game_data.find("active_playlists").findall("playlist_name")

        return { 
            "activated_dlc_count": int(root.get("dlc")),
            "activated_playlists": [ 
                # list(map(
                #     str.split("/"),
                #     playlists,
                # ))
                mission.split("/")[3] for mission in playlists
            ],
            "game_data": {
                "currency":        int(game_data.get("currency")),
                "research_point":  int(game_data.get("research_point")),
                "date": f"{game_data.get('year')}-{game_data.get('month').zfill(2)}-{game_data.get('day').zfill(2)}",
                "time": f"{game_data.get('hour').zfill(2)}:{game_data.get('minute').zfill(2)}"
            },
            "difficulty_setting": {
                "vehicle_damage":    diff_sett.get("vehicle_damage"),
                "player_damage":     diff_sett.get("player_damage"),
                "npc_damage":        diff_sett.get("npc_damage"),
                "starting_currency": diff_sett.get("starting_currency"),
                "fast_travel":       diff_sett.get("fast_travel"),
                "teleport_vehicle":  diff_sett.get("teleport_vehicle"),
                "lightning":         diff_sett.get("lightning"),
                "aggressive_animals": {
                    "shark":     diff_sett.get("sharks"),
                    "megalodon": diff_sett.get("megalodon")
                }
            },
            "game_mode_setting": {
                "day_night_length": int(game_sett.get("day_night_length")),
                "sunset":           int(game_sett.get("sunset")),
                "creative_menu":        game_sett.get("creative_menu"),
                "base_island":          game_sett.get("base_island").split("/")[2][:-4],
                "ceasefire":            game_sett.get("ceasefire"),
                "cleanup_vehicle":      game_sett.get("cleanup_vehicle"),
                "despawn_on_leave":     game_sett.get("despawn_on_leave")
            }
        }

def setup(client: commands.Bot) -> None:
    client.add_cog(Server(client))