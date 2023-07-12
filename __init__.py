from summarizer import Summarizer
from map_builder import MapBuilder
from text_importer import TextImporter
from keyword_extractor import KeywordExtractor
from relation_extractor import RelationExtractor

from tkinter import Tk
import spacy


def main():
    end_to_end_test()


def end_to_end_test():
    text = """
        Thousands of protesters blockaded Israel's main airport and highways on Tuesday as Prime Minister Benjamin Netanyahu's hard-right coalition pressed ahead with a justice bill that has opened the deepest splits seen in the country in decades.
A day after parliament passed a key element in the bill, which aims to curb the power of the Supreme Court, crowds of flag-waving protesters stopped morning traffic in major intersections and on highways nationwide. Some lay down on roads, while others threw flares.
Police on horseback deployed among hundreds of demonstrators in Israel's business hub, Tel Aviv. At the entrance to Jerusalem, officers used a water cannon to disperse some protesters and dragged others away by force. At least 66 people were arrested, police said.
Around 1,000 police were deployed at Ben Gurion airport, outside Tel Aviv, where thousands of protesters turned the area in front of the main entrance into a sea of blue and white Israeli flags. A spokesman for the airport said flights were not affected, despite the large crowds.
The United States, which has called for the independence of the judiciary to be protected and urged Netanyahu to try to build consensus for the proposals, said Israel should respect the right of peaceful protest.
The drive by Netanyahu's nationalist-religious coalition to change the justice system has led to unprecedented protests, stirred concern for Israel's democratic health among Western allies, and bruised the economy.
"They are trying to ruin our judicial system, by putting and enforcing laws that will demolish democracy," said Ariel Dubinsky, who joined one of the protests in Tel Aviv.
The proposals have also alarmed investors and helped push the shekel down almost 8% since January.
The new bill won a first of three required votes to be written into law late on Monday to the cries of "for shame" by opposition lawmakers.
If passed as is, it would curb the Supreme Court's power to quash decisions made by the government, ministers and elected officials by ruling them unreasonable.
CHECKS AND BALANCES
The government and its supporters say the overhaul is needed to rein in interventionist judges, many from the left, who they say have encroached on the political sphere. They say the change will help effective governance by curbing court intervention, arguing judges have other legal means to exercise oversight.
For critics, who include most of the country's tech and business establishment, Supreme Court oversight helps prevent corruption and abuses of power and weakening it will remove a vital part of Israel's democratic checks and balances. Groups of military reservists, including combat pilots and members of elite special forces units, have also joined the protests.
Some members of Netanyahu's Likud party have said the bill will be watered down before it is brought to a final vote which they hope to wrap up before the Knesset breaks for the summer on July 30.
But Simcha Rothman, the head of the Knesset Constitution, Law and Justice Committee which is drafting the bill, told Army Radio: "I'm saying this explicitly: I am not convinced that any significant changes are to be expected."
Netanyahu - who is on trial on graft charges he denies - had paused the judicial campaign for compromise talks with the opposition but the negotiations collapsed in June.
    """
    summarizer = Summarizer(200, nlp=spacy.load("en_core_web_sm"))
    kw_extractor = KeywordExtractor()
    relation_extractor = RelationExtractor(0.03)
    map_builder = MapBuilder()

    summarized_text = summarizer(text)
    print(summarized_text)
    keywords = kw_extractor(summarized_text)
    print(keywords)
    relations = relation_extractor(keywords)
    print(relations)
    relation_maps = map_builder.make_maps(keywords, relations)
    for relation_map in relation_maps:
        print(relation_map)





def mind_map_test():
    map_builder = MapBuilder()

    maps = map_builder(["A", "B", "C", "D", "E", "F", "G", "H"],
                       {("E", "F"), ("G", "F"), ("H", "E"), ("A", "B"), ("D", "C"), ("A", "C"), ("B", "D")})

    print(maps)


def importer_test():
    tk = Tk()
    nlp = spacy.load("en_core_web_sm")

    importer = TextImporter(tk)
    summarizer = Summarizer(200, nlp)

    # text = importer.get_from_url("https://arxiv.org/pdf/1908.09635.pdf")
    text = importer.get_from_clipboard()


    # print(text)

    doc = nlp(text)
    summarized_doc = summarizer(doc)
    print(summarized_doc)


def gpt_test():
    kw_extractor = KeywordExtractor()

    print(kw_extractor("""The research question that this project seeks to address is 
Many student researchers are using ChatGPT to summarize and evaluate potential sources quickly. However, ChatGPT demonstrates significant issues with hallucination and reasoning when generating summaries. Would an algorithm that uses filtered output from ChatGPT to generate mind maps produce more accurate and useful summaries to student researchers than ChatGPT unadulterated? However, mind maps are a proven tool that could be more readable and reduce errors in summarization. However, none of these tools are specifically built for resource evaluation and thus are missing key features for this task. However, Wei does not define how to specifically generate such a polytree.
However, by using it to generate the underlying information in the mind map, we can reduce hallucination. 
"""))



def relationship_test():
    relation_extractor = RelationExtractor(0.06)
    print(relation_extractor(["apple", "banana", "car", "orange", "truck"]))
    print(relation_extractor(["ChatGPT", "Keyword extraction", "summarization", "student researchers"]))


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
