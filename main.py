#!/usr/bin/env python

import PlexLib
import time
import calendar


class PrintChat:
    @staticmethod
    def on_message(channel, message):
        utctime = time.strptime(message['date'], '%Y-%m-%dT%H:%M:%S+00:00')
        timestamp = time.strftime("%H:%M:%S", time.localtime(calendar.timegm(utctime)))
        if message['user']:
            if message['type'] == 'normal':
                print(f"[{channel}] ({timestamp}) <{message['user']['name']}>: {message['content']}")
            elif message['type'] == 'tip':
                print(
                    f"[{channel}] ({timestamp}) <Tip:{message['user']['name']}>: {message['content']} ({message['credits']} PD)")
            elif message['type'] == 'subscription':
                print(f"[{channel}] ({timestamp}) <Tip:{message['user']['name']} Has Just Subscribed!>")
            if message['content'].split(' ')[0] == '!trigger':
                PlexLib.send_message(channel, 'Reaction Message')
        elif message['type'] == 'milestone':
            print(f"[{channel}] ({timestamp}) <Milestone Reached>: {message['content']}")
        elif message['type'] == 'system':
            print(f"[{channel}] ({timestamp}) <System>: {message['content']}")

    @staticmethod
    def on_messagedeleted(channel, message_id):
        print(f"[{channel}] Message Deleted with ID: {message_id}")

    @staticmethod
    def on_viewercountupdate(channel, viewers):
        print(f"[{channel}] Viewer count update: {viewers}")

    @staticmethod
    def on_milestoneupdate(channel, milestones, progress):
        print(f"[{channel}] Milestones (Update): {milestones} Progress: {progress}")

    @staticmethod
    def on_milestonereached(channel, milestones, progress):
        print(f"[{channel}] Milestones (Reached): {milestones} Progress: {progress}")

    @staticmethod
    def on_tip(channel, milestones, progress, top):
        if milestones:
            print(f"[{channel}] Tip! Milestones (Reached): {milestones} Progress: {progress}\nTop Tippers: {top}")
        else:
            print(f"[{channel}] Tip! Top Tippers: {top}")

    @staticmethod
    def on_userupdate(channel, user):
        print(f"[{channel}] User Update: Name:{user['name']}")

    @staticmethod
    def on_streamstart(channel, milestones, progress, top, title, tags, start_time, public):
        print(
            f"[{channel}] Stream Started!\nMilestones (Reached): {milestones} Progress: {progress}\nTop Tippers: {top}\nStream Title: {title}\nStream Tags: {tags}\nStart Time UTC: {start_time}\nPublic? {public}")

    @staticmethod
    def on_streamupdate(channel, milestones, progress, top, title, tags, start_time, public, nsfw):
        print(
            f"[{channel}] Stream Started!\nMilestones (Reached): {milestones} Progress: {progress}\nTop Tippers: {top}\nStream Title: {title}\nStream Tags: {tags}\nStart Time UTC: {start_time}\nPublic? {public} NSFW? {nsfw}")

    @staticmethod
    def on_streamend(channel, status):
        print(f"[{channel}] Stream Status: {status}")

    @staticmethod
    def on_streamerupdate(channel, user):
        print(f"[{channel}] Streamer Updated: {user}")

    @staticmethod
    def on_tipsuggestions(channel, tips):
        print(f"[{channel}] Tip Suggestions Updated: {tips}")

    @staticmethod
    def on_experiencereceived(amount, level_stats):
        print(f"Experience ({amount}): {level_stats}")

    @staticmethod
    def on_newreward(message, reason, amount):
        print(f"Reward ({amount}): {message} ({reason})")

    @staticmethod
    def on_followedstreamstart(message, streamer):
        print(f"Followed Stream Started: {message}\n{streamer}")

    @staticmethod
    def on_creditbalanceupdate(t_credits):
        print(f"New credit balace: {t_credits} PD")


PlexLib.register_callback("on_message", PrintChat.on_message)
PlexLib.register_callback("on_messagedeleted", PrintChat.on_messagedeleted)
PlexLib.register_callback("on_viewercountupdate", PrintChat.on_viewercountupdate)
PlexLib.register_callback("on_milestoneupdate", PrintChat.on_milestoneupdate)
PlexLib.register_callback("on_milestonereached", PrintChat.on_milestonereached)
PlexLib.register_callback("on_tip", PrintChat.on_tip)
PlexLib.register_callback("on_userupdate", PrintChat.on_userupdate)
PlexLib.register_callback("on_streamstart", PrintChat.on_streamstart)
PlexLib.register_callback("on_streamupdate", PrintChat.on_streamupdate)
PlexLib.register_callback("on_streamend", PrintChat.on_streamend)
PlexLib.register_callback("on_streamerupdate", PrintChat.on_streamerupdate)
PlexLib.register_callback("on_tipsuggestions", PrintChat.on_tipsuggestions)
PlexLib.register_callback("on_experiencereceived", PrintChat.on_experiencereceived)
PlexLib.register_callback("on_newreward", PrintChat.on_newreward)
PlexLib.register_callback("on_followedstreamstart", PrintChat.on_followedstreamstart)
# PlexLib.set_tips(PlexLib.format_tips({'testtip': 10, 'testtip 2': 20, 'testtip 3': 30}))
# PlexLib.set_stream_info("Test Title", True, True, False, PlexLib.format_milestones(
#     {"Milestone 1": 80, "Milestone 2": 120, "Milestone 3": 160, "Milestone 4": 200}), ["set", "some", "tags"])
