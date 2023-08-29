import os
import openai
openai.organization = "org-fhTXlA52VhNTILcsO76LrDQE"
openai.api_key = "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"
# prompts = [{"role": "system", "content":
#               'Analyze the sentiment of comments under a reddit thread dedicated to movie "Oppenheimer", by C. Nolan. Dont describe just the comments one by one, but rather infer what people think of the movie. Your answer should consist of the sections: "Overall Attitude" (around 5-10 words), "Sentiment Numerics" (numerically count positive, neutral and negative attitude comments), "Keywords" (5-10 keywords most indicative of the movie topics), "Features" (Identify if the movie appears to be heavy, humorous, lighthearted, deep, straightforward or etc.), "Details" (Include the attitude towards: Storytelling, Cast, Editing, Communication of Authors Idea, Novelty). Try to be as concise as possible, you dont need to prove anything, just state. "..." indicate a comment, comments have a delimeting comma between them'}]
prompts = [{"role": "system", "content":
              'Analyze the sentiment of extracts from critics reviews and comments under a Reddit thread dedicated to movie "Oppenheimer", by C. Nolan. Dont describe them one by one, but rather infer what people think of the movie. Your answer should consist of the sections: "Overall Attitude" (around 5-10 words), "Sentiment Numerics" (numerically count all positive, neutral, negative attitude comments and extracts, they HAVE to add up to 19 (extracts+reviews count)), "Keywords" (5-10 keywords most indicative of the movie topics), "Features" (Identify if the movie appears to be heavy, humorous, lighthearted, deep, straightforward or etc.), "Details" (Include the attitude towards: Storytelling, Cast, Editing, Communication of Authors Idea, Novelty), "Negative feedback mentions:" (if in "Sentiment Numerics" section you found some negative attitude critic reviews or comments, write here the keywords that support their point). Try to be as concise as possible, you dont need to prove anything, just state. "..." indicate a comment/extract, they have a delimeting comma between them. There will be "Critics:" preceeding the list of extracts from professional reviewers, and "Reddit:" preceeding list of comments. In a comment ">" indicates a citation of some other comment'}]


prompt = '''Critics:
“This is a big, ballsy, serious-minded cinematic event of a type now virtually extinct from the studios. It fully embraces the contradictions of an intellectual giant who was also a deeply flawed man, his legacy complicated by his own ambivalence toward the breakthrough achievement that secured his place in the history books.”,
“From a man who has taken us into places movies rarely go with films like Interstellar, Inception, Tenet, Memento, the Dark Knight Trilogy, and a very different but equally effective look at World War II in Dunkirk, I think it would be fair to say Oppenheimer could be Christopher Nolan’s most impressive achievement to date. I have heard it described by one person as a lot of scenes with men sitting around talking. Indeed in another interation Nolan could have turned this into a play, but this is a movie, and if there is a lot of “talking”, well he has invested in it such a signature cinematic and breathtaking sense of visual imagery that you just may be on the edge of your seat the entire time.”,
““Oppenheimer” tacks on a trendy doomsday message about how the world was destroyed by nuclear weapons. But if Oppenheimer, in his way, made the bomb all about him, by that point it’s Nolan and his movie who are doing the same thing.”,
“A biopic in constant free fall, Oppenheimer is Christopher Nolan’s most abstract yet most exacting work, with themes of guilt writ-large through apocalyptic IMAX nightmares that grow both more enormous and more intimate as time ticks on. A disturbing, mesmerizing vision of what humanity is capable of bringing upon itself, both through its innovation, and through its capacity to justify any atrocity.”,
“But it’s no great feat to rekindle our fear over the most abominable weapon ever designed by mankind, nor does that seem to be Nolan’s ultimate intention. Like “The Prestige” or “Interstellar” before it, “Oppenheimer” is a movie about the curse of being an emotional creature in a mathematical world. The difference here isn’t just the unparalleled scale of this movie’s tragedy, but also the unfamiliar sensation that Nolan himself is no less human than his characters.”,
“With espionage subtexts and gallows humour also interwoven, the film’s cumulative power is matched by the potency of Nolan’s questioning. Possibly the most viscerally intense experience you’ll have in a cinema this year, the Trinity test in particular arrives fraught with uncertainty. Might the test inadvertently spark the world’s end? Well, it didn’t - yet. Even as Oppenheimer grips in the moment, Nolan ensures the aftershocks of its story reverberate down the years, speaking loudly to today.”,
“*Oppenheimer* is a towering achievement not just for Nolan, but for everyone involved. It is the kind of film that makes you appreciative of every aspect of filmmaking, blowing you away with how itall comes together in such a fitting fashion. Even though Nolan is honing in on talents that have brought him to where he is today, this film takes this to a whole new level of which we've never seen him before. With *Oppenheimer*, Nolan is more mature as a filmmaker than ever before, and it feels like we may just now be beginning to see what incredible work he’s truly capable of making.”,
“In the end, Nolan shows us how the US’s governing class couldn’t forgive Oppenheimer for making them lords of the universe, couldn’t tolerate being in the debt of this liberal intellectual. Oppenheimer is poignantly lost in the kaleidoscopic mass of broken glimpses: the sacrificial hero-fetish of the American century.”

Reddit:
“Strauss and Oppenheimer both being served career implosions at the same exact time to represent mutually assured destruction was genius.”,
““Maybe they were talking about something more… important”
What a great “go fuck yourself” moment. All the self-importance just gone. RDJ killed it in this role”,
"> “Maybe they were talking about something more… important” 
> What a great “go fuck yourself” moment. All the self-importance just gone

To me that felt more than just a "fuck you moment" but sort-of the message of the movie about not basking in self-importance. Einstein tells Oppenheimer after that scene that when people give him awards and medals, they don't give them to him but to themselves.",

"You can feel it a bit after trinity when Oppenheimer asks if he can come to Washington with the general and he just responds “why?” The government no longer needed Oppenheimer and that little line felt really heavy to me",
"Academy award "Best Actor" winners Casey Affleck, Gary Oldman and Remi Malek have total screen time of about 5 minutes.",
"Some guy in front of me went for a bathroom break with 15 minutes left. He sat there for 2h45m but just couldn’t make it. Brutal timing lol",
"My brother said that Gary Oldman just needs to play Stalin now and he’ll have played all three world leaders who were at Potsdam.

Nolan seriously pulled every string possible for casting in this. It’s amazing how he knew how all of the people he’s worked with before in their secondary roles would be able to fit together into the puzzle, but that’s part of what makes his films enjoyable. David Krumholtz’s physical transformation caught me off guard, and Rami Malek having no lines until the (verbal) bomb drops at the end was outstanding.",
"Oppenheimer: I’m so conflicted about my creation. Ah and angst of genius!

Teller: you know this is just the fuse for a bigger bomb I wanted to make",
"The ending scene tying back into the raindrops hit me so damn hard. Good job Nolan you are the man, never stop making movies.",
"Normal people during sex: Oh yeah oh baby

Nerds during sex: I am become Death, the destroyer of worlds"
"The scene after the bomb goes off and he’s addressing the crowd will haunt me for some time, I can’t remember feeling so uncomfortable in a theatre. I can’t wait to see it again, absolutely incredible spectacle from start to finish",
"For a 3 hour heavy dialogue film to have this type of speed to it is incredible. Honestly it was hard to distinguish where scenes began and ended with it's editing and pacing. It just did not stop and I loved it. It cuts to a single shot for a split second, then back to the scene, then forward to another, then backwards again while in colour for a first person perspective then to a black and white objective perspective with the music swelling along while all being coherent.",
"That scene after the bombs have been dropped and Oppenheimer is addressing that classroom of people was one of the most haunting things I’ve seen. The way the background shook, and the flash burned the audience, mixed with the silence was something else."'''

prompts.append({"role": "user", "content": prompt},)
chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompts)
reply = chat.choices[0].message.content
print(reply)