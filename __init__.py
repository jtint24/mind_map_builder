from summarizer import Summarizer
from map_builder import MapBuilder
from text_importer import TextImporter
from keyword_extractor import KeywordExtractor

from tkinter import Tk
import spacy


def main():
    gpt_test()


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
