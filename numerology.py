import helperfunctions

class numerology:
    async def run(self, message):
        # number sum
        if message.content.startswith(('!num ', '!numerology ', '!six ')):
            arr = list(' '.join(message.content.split(' ')[1:]).lower())
            total = sum(ord(c) - 96 for c in arr if 'a' <= c <= 'z')
            if message.content.startswith('!six '):
                total = total * 6
            await message.channel.send(str(total))
        elif message.content == '!num':
            await message.channel.send(helperfunctions.pick_string([
                'num num num',
                'num num num num num',
                'nom nom nom hehe',
                'num num give me gum gum',
                'num nom num nom num',
                'num num non mom',
                'num non mum nun',
                'num num nom mom mum',
                'nommy nommy nom',
                'mom',
                'num',
                'nom',
                'rum'
            ]))
        elif message.content == '!six':
            await message.channel.send(helperfunctions.pick_string([
                '6'
            ]))
        
        # rot13
        elif message.content.startswith("!rot"):
            spoilerResult = False
            args = message.content.split(' ')
            try:
                n = int(args[0][4:])
            except NameError:
                await message.channel.send(helperfunctions.pick_string([
                    "don't see a rot value for me",
                    "try specifying a number",
                    "rot"
                ]))
                return
            msg = ' '.join(args[1:]).upper()
            if msg:
                out = numerology.rot(msg, n)
                await message.channel.send(out)
            else:
                # no message, check if this is a reply
                if message.type == "reply":
                    og = message.reference.resolved
                    if og.embeds:
                        await message.channel.send(og.embeds[0].description)
                    else:
                        out = numerology.rot(og.content, n)
                        await message.channel.send(out)
                else:
                    await message.channel.send(helperfunctions.pick_string([
                        "don't see anything to rot",
                        "try specifying a string or reply",
                        "rot"
                    ]))

    def rot(msg, n):
        if msg.startswith("||") and msg.endswith("||"):
            spoilerResult = True
            msg = msg[2:-2] 
        rot = [numerology.shift(c, n) for c in msg]
        out = ''.join(rot)
        if spoilerResult:
            out = '||' + out + '||'
        return out


    def shift(c, n):
        letter = ord(c) - 65
        if 0 <= letter < 26:
            rot = (letter + n) % 26
            return chr(rot + 65)
        else:
            return c