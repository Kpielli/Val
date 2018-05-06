# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Val")
define jerry = Character("Jerry")
define odd = Character("Guy in the corner")

# The game starts here.

label start:

    $ xp_points = 0 #general points
    $ strength_points = 0 #strength
    $ dexterity_points = 0 #being able to do hand work like lockpicking
    $ wisdom_points = 0 #knowledge like a wise wizard would have. magic.
    $ charisma_points = 0 #abilty to lead and have power
    $ intellect_points = 0 #knowledge like a science dude would have

    $ orange_juice_bottles = 0

    $ effort_path = 0
    $ whatev_path = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg street

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "val happy.png" to the images
    # directory.

    show val happy

    # These display lines of dialogue.

    v "Hey, I'm Val."

    v "I'm a Tech Geek, Weeb, and Rebelling teen."

    menu:
        "Character decision. Effects the identity of Val."

        "I'm looking for an adventure to prove myself":

            $ effort_path += 1

            jump adv1

        "I'm just take what life has to give me":

            $ whatev_path += 1

            jump whatev1

label adv1:

    v "I'm a self proclaimed adventurer and hacker."

    v "Which is why I'm in this shopping street at this late at night."

    v "This late being around 12:07 if the clock is right."

    v "I made it a while ago so it might have broken by now. Shoot, I should have fixed it when I had the chance."

    v "Anyway I'm going to a bar to catch up with the guys who work there."

    jump bar1

label whatev1:

    v "Because honestly, I don't care that much about stuff."

    v "People tend to say I'm a super chill person cus of that."

    v "Though I guess they don't see me hanging around in random allyways at ~12 at night."

    v "0r that I like getting drinks at sus bars. But whats wrong with that huh."

    jump bar1

label bar1:

    scene bg street align left
    with fade

    v "Ugh forgot what a garbage dump this place was."

    show val happy at left

    menu:
        v "But if I'm here I might as well do something."

        "talk to Jerry, the bartender":

            show jerry cross at right
            with fade

            $ charisma_points += 1

            v "Hey Jerry guess who's here!"
            jerry "Oh no, of course it's little Val, back at my alcohol bar to get orange juice isn't it."
            v "Nah, I'm here to talk. What's up?"
            jerry "Nothing much. You, girl?"
            v "I'm great! I feel like a well oiled machine cus I'm getting so good at hacking that my keyboard is almost a part of me! It's great!"
            jerry "Huh, I didn't know people started to feel that way if they got into computer work. Weird."
            jerry "Speaking of which, I've been hearing that a lot of people have been going missing around here."
            v "What do you mean by missing? Like, dead? Or like 'ran away from their wives'?"
            jerry "I'd say closer to dead honestly. They've just completly disapeared."
            v "Some mob or gang or something?"
            jerry "No idea. No one is claiming it as their work..."
            jerry "All I'm saying is stay safe okay girl. You're younger than you think. You don't know how to feel fear yet."
            v "I'm not even THAT young. And I know fear!"
            jerry "No. You shouldn't. Now, do you want a cup of juice?"

            menu:
                "Yes please!":
                    $ strength_points += 1

                    v "I love this stuff."
                    jerry "Yeah I know. Always have since you were a kid."
                    "He sounds so nostalgic that you feel bad. Him and your mom were close since they were younger, and he hated remembering when she was alive."
                    "He breaks out of it, and looks at you again."
                    jerry "Run along girl, go find friends your own age."
                    return

                "Nah.":
                    v "I really want to say yes, but I should get going though."
                    jerry "Yeah. You loved this stuff since you were a kid so I'd feel bad letting you leave without some though."
                    jerry "Here just take some in a bottle."
                    "Jerry hands you a bottle of orange juice and you remember coming here with your mom when you were younger. Jerry and her had been friends since childhood."
                    v "Thanks. Means a lot."
                    $ orange_juice_bottles += 1
                    return

        "get a drink":

            $ strength_points += 1

            v "ah~ I needed this."

            "You feel refreshed after your cup of orange juice that the bartender gave you with an eyeroll."

            "You're glad you didn't get a beer, even though no one would have cared that you're underaged, because it would have just made your head hurt."

            return

        "talk to the odd guy in the corner":

            $ charisma_points += 1

            show oddguyincorner at right
            with fade

            v "hey dude whats up."
            odd "I was expecting you"
            v "uhh... no you weren't."
            v "i just chose to walk over to you, so..."
            odd "No, I knew you'd come here. And I was waiting."
            v "Oookay molestor much? I'm friends with Jerry, the guy who owns this bar, so don't try to mess with me here."
            "The guy laughs under his breath."
            odd "I'm not into 5 year olds, don't worry."
            v "I'm not five!"
            odd "No you're not. You're 19, I know."
            v "How do you know that? Creep."
            "Val moves away from the man who gets up and grabs her wrist. She frees herself from his grasp and runs off."

            hide oddguyincorner
            show jerry cross at right
            with fade
            $ charisma_points += 1

            jerry "Hey little girl. What happened?"
            v "weirdo grabbed my wrist."
            "Jerry leans towards Val in concern. She waves him off."
            v "I'm just annoyed because he knew who I was."
            jerry "Thats odd, but a lot of people can buy information so don't be too freaked out over something like that. Just keep to yourself and don't go messing in peoples buisness."
            v "Yeah yeah thanks."
            jerry "You here from orange juice?"
            v "I've grown up from when my mom used to take me here, stop treating me like a child!"
            "Jerry looks offended"
            v "Sorryyyy. I just meant I'm tired of people looking after me like I'm a baby just because my mom died."
            jerry "Yeah. Forget that you're almost 20. Proud of you, you know."
            menu:
                v "It's getting awkward so I want to wrap this up."
                "Can I actually have orange juice in a bottle to go?":
                    $ orange_juice_bottles += 1
                    return
                "I need to go, but I'll come back again soon.":
                    return

    # This ends the game.

    return
