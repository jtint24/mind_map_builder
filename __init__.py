from summarizer import Summarizer

import spacy


def main():
    pass


def summarizer_test():
    nlp = spacy.load("en_core_web_sm")

    summarizer = Summarizer(100, nlp)

    text = nlp("""
    Kevin McCarthy is risking Donald Trump’s wrath by not officially endorsing his third White House bid, but the speaker is also fulfilling an important mission: sparing the House GOP a civil war over 2024.
While scores of McCarthy’s members have already backed Trump, plenty of other Republicans are steering clear of the polarizing former president in the GOP primary. That camp includes virtually every swing-seat lawmaker, many of whom fear that embracing Trump could spell their electoral doom next fall — as well as allies of Trump’s rivals, from Ron DeSantis to Doug Burgum.
So as much as McCarthy might risk alienating Trump by staying on the sidelines, the California Republican also provides the most political cover he can to his vulnerable members. The pressure on the speaker to choose sides will only grow throughout the summer, though, as Trump locks down support across the House GOP and questions intensify about why McCarthy isn’t fully embracing the man who helped deliver him the speakership.
Some Republicans already view McCarthy as a Trump backer in all but name. Pro-Trump Rep. Dan Meuser (R-Pa.) suggested that the speaker is subtly clearing a path for his members to rally behind the former president by the end of the primary.
Meuser summed up McCarthy’s 2024 message to House Republicans this way: “‘Hey, you're with DeSantis right now. That's OK. We get that. You're with Mike Pence, Tim Scott. But in the end, we’ve got to come together with who’s going to be our winning candidate.
""")

    summarized_text = summarizer(text)

    print(summarized_text)


if __name__ == "__main__":
    main()
